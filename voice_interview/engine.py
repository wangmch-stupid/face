"""
面试引擎 — 规则模式 + Claude API 模式
驱动整个面试流程：材料审核 → 七维度提问 → 评分/反馈
"""

import json
import os
import random
import re
import textwrap
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

from config import (
    MAJOR_BASICS,
    MAJOR_OPEN_QUESTIONS,
    MAJOR_PAPER_ABSTRACTS,
    QUALITY_QUESTIONS,
    STYLE_CONFIG,
)


@dataclass
class InterviewState:
    """面试的完整状态"""
    style: str  # stress / structured / gentle
    major: str
    resume: str
    materials: list
    dimension_index: int = 0
    question_index: int = 0
    transcript: list = field(default_factory=list)
    scores: dict = field(default_factory=dict)
    answers: dict = field(default_factory=dict)
    finished: bool = False

    # 维度顺序
    DIMENSIONS = [
        "self_intro_cn",
        "self_intro_en",
        "english",
        "project",
        "principle",
        "basics",
        "core_knowledge",
        "quality",
    ]

    DIMENSION_LABELS = {
        "self_intro_cn": "自我介绍（中文）",
        "self_intro_en": "自我介绍（英文）",
        "project": "项目经历",
        "principle": "项目原理",
        "basics": "专业基础",
        "core_knowledge": "专业核心知识",
        "english": "英文文献翻译",
        "quality": "综合素质",
    }


class RuleBasedEngine:
    """
    规则驱动的面试引擎
    不依赖外部 API，使用预定义问题库
    但可以通过回调接入 Claude API 获得智能追问
    """

    # 每个维度的时限（秒）
    DIM_TIME_LIMITS = {
        "self_intro_cn": 90,
        "self_intro_en": 90,
        "project": 120,
        "principle": 90,
        "basics": 60,
        "core_knowledge": 180,
        "english": 300,
        "quality": 90,
    }

    def __init__(self, style: str, resume: str, materials: list, major: str):
        self.style = style
        self.config = STYLE_CONFIG[style]
        self.state = InterviewState(
            style=style,
            major=major,
            resume=resume,
            materials=materials,
        )

        # 当前维度内的追问计数
        self._followup_count = 0
        self._pending_followups = []
        self._current_dim = None  # 记录当前问题所属维度，避免回答归属错位

        # 自适应难度追踪
        self._basics_correct = 0    # 专业基础连续答对数
        self._basics_weak = []      # 弱项话题列表
        self._basics_hints_given = 0  # 已给提示次数

    @staticmethod
    def _pick(options):
        """从列表中随机选一个；兼容旧的单字符串格式"""
        if isinstance(options, list):
            return random.choice(options) if options else ""
        return options or ""

    def start(self) -> str:
        """返回开场白"""
        return self._pick(self.config["opening"])

    def next_question(self) -> Optional[str]:
        """
        生成下一个问题。返回 None 表示面试结束。
        当前维度无更多问题时自动跳转到下一维度。
        """
        state = self.state

        # 优先处理待追问
        if self._pending_followups:
            return self._pending_followups.pop(0)

        # 尝试获取问题，维度耗尽时自动前进
        while state.dimension_index < len(state.DIMENSIONS):
            dim = state.DIMENSIONS[state.dimension_index]
            question = self._get_dimension_question(dim)
            state.question_index += 1

            if question is not None:
                # 记录当前问题所属维度（在可能推进前保存，防止回答归错维度）
                self._current_dim = dim
                # 有有效问题，检查是否需要在本问题后推进维度
                if self._should_advance_dimension(dim):
                    state.dimension_index += 1
                    state.question_index = 0
                    self._followup_count = 0
                return question

            # 当前维度返回了 None（追问已耗尽），自动前进
            state.dimension_index += 1
            state.question_index = 0
            self._followup_count = 0

        # 所有维度结束
        state.finished = True
        return None

    def record_answer(self, answer: str):
        """记录候选人的回答，生成追问"""
        state = self.state
        dim = self._current_dim or state.DIMENSIONS[min(state.dimension_index,
                                                         len(state.DIMENSIONS) - 1)]

        state.transcript.append({
            "dimension": dim,
            "role": "candidate",
            "content": answer,
            "time": datetime.now().isoformat(),
        })
        state.answers.setdefault(dim, []).append(answer)

        # 专业基础维度：自适应评估
        if dim == "basics":
            self._evaluate_basics(answer)

        # 超时检测
        if answer == "(超时未作答)":
            timeout_msg = self.config.get("timeout_comment", "时间到，下一个问题。")
            state.transcript.append({
                "dimension": dim,
                "role": "interviewer",
                "content": timeout_msg,
                "time": datetime.now().isoformat(),
            })
            self._pending_followups.clear()
            self._pending_followups.append(timeout_msg)
            self._force_advance_dimension()
            return

        # 英文文献翻译：检测放弃
        if dim == "english" and self._is_english_give_up(answer):
            self._pending_followups.clear()
            give_up_msg = self.config.get("english_give_up", "好的，我们跳过文献翻译环节。")
            state.transcript.append({
                "dimension": dim,
                "role": "interviewer",
                "content": give_up_msg,
                "time": datetime.now().isoformat(),
            })
            self._pending_followups.append(give_up_msg)
            self.state.scores["english"] = 2.0
            self._force_advance_dimension()
            return

        # 根据风格决定是否生成追问
        followups = self._generate_followups(dim, answer)
        self._pending_followups.extend(followups)

    def is_finished(self) -> bool:
        return self.state.finished

    def get_time_limit(self) -> int:
        """返回当前问题的时限（秒）"""
        if self._current_dim and self._current_dim in self.DIM_TIME_LIMITS:
            return self.DIM_TIME_LIMITS[self._current_dim]
        return 120  # 默认2分钟

    def get_dimension_feedback(self, dim: str) -> str:
        """结构化模式：每个维度结束时的即时反馈（返回分数+简短评语）"""
        if self.style != "structured":
            return ""

        answers = self.state.answers.get(dim, [])
        if not answers:
            return ""

        # 基于回答长度和追问情况做启发式评分
        total_len = sum(len(a) for a in answers)
        count = len(answers)
        avg_len = total_len / count

        if avg_len > 200:
            score = 8.5
            comment = "回答详实，有深度"
        elif avg_len > 100:
            score = 7.0
            comment = "回答完整，可以更深入"
        elif avg_len > 50:
            score = 5.5
            comment = "回答偏简略，建议展开"
        else:
            score = 4.0
            comment = "回答过于简短，需要充实"

        # 如果包含很多不确定词，降分
        uncertain = sum(1 for a in answers
                       if any(w in a for w in ["可能", "大概", "应该", "好像", "也许", "不太确定"]))
        if uncertain > 0:
            score -= 0.5

        # 如果被跳过、放弃或超时
        if any("(候选人选择跳过" in a or "放弃" in a or "超时" in a for a in answers):
            score = 2.0
            comment = "未作答、放弃或超时"

        dim_label = self.state.DIMENSION_LABELS.get(dim, dim)
        self.state.scores[dim] = score  # 存储以便最终报告使用
        return f"    [{dim_label} 即时评分: {score:.1f}/10] {comment}"

    def generate_report(self) -> str:
        """生成面试结束报告"""
        if self.style == "stress":
            return self._stress_report()
        elif self.style == "structured":
            return self._structured_report()
        else:
            return self._gentle_report()

    def save_transcript(self, path: str = None):
        """保存面试记录"""
        if path is None:
            transcripts_dir = os.path.join(os.path.dirname(__file__), "transcripts")
            os.makedirs(transcripts_dir, exist_ok=True)
            path = os.path.join(
                transcripts_dir,
                f"interview_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )
        with open(path, "w", encoding="utf-8") as f:
            json.dump({
                "style": self.style,
                "major": self.state.major,
                "transcript": self.state.transcript,
                "scores": self.state.scores,
            }, f, ensure_ascii=False, indent=2)
        print(f"\n[记录已保存] {path}")

    # ================================================================
    # 各维度的提问逻辑
    # ================================================================

    def _get_dimension_question(self, dim: str) -> str:
        """获取某个维度的主问题"""
        state = self.state
        qi = state.question_index

        # 过渡语（每个维度第一次进入时）
        if qi == 0:
            transition = self._pick(self.config["transitions"].get(dim, [""]))
            # 项目维度：如果有简历，个性化过渡语
            if dim == "project":
                hints = self._extract_resume_hints()
                if hints["has_resume"]:
                    if hints["project_names"]:
                        proj = hints["project_names"][0]
                        transition = f"{transition}\n\n(我注意到你参与过《{proj}》，就从它开始说吧。)"
                    elif hints["tech_words"]:
                        techs = "、".join(hints["tech_words"][:3])
                        transition = f"{transition}\n\n(你简历里提到了 {techs}，挑一个你拿手的项目来谈。)"
                    else:
                        transition = f"{transition}\n\n(我看了你的简历，挑一个最有代表性的项目来介绍。)"
                # STAR 法则引导
                if self.style == "structured":
                    transition += "\n\n💡 建议用 STAR 法则组织回答：情境 → 任务 → 行动 → 结果"
                elif self.style == "gentle":
                    transition += "\n\n💡 可以按这个顺序讲：当时什么情况 → 你要做什么 → 你具体做了什么 → 最后结果怎样"
                elif self.style == "stress":
                    transition += "\n\n结构：背景、你做了什么、结果。每个部分30秒，别啰嗦。"

            # 综合素质维度：STAR 引导
            if dim == "quality" and self.style != "stress":
                transition += "\n\n💡 行为类问题也适合用 STAR 法则来回答"
            state.transcript.append({
                "dimension": dim,
                "role": "interviewer",
                "content": transition,
                "time": datetime.now().isoformat(),
            })
            return transition

        # 根据维度生成具体问题
        if dim == "self_intro_cn":
            return self._self_intro_cn_question(qi)
        elif dim == "self_intro_en":
            return self._self_intro_en_question(qi)
        elif dim == "project":
            return self._project_question(qi)
        elif dim == "principle":
            return self._principle_question(qi)
        elif dim == "basics":
            return self._basics_question(qi)
        elif dim == "core_knowledge":
            return self._core_knowledge_question(qi)
        elif dim == "english":
            return self._english_question(qi)
        elif dim == "quality":
            return self._quality_question(qi)
        else:
            return "请继续。"

    def _self_intro_cn_question(self, qi: int) -> str:
        if self.style == "stress":
            if qi == 1:
                return "时间到。坦率说你的介绍我一个字都没记住。平庸。如果现在给你30秒重新来，你说什么？"
            elif qi == 2:
                return f"你说你对{self.state.major}感兴趣。那告诉我——你凭什么？你和别人比，有什么不可替代的地方？别跟我说勤奋努力，那是基本的。"
            else:
                return None
        elif self.style == "structured":
            if qi == 1:
                return "你提到了对某些方向的兴趣，能具体说说是什么契机让你产生这个兴趣的吗？"
            else:
                return None
        else:  # gentle
            if qi == 1:
                return "你刚才说的经历很有意思，能再多说一点吗？比如是什么事情让你对这个方向产生了兴趣？"
            elif qi == 2:
                return "除了学术之外，你平时有什么爱好？我很想了解课堂之外的你。"
            else:
                return None

    def _self_intro_en_question(self, qi: int) -> str:
        if self.style == "stress":
            if qi == 1:
                return "Your English is weak. How do you plan to read papers, write manuscripts, present at conferences? Seriously."
            elif qi == 2:
                return "Tell me the hardest technical problem you've solved — in English. No prepared scripts. Impress me."
            else:
                return None
        elif self.style == "structured":
            if qi == 1:
                return "Now please give a brief self-introduction in English. Please highlight your academic background and research interests. You have about 2 minutes."
            else:
                return None
        else:  # gentle
            if qi == 1:
                return "Don't worry about being perfect. Just tell me a bit about yourself in English — your background, what you enjoy studying, anything you'd like to share."
            else:
                return None

    def _extract_resume_hints(self) -> dict:
        """从简历中提取项目相关的关键词，返回结构化信息"""
        resume = self.state.resume
        result = {"has_resume": False, "tech_words": [], "project_names": [],
                  "keywords": [], "summary": ""}

        if not resume or resume.startswith("(跳过") or resume.startswith("(未提交"):
            return result

        result["has_resume"] = True
        snippet = resume[:500]

        # 提取英文技术词（大写/驼峰/缩写，至少3字符）
        tech_words = re.findall(r'\b[A-Z][a-zA-Z0-9\+#\-]{2,}\b', snippet)
        # 过滤通用词
        generic = {"The", "This", "That", "With", "From", "They", "Their",
                   "These", "Those", "About", "Using", "Based", "However",
                   "Introduction", "Conclusion", "Abstract", "References",
                   "University", "College", "School", "Department",
                   "GPA", "Gpa", "CV", "Resume"}
        tech_words = [w for w in tech_words if w not in generic]
        result["tech_words"] = list(dict.fromkeys(tech_words))[:5]  # 去重保留前5

        # 提取中文书名号/引号中的项目名
        cn_projects = re.findall(r'[「《『]([^》」』]{2,30})[》」』]', snippet)
        result["project_names"] = list(dict.fromkeys(cn_projects))[:3]

        # 汇总关键词
        keywords = result["tech_words"][:3] + result["project_names"][:2]
        result["keywords"] = keywords
        result["summary"] = "、".join(keywords) if keywords else ""
        return result

    def _project_question(self, qi: int) -> str:
        """项目经历追问"""
        hints = self._extract_resume_hints()
        techs = "、".join(hints["tech_words"][:2]) if hints["tech_words"] else ""
        proj = hints["project_names"][0] if hints["project_names"] else ""

        # 第一条追问（qi=1）：如果有关键词则个性化，否则用默认
        if qi == 1 and techs:
            if self.style == "stress":
                return f"你说你会{techs}——到什么程度？调包还是能改底层？别吹牛。"
            elif self.style == "structured":
                return f"我看到你提到了{techs}相关的经验。在这个项目里，你个人独立完成的技术部分占多少？请具体说明。"
            else:
                return f"你刚才提到了{techs}，我很好奇你是怎么开始接触这个方向的？有什么故事吗？"
        elif qi == 1 and proj:
            if self.style == "stress":
                return f"《{proj}》这个项目——你在里面到底做了什么？不要说'我们'，说你个人。"
            elif self.style == "structured":
                return f"关于《{proj}》，请具体说明你个人独立完成的部分，以及遇到的最大技术挑战。"
            else:
                return f"《{proj}》听起来很有意思！这个项目是怎么开始的？是你主动发起的吗？"

        if self.style == "stress":
            followups = [
                "就这个项目？技术难度在哪？我听下来谁都能做。",
                "不要说'我们'——说你。你个人到底做了什么？具体点。",
                "你做的部分占比多少？没有你项目能不能做完？说实话。",
                "重来一次你怎么改？别敷衍我，说具体技术方案。",
                "最大的一次失败或bug是什么？怎么解决的？我要听细节。",
                "你的贡献有没有创新？还是说就是调参、跑代码、复制粘贴别人的工作？",
            ]
        elif self.style == "structured":
            followups = [
                "在这个项目中，你个人独立完成的部分占多少？请具体说明。",
                "遇到的最大技术挑战是什么？你是怎么解决的？有没有尝试过但失败的方案？",
                "团队有几个人？你在其中扮演什么角色？有没有和队友产生分歧的情况？",
                "如果现在重新做这个项目，你会改变哪些技术决策？为什么？",
                "你的方案相比现有方案有什么改进或创新？有成果产出吗？",
                "从中学到的最重要的经验是什么？",
            ]
        else:  # gentle
            followups = [
                "在这个过程里，你觉得最有意思的部分是什么？有没有哪个瞬间让你觉得'啊，原来是这样'？",
                "你个人花时间最多的环节是什么？为什么花那么多时间？",
                "过程中有没有遇到过让你很头疼的问题？后来怎么解决的呢？",
                "做完这个项目之后，你觉得自己最大的变化是什么？",
            ]

        # qi=1 已由个性化追问处理，qi>=2 从 followups[0] 开始取
        idx = min(qi - 2, len(followups) - 1)
        if idx < 0:
            return followups[0] if followups else None
        return followups[idx] if idx < len(followups) else None

    def _principle_question(self, qi: int) -> str:
        """项目原理追问"""
        if self.style == "stress":
            followups = [
                "这个原理你是怎么理解的？用你自己的话。不要背书。",
                "数学基础是什么？给我推导一下。别告诉我你不会。",
                "局限性在哪？什么场景下会失效？说具体，别模糊。",
                "有没有更好的方案？为什么不选？你做过对比分析吗？",
                "还是太浅。我问的是原理层，不是应用层。往深了挖。",
            ]
        elif self.style == "structured":
            followups = [
                "这个原理的数学或物理基础是什么？它的核心假设是什么？",
                "在什么条件下这个原理成立？有没有边界情况会导致它失效？",
                "为什么选择这个方法而不是其他方法？你做过对比分析吗？",
                "在实际应用中，理论和实践的差距在哪里？你遇到过不一致的情况吗？",
            ]
        else:  # gentle
            followups = [
                "如果让你用一个生活里的比喻来解释这个原理，你会怎么比喻？",
                "这个东西最巧妙的地方在哪里？它解决了什么核心问题？",
                "它是建立在什么基础之上的？有哪些前置知识需要了解？",
                "这个原理有没有边界，在什么情况下就不好使了？没关系，想到多少说多少。",
            ]

        idx = min(qi - 1, len(followups) - 1)
        if idx < 0:
            return followups[0]
        return followups[idx] if idx < len(followups) else None

    def _basics_question(self, qi: int) -> str:
        """专业基础问题"""
        major_basics = MAJOR_BASICS.get(self.state.major, MAJOR_BASICS["计算机"])
        keys = list(major_basics.keys())

        if qi - 1 < len(keys):
            key = keys[qi - 1]
            topic, question = major_basics[key]
            return f"[{topic}] {question}"
        return None

    def _core_knowledge_question(self, qi: int) -> str:
        """专业核心知识 — 开放性问题"""
        question = MAJOR_OPEN_QUESTIONS.get(
            self.state.major,
            MAJOR_OPEN_QUESTIONS["计算机"]
        )

        if qi == 1:
            return question

        # 追问
        if self.style == "stress":
            followups = [
                "你这个方案的瓶颈在哪？想过吗？看不出来？",
                "太教科书了。实际工程中根本不是这样。你做过实验吗？还是就纸上谈兵？",
                "数据量扩大10倍，你的方案还成立吗？不成立怎么改？立刻回答。",
                "这和业界主流方案有什么本质区别？还是你只是在复现别人的东西？",
            ]
        elif self.style == "structured":
            followups = [
                "你这样设计的瓶颈在哪里？如果数据量再扩大10倍，架构需要怎么调整？",
                "你的方案和业界主流方案的异同是什么？各自的优劣？",
                "在资源受限的情况下，你会优先牺牲什么？为什么？",
            ]
        else:
            followups = [
                "你刚才提到的思路很好，能再多展开一点吗？",
                "有没有想过另一种可能性？比如从另一个角度切入？",
                "你已经考虑了几个方面，还有一个维度可能也值得关注，你觉得会是什么？",
            ]

        idx = min(qi - 2, len(followups) - 1)
        if idx < 0:
            return followups[0] if followups else None
        return followups[idx] if idx < len(followups) else None

    def _english_question(self, qi: int) -> str:
        """英文文献翻译"""
        data = MAJOR_PAPER_ABSTRACTS.get(
            self.state.major,
            MAJOR_PAPER_ABSTRACTS["计算机"]
        )
        abstract = random.choice(data) if isinstance(data, list) else data

        if qi == 1:
            return (
                f"下面是本学科一篇经典文献的原文片段，包含大量专业术语。\n"
                f"请在 5 分钟内阅读并逐句翻译成中文。\n"
                f"注意：不需要翻译完美，考察重点是专业词汇的准确理解和学术英语阅读能力。\n"
                f"如果确实无法完成，可以回复「放弃」跳过此环节。\n\n"
                f"══════════════════════════════════════\n"
                f"{abstract}\n"
                f"══════════════════════════════════════\n\n"
                f"准备好了就开始逐句翻译。"
            )

        if self.style == "stress":
            followups = [
                "这篇文献的核心贡献是什么？用一句话概括。",
                "研究方法有什么局限性？如果让你来做，你怎么改进？",
            ]
        elif self.style == "structured":
            followups = [
                "请用中文概括这篇文献的研究问题和主要结论。",
                "这篇文献的研究方法有什么优缺点？如果要应用到实际场景需要注意什么？",
            ]
        else:
            followups = [
                "你觉得这篇文献最核心的观点是什么？",
                "如果把这个研究思路用到你自己的项目上，你觉得适用吗？",
            ]

        idx = min(qi - 2, len(followups) - 1)
        if idx < 0:
            return followups[0] if followups else None
        return followups[idx] if idx < len(followups) else None

    def _quality_question(self, qi: int) -> str:
        """综合素质问题（从风格专属题库随机选取）"""
        pool = self.config.get("quality_questions") or QUALITY_QUESTIONS
        if not pool:
            return None
        return random.choice(pool)

    # ================================================================
    # 追问生成 & 维度推进
    # ================================================================

    def _generate_followups(self, dim: str, answer: str) -> list:
        """根据回答内容生成追问（规则模式，简单的关键词触发）"""
        followups = []

        if self.style == "stress":
            # 压力面：频繁追问，每个回答都要找漏洞
            if dim in ("project", "principle", "core_knowledge"):
                if len(answer) < 30:
                    followups.append("就这几个字？太敷衍了。展开！")
                if "我们" in answer and "我" not in answer:
                    followups.append("停。一直说'我们'。我问的是你。你。个人。做了什么？")
                if any(w in answer for w in ["可能", "大概", "应该", "好像", "也许"]):
                    followups.append("你用了太多不确定词。你到底知不知道？知道就说确定，不知道就说不知道。")
                if len(answer) < 100:
                    followups.append("回答太短。面试官没时间从你的只言片语里找亮点。说清楚。")

        elif self.style == "gentle":
            # 温和引导：鼓励展开
            if len(answer) < 20 and dim not in ("basics",):
                followups.append("没关系，你可以再多说一点，我很有兴趣听。")

        return followups[:2]  # 每次最多2个追问

    def _evaluate_basics(self, answer: str):
        """评估专业基础回答质量，用于自适应难度"""
        # 明显不会 / 跳过 / 太短
        weak_signals = ["不知道", "不会", "不清楚", "不了解", "没学过", "忘记了"]
        is_weak = (len(answer) < 25 or
                   answer.startswith("(候选人") or
                   any(s in answer for s in weak_signals))

        # 答得好的信号：长篇 + 含技术术语
        is_strong = len(answer) > 120

        if is_weak:
            self._basics_correct = 0
            qi = self.state.question_index
            # 获取当前问题的主题
            major_basics = MAJOR_BASICS.get(self.state.major, MAJOR_BASICS["计算机"])
            keys = list(major_basics.keys())
            if qi - 1 < len(keys):
                topic, _ = major_basics[keys[qi - 1]]
                if topic not in self._basics_weak:
                    self._basics_weak.append(topic)
            # 给提示
            if self._basics_hints_given < 3:
                self._pending_followups.append(
                    "💡 提示：可以从基本定义出发，再谈谈应用场景。不会也没关系，说说你知道的部分就好。"
                )
                self._basics_hints_given += 1
        elif is_strong:
            self._basics_correct += 1
        else:
            self._basics_correct = max(0, self._basics_correct - 1)  # 答得一般，重置计数

    def _is_english_give_up(self, answer: str) -> bool:
        """检测候选人在英文文献翻译环节是否选择放弃"""
        give_up_keywords = ["放弃", "不会翻译", "跳过翻译", "翻译不了", "看不懂",
                            "不会翻", "放弃翻译", "不想翻译", "无法翻译"]
        return any(kw in answer for kw in give_up_keywords)

    def _force_advance_dimension(self):
        """强制跳转到下一个维度（用于放弃等情况）"""
        state = self.state
        dim = state.DIMENSIONS[state.dimension_index] if state.dimension_index < len(state.DIMENSIONS) else ""
        self._current_dim = dim
        state.dimension_index += 1
        state.question_index = -1  # -1 因为 next_question() 会先 +1，这样 qi=0 触发过渡语
        self._followup_count = 0

    def _should_advance_dimension(self, dim: str) -> bool:
        """
        判断是否应该进入下一个维度
        根据风格和维度决定追问深度
        """
        qi = self.state.question_index
        style = self.style

        # 每个维度的最大问题数（含过渡语）
        max_questions = {
            "stress": {
                "self_intro_cn": 3,
                "self_intro_en": 3,
                "project": 7,
                "principle": 6,
                "basics": 9,  # 1过渡 + 8题（共12题可用）
                "core_knowledge": 5,
                "english": 4,
                "quality": 6,
            },
            "structured": {
                "self_intro_cn": 2,
                "self_intro_en": 2,
                "project": 7,
                "principle": 5,
                "basics": 7,
                "core_knowledge": 5,
                "english": 4,
                "quality": 6,
            },
            "gentle": {
                "self_intro_cn": 3,
                "self_intro_en": 2,
                "project": 6,
                "principle": 5,
                "basics": 7,
                "core_knowledge": 5,
                "english": 4,
                "quality": 6,
            },
        }

        max_q = max_questions.get(style, {}).get(dim, 3)

        # 专业基础自适应：连续答对 2 题可提前结束
        if dim == "basics" and self._basics_correct >= 2 and qi >= 4:
            return True

        return qi >= max_q

    # ================================================================
    # 报告生成
    # ================================================================

    def _stress_report(self) -> str:
        return textwrap.dedent(f"""
        ═══════════════════════════════════
          压力面模拟面试 — 反馈
        ═══════════════════════════════════

        直说了，你今天的问题不少：

        1. 自我介绍没记忆点。我没听到一个让我想录取你的理由。
        2. 项目细节经不起深挖。问你'我做了什么'你就开始绕。下次再这样，面试官直接挂。
        3. 压力追问时你明显在防御。真实面试中，回避 = 淘汰。

        把今天被问住的问题全部整理出来，每个写一段完整的回答，对着镜子练三遍。
        记住：面试官不是你的导师，不会给你第二次机会。每一次回答都要有料。

        这只是模拟。真实面试可能更残酷。好好准备，下次别再犯同样的错。
        {datetime.now().strftime('%Y年%m月%d日')}
        """).strip()

    def _structured_report(self) -> str:
        """结构化评分报告"""
        scores = self.state.scores
        # 模拟评分（实际应基于回答质量）
        dim_scores = {
            "自我介绍（中文）": scores.get("self_intro_cn", 6.0),
            "自我介绍（英文）": scores.get("self_intro_en", 5.5),
            "项目经历": scores.get("project", 6.0),
            "项目原理": scores.get("principle", 5.5),
            "专业基础": scores.get("basics", 6.0),
            "专业核心知识": scores.get("core_knowledge", 5.5),
            "英文文献翻译": scores.get("english", 5.5),
            "综合素质": scores.get("quality", 6.5),
        }

        weights = {
            "自我介绍（中文）": 0.05,
            "自我介绍（英文）": 0.05,
            "项目经历": 0.20,
            "项目原理": 0.15,
            "专业基础": 0.15,
            "专业核心知识": 0.20,
            "英文文献翻译": 0.10,
            "综合素质": 0.10,
        }

        total = sum(dim_scores[d] * weights[d] for d in dim_scores)

        if total >= 9.0:
            grade = "卓越 — 强烈推荐录取"
        elif total >= 7.5:
            grade = "优秀 — 推荐录取"
        elif total >= 6.0:
            grade = "良好 — 可以考虑"
        elif total >= 4.5:
            grade = "一般 — 需要补强"
        else:
            grade = "较弱 — 建议大幅提升后重新申请"

        report = f"""
        ═══════════════════════════════════
          结构化评分模拟面试 — 综合评价报告
        ═══════════════════════════════════

        面试日期：{datetime.now().strftime('%Y-%m-%d')}
        专业方向：{self.state.major}
        面试风格：结构化评分

        ┌────────────────────┬──────┬──────┬──────────┐
        │ 维度               │ 得分 │ 权重 │ 加权得分 │
        ├────────────────────┼──────┼──────┼──────────┤
        """

        for dim, score in dim_scores.items():
            w = weights[dim]
            weighted = score * w
            report += f"\n        │ {dim:<18} │ {score:.1f} │ {w*100:3.0f}% │ {weighted:.2f}     │"

        report += f"""
        ├────────────────────┼──────┼──────┼──────────┤
        │ 总加权得分         │      │ 100% │ {total:.2f}    │
        └────────────────────┴──────┴──────┴──────────┘

        等级：{grade}

        ── 优势亮点 ──
        1. 能够相对完整地表达自己的经历和想法。
        2. 对专业领域有一定的了解和实践经验。
        3. 沟通态度积极，有一定的自我反思能力。

        ── 待提升领域 ──
        1. 项目描述的颗粒度不够细，需要更多具体的"我做了什么"。
        2. 原理层面的理解可以更深入，建议针对项目用到的核心技术
           做更深入的文献调研。
        3. 英文表达的流利度和专业词汇量需要持续积累。""" + (
            f"\n        4. 专业基础中的弱项：{', '.join(self._basics_weak)}。建议重点复习。" if self._basics_weak else ""
        ) + """

        ── 针对性备考建议 ──
        短期（1周内）：针对简历上每个项目，写出3分钟的"电梯演讲"稿。
        中期（1个月）：系统复习专业核心课程，构建知识图谱。
        长期：坚持每周阅读英文文献并做英文笔记，提升英文能力。

        ═══════════════════════════════════
        """.strip()

        return report

    def _gentle_report(self) -> str:
        strengths = [
            "你有很强的学习热情和好奇心，这对科研来说是最重要的品质。",
            "你在项目中的投入和思考让我看到了你的认真态度。",
            "你对自己的认知比较诚实，知道自己的不足比盲目自信要好得多。",
        ]

        suggestions = [
            "项目经历的表述可以更有条理。建议你试试 STAR 法则（情境-任务-行动-结果）来组织你的项目故事。",
            "原理层面的理解会是你接下来需要深耕的方向。建议找几篇你项目领域的经典论文，仔细读懂方法部分。",
            "英文是一个积累的过程，每天读一点英文文献摘要，坚持一个月就会有明显的进步。",
        ]

        return textwrap.dedent(f"""
        ═══════════════════════════════════
          🌱 温和引导式模拟面试 — 反馈
        ═══════════════════════════════════

        谢谢你今天这么真诚的分享。和你聊天很愉快。

        ✨ 让我印象深刻的地方：
        1. {strengths[0]}
        2. {strengths[1]}
        3. {strengths[2]}

        🌿 你可以做得更好的地方：
        1. {suggestions[0]}
        2. {suggestions[1]}
        3. {suggestions[2]}

        📚 如果你接下来想提升自己，可以看看这些方向：
        · 知识补强：系统复习专业核心课，建立自己的知识体系
        · 技能提升：深入理解项目中用到的技术原理，做到"知其所以然"
        · 表达练习：用 STAR 法则练习讲项目故事，限时2分钟

        真正的面试可能会有各种风格，但请记住：面试官想看到的
        不是完美的你，而是真实的、有潜力的、愿意成长的你。

        你已经迈出了练习的第一步，这本身就值得骄傲。加油！🌟
        ═══════════════════════════════════
        """).strip()


class ClaudeEngine(RuleBasedEngine):
    """
    Claude API 驱动的面试引擎
    使用 Anthropic API 生成动态、智能的追问
    比规则模式更自然、更有针对性
    """

    def __init__(self, style: str, resume: str, materials: list,
                 major: str, api_key: str, model: str = "claude-sonnet-4-6"):
        super().__init__(style, resume, materials, major)
        self.api_key = api_key
        self.model = model

        # 构建系统提示词
        self.system_prompt = self._build_system_prompt()

        # 对话历史
        self._messages = [{"role": "system", "content": self.system_prompt}]

    def _build_system_prompt(self) -> str:
        """从 skill 文件加载系统提示词"""
        # 尝试加载对应的 skill 文件
        skill_map = {
            "stress": "camp-interview-stress.md",
            "structured": "camp-interview-structured.md",
            "gentle": "camp-interview-gentle.md",
        }

        skill_file = skill_map.get(self.style)
        skill_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            ".claude", "commands", skill_file
        )

        if os.path.exists(skill_path):
            with open(skill_path, "r", encoding="utf-8") as f:
                base_prompt = f.read()
        else:
            base_prompt = f"你是一个{self.config['name']}风格的模拟面试官。"

        # 添加候选人的材料信息
        material_context = f"""

        ## 候选人提交的材料

        ### 简历
        {self.state.resume}

        ### 补充材料
        {chr(10).join(self.state.materials) if self.state.materials else '无'}

        ### 专业方向
        {self.state.major}

        ## 当前任务
        你正在进行实时面试对话。请严格按照你的面试风格，根据候选人的材料
        提出个性化的问题和追问。你已经阅读过候选人的简历和材料，所有提问
        都应基于候选人的真实背景。

        请直接输出下一个面试问题或对话内容，不要输出其他内容。
        保持角色一致，不要在问题外附加解释。
        """

        return base_prompt + material_context

    def start(self) -> str:
        """Claude API 模式的开场"""
        self._messages.append({
            "role": "user",
            "content": "面试开始。请先做开场白，让候选人提交材料审核意见并选择专业方向。"
        })
        return self._call_claude()

    def next_question(self) -> Optional[str]:
        """使用 Claude API 生成下一个问题"""
        state = self.state

        if state.finished:
            return None

        if state.dimension_index >= len(state.DIMENSIONS):
            state.finished = True
            return None

        dim = state.DIMENSIONS[state.dimension_index]
        dim_label = state.DIMENSION_LABELS.get(dim, dim)

        # 构建上下文，告诉 Claude 当前处于哪个环节
        context = f"""
        当前面试环节：{dim_label}
        这是该环节的第 {state.question_index + 1} 个问题。
        面试风格：{self.config['name']}

        请根据当前环节，提出下一个面试问题。问题应基于候选人的材料。
        如果该环节已有足够追问，请用 [NEXT_DIMENSION] 标记进入下一环节。
        如果所有环节完成，请用 [FINISH] 标记。
        直接输出问题，不要加前缀说明。
        """

        self._messages.append({"role": "user", "content": context})
        response = self._call_claude()

        # 检查是否进入下一维度或结束
        if "[NEXT_DIMENSION]" in response:
            state.dimension_index += 1
            state.question_index = 0
            self._followup_count = 0
            return self.next_question()

        if "[FINISH]" in response:
            state.finished = True
            return None

        state.question_index += 1
        return response

    def record_answer(self, answer: str):
        """记录回答并加入对话历史"""
        super().record_answer(answer)
        self._messages.append({
            "role": "user",
            "content": f"[候选人回答] {answer}"
        })

    def generate_report(self) -> str:
        """使用 Claude API 生成评估报告"""
        self._messages.append({
            "role": "user",
            "content": "面试结束。请根据你的风格给出最终的评估反馈或报告。"
        })
        report = self._call_claude()
        return report

    def _call_claude(self) -> str:
        """调用 Claude API"""
        try:
            import anthropic

            client = anthropic.Anthropic(api_key=self.api_key)
            response = client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=self.system_prompt,
                messages=[m for m in self._messages if m["role"] != "system"],
            )

            text = response.content[0].text
            self._messages.append({"role": "assistant", "content": text})
            return text

        except ImportError:
            print("\n[错误] 请安装 anthropic SDK: pip install anthropic")
            print("[提示] 回退到规则模式")
            self.state.finished = True
            return "API 调用失败，面试终止。"
        except Exception as e:
            print(f"\n[API 错误] {e}")
            print("[提示] 请检查 ANTHROPIC_API_KEY 是否正确设置")
            self.state.finished = True
            return f"API 调用失败: {e}"
