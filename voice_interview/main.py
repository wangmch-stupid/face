"""
夏令营模拟面试 — 语音对话系统
================================
三种面试风格（压力面 / 结构化评分 / 温和引导式）
× 两种输入模式（文字 / 语音）
× 两种引擎（规则模式 / Claude API 模式）

用法:
    python main.py                          # 交互式选择
    python main.py --style stress           # 直接指定风格
    python main.py --style structured --text-only  # 仅文字模式
    python main.py --style gentle --claude  # 使用 Claude API
"""

import asyncio
import os
import sys
import argparse
from pathlib import Path

# 确保能导入同目录模块
sys.path.insert(0, str(Path(__file__).parent))

from voice_io import speak, speak_en, listen, set_tts_style, check_stt_available, VOICES
from engine import RuleBasedEngine, ClaudeEngine


# ============================================================
# UI 工具函数
# ============================================================

def clear_screen():
    os.system("cls" if sys.platform == "win32" else "clear")


def print_banner():
    print(r"""
  ╔══════════════════════════════════════╗
  ║     🎓 夏令营模拟面试 — 语音对话系统  ║
  ║      压力面 · 结构化 · 温和引导      ║
  ╚══════════════════════════════════════╝
    """)


def print_divider(char="─", width=50):
    print(char * width)


def select_from_list(title: str, options: list, prompts: list = None):
    """让用户从列表中选择"""
    if prompts is None:
        prompts = [f"{i+1}. {o}" for i, o in enumerate(options)]

    print(f"\n{title}")
    for p in prompts:
        print(f"  {p}")
    print()

    while True:
        choice = input("> ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        print(f"  请输入 1-{len(options)}")


def _parse_file_path(raw: str) -> str:
    """清洗用户输入的文件路径"""
    path = raw.strip()
    # 去掉首尾引号（拖拽文件到终端常带引号）
    if (path.startswith('"') and path.endswith('"')) or \
       (path.startswith("'") and path.endswith("'")):
        path = path[1:-1]
    # 展开 ~ 和环境变量
    path = os.path.expandvars(os.path.expanduser(path))
    # 统一分隔符
    path = os.path.normpath(path)
    return path


def _read_pdf_file(path: str) -> str:
    """读取 PDF 文件，提取文本内容"""
    # 方案1: pymupdf (fitz) — 最快最准
    try:
        import fitz
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip() or "[PDF 内容为空]"
    except ImportError:
        pass
    except Exception as e:
        pass  # 尝试下一个方案

    # 方案2: pdfplumber — 准确但慢
    try:
        import pdfplumber
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
        return text.strip() or "[PDF 内容为空]"
    except ImportError:
        pass
    except Exception as e:
        pass

    # 方案3: PyPDF2 — 纯Python，最兼容
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
        return text.strip() or "[PDF 内容为空]"
    except ImportError:
        return "[无法读取 PDF：请安装 pip install PyPDF2]"
    except Exception as e:
        return f"[PDF 读取失败: {e}]"


def _read_file(path: str) -> str:
    """读取任意文件，根据扩展名自动选择读取方式"""
    ext = os.path.splitext(path)[1].lower()

    if ext == '.pdf':
        return _read_pdf_file(path)

    # 文本文件
    text_exts = {'.txt', '.md', '.py', '.json', '.xml', '.csv', '.log',
                 '.java', '.c', '.cpp', '.h', '.js', '.ts', '.html', '.css',
                 '.yaml', '.yml', '.toml', '.cfg', '.ini', '.tex', '.bib',
                 '.doc', '.docx'}
    if ext in {'.doc', '.docx'}:
        return "[Word 文档暂不支持直接读取，请导出为 PDF 或 TXT 后重试]"

    encodings = ['utf-8', 'gbk', 'gb2312', 'gb18030', 'latin-1']
    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
        except Exception as e:
            return f"[读取失败: {e}]"
    return f"[文件编码无法识别: {path}]"


def _read_text_file(path: str) -> str:
    """兼容旧函数名，转发到 _read_file"""
    return _read_file(path)


def collect_materials():
    """收集候选人的简历和材料"""
    print_divider()
    print("📋 第一步：提交材料")
    print()
    print("面试官需要先了解你的背景。请提交你的简历（必需），")
    print("以及其他辅助材料（可选：成绩单、项目报告、论文等）。")
    print()
    print("提交方式：")
    print("  · 直接粘贴文本，输入 END 结束")
    print("  · 或拖拽文件到窗口 / 输入文件路径")
    print("  · 支持 .txt .md .pdf(文本) 等文本文件")
    print("  · 什么都不提交直接回车 = 跳过材料")
    print()

    # 简历
    print("【简历 - 必需】")
    resume_lines = []
    first_line = input("> ").strip()

    if first_line.upper() == "END" or first_line == "":
        resume = "(候选人未提交简历)"
    elif os.path.exists(_parse_file_path(first_line)):
        # 文件路径
        path = _parse_file_path(first_line)
        resume = _read_text_file(path)
        print(f"  [已读取: {os.path.basename(path)}]")
    elif os.path.exists(first_line):
        # 未清洗的路径也试试
        resume = _read_text_file(first_line)
        print(f"  [已读取: {os.path.basename(first_line)}]")
    else:
        # 直接粘贴的文本
        resume_lines.append(first_line)
        print("  (继续粘贴内容，输入 END 结束)")
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            resume_lines.append(line)
        resume = "\n".join(resume_lines)

    print(f"  [简历已收到，{len(resume)} 字]")

    # 补充材料
    print("\n【补充材料 - 可选，直接回车跳过】")
    print("  输入文件路径或粘贴内容，回车跳过")
    materials = []
    while True:
        line = input("> ").strip()
        if line == "":
            break
        if line.upper() == "END":
            break

        cleaned = _parse_file_path(line)
        if os.path.exists(cleaned):
            content = _read_text_file(cleaned)
            if not content.startswith("[无法读取") and not content.startswith("[文件编码"):
                print(f"  [已读取: {os.path.basename(cleaned)}]")
            else:
                print(f"  {content}")
            materials.append(content)
        elif os.path.exists(line):
            content = _read_text_file(line)
            if not content.startswith("[无法读取") and not content.startswith("[文件编码"):
                print(f"  [已读取: {os.path.basename(line)}]")
            else:
                print(f"  {content}")
            materials.append(content)
        else:
            materials.append(line)
            print(f"  [已记录文本，{len(line)} 字]")

    print(f"  [收到 {len(materials)} 份补充材料]")
    return resume, materials


def _select_input_mode() -> bool:
    """选择输入方式：语音 或 文字"""
    print_divider()
    print("🎙️  回答方式")
    print()
    print("  1. 语音回答 — 面试官提问后，你口头回答（需要麦克风）")
    print("  2. 文字回答 — 面试官提问后，你打字回答")
    print()
    while True:
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            print("  ✅ 语音回答模式 — 请确保麦克风可用")
            return True
        elif choice == "2":
            print("  ✅ 文字回答模式")
            return False
        print("  请输入 1 或 2")


def select_major():
    """选择专业方向 — 支持序号或直接输入名称"""
    print_divider()
    print("📚 专业方向")
    print()
    majors = ["计算机", "电子", "机械", "材料", "生物", "化学", "物理", "数学", "经管", "其他"]
    for i, m in enumerate(majors):
        print(f"  {i+1}. {m}")
    print()

    while True:
        choice = input("请输入序号或专业名称: ").strip()
        if not choice:
            continue

        # 数字序号
        if choice.isdigit() and 1 <= int(choice) <= len(majors):
            major = majors[int(choice) - 1]
            if major == "其他":
                major = input("请输入具体专业方向: ").strip() or "其他"
            return major

        # 直接输入名称（模糊匹配）
        for m in majors:
            if m == choice or m in choice or choice in m:
                if m == "其他":
                    major = input("请输入具体专业方向: ").strip() or "其他"
                    return major
                return m

        # 未匹配到，直接使用输入
        print(f"  [未匹配预置专业，将使用自定义方向: {choice}]")
        return choice


def _detect_english(text: str) -> bool:
    """检测文本是否主要为英文（用于 TTS 语言切换）"""
    sample = text[:80].strip()
    if not sample:
        return False
    alpha_chars = sum(1 for c in sample if c.isalpha())
    if alpha_chars == 0:
        return False
    # 检查是否含 CJK 字符（中文、日文、韩文）
    cjk = sum(1 for c in sample if '一' <= c <= '鿿' or
              '぀' <= c <= 'ヿ' or '가' <= c <= '힯')
    if cjk > 0:
        return False
    # ASCII 字母占比 > 60% 且非字母符号不多
    ascii_alpha = sum(1 for c in sample if c.isascii() and c.isalpha())
    return ascii_alpha / alpha_chars > 0.8 and ascii_alpha >= 5


# ============================================================
# 面试主循环
# ============================================================

async def run_interview_loop(engine, voice_io_enabled: bool, tts_enabled: bool):
    """面试主循环 — 提问 → 回答 → 追问 → 推进维度"""

    # 开场白
    opening = engine.start()
    print_divider("═", 50)
    print(f"\n【面试官】\n{opening}\n")

    if tts_enabled:
        await speak(opening)

    # 维度循环
    last_dim = None
    while not engine.is_finished():
        question = engine.next_question()

        if question is None:
            # 面试结束，生成报告
            print_divider("═", 50)
            print("\n⏳ 面试结束，正在生成报告...\n")
            break

        # 检测是否进入新维度
        current_dim_idx = engine.state.dimension_index
        if current_dim_idx < len(engine.state.DIMENSIONS):
            current_dim = engine.state.DIMENSIONS[current_dim_idx]
            if current_dim != last_dim:
                total = len(engine.state.DIMENSIONS)
                dim_num = current_dim_idx + 1
                progress_bar = "█" * dim_num + "░" * (total - dim_num)
                label = engine.state.DIMENSION_LABELS.get(current_dim, current_dim)
                print_divider()
                print(f"  [{dim_num}/{total}] {progress_bar}")
                print(f"  ▶ {label}")
                print_divider()
                last_dim = current_dim

        # 输出问题
        print(f"\n【面试官】\n{question}\n")

        # TTS 朗读
        if tts_enabled:
            try:
                is_english = current_dim in ("self_intro_en", "english") or \
                    _detect_english(question)
                if is_english:
                    await speak_en(question)
                else:
                    await speak(question)
            except Exception as e:
                print(f"  [TTS 播放失败: {e}]")

        # 获取回答
        try:
            if voice_io_enabled:
                attempt_count = 0
                retry = True
                while retry and attempt_count < 2:
                    attempt_count += 1
                    answer = listen(language="zh-CN", timeout=60)
                    if answer:
                        print(f"\n  📝 识别结果: {answer}")
                        retry = False
                    elif attempt_count < 2:
                        print(f"\n  🎤 未识别到语音，再试一次？(第{attempt_count}/2次)")
                        choice = input("  按 Enter 重试语音，输入任意文字后回车 = 打字模式: ").strip()
                        if choice:
                            answer = choice
                            retry = False
                    else:
                        answer = input("\n  ⌨️  语音识别 2 次均失败，请打字回答: ")
                        retry = False
            else:
                answer = input("\n你的回答: ")
        except (EOFError, KeyboardInterrupt):
            print("\n⚠️ 面试被中断。")
            break

        if not answer or not answer.strip():
            answer = "(候选人未作答)"
        elif answer.strip().lower() in ("/quit", "/exit"):
            print("\n  👋 你选择结束面试。正在保存记录...")
            engine.state.finished = True
            break

        # 记录回答
        try:
            engine.record_answer(answer)
        except Exception as e:
            print(f"  [记录出错: {e}]")

    # 输出报告
    report = engine.generate_report()
    print(report)

    if tts_enabled:
        # 只朗读报告的第一段总结
        summary = report.split("\n\n")[0] if report else "面试结束。"
        await speak("面试结束。以下是你的评估报告。")

    # 保存记录
    engine.save_transcript()

    print("\n感谢使用夏令营模拟面试系统！")


# ============================================================
# 入口
# ============================================================

async def main():
    parser = argparse.ArgumentParser(
        description="夏令营模拟面试 — 语音对话系统"
    )
    parser.add_argument(
        "--style", "-s",
        choices=["stress", "structured", "gentle"],
        help="面试风格"
    )
    parser.add_argument(
        "--text-only", "-t",
        action="store_true",
        help="纯文字模式（禁用语音输入和TTS）"
    )
    parser.add_argument(
        "--no-tts",
        action="store_true",
        help="禁用 TTS 语音输出（保留文字）"
    )
    parser.add_argument(
        "--no-stt",
        action="store_true",
        help="禁用语音输入（使用键盘）"
    )
    parser.add_argument(
        "--claude", "-c",
        action="store_true",
        help="使用 Claude API 模式（需设置 ANTHROPIC_API_KEY）"
    )
    parser.add_argument(
        "--tts-voice",
        choices=list(VOICES.keys()),
        default="xiaoxiao",
        help="TTS 声音选择"
    )
    parser.add_argument(
        "--major", "-m",
        type=str,
        default=None,
        help="专业方向（如 计算机/化学/物理），跳过交互选择"
    )
    parser.add_argument(
        "--resume", "-r",
        type=str,
        default=None,
        help="简历文件路径或直接文本"
    )
    parser.add_argument(
        "--skip-setup",
        action="store_true",
        help="跳过所有交互步骤，直接用默认配置开始"
    )
    args = parser.parse_args()

    clear_screen()
    print_banner()

    # Step 1: 选择风格
    if args.style:
        style = args.style
    else:
        styles = ["压力面 — 咄咄逼人，高压追问", "结构化评分 — 专业评估，详细报告", "温和引导式 — 温暖包容，循序渐进"]
        idx = select_from_list("选择面试风格：", styles)
        style = ["stress", "structured", "gentle"][idx]

    style_names = {"stress": "压力面", "structured": "结构化评分", "gentle": "温和引导式"}
    set_tts_style(style)  # 切换 TTS 音色/语速/音高预设
    print(f"\n✅ 面试风格：{style_names[style]}")

    # Step 2: 提交材料（跳过或快速通道）
    if args.skip_setup:
        resume = "(跳过材料提交)"
        materials = []
    elif args.resume:
        # 命令行直接指定简历
        if os.path.exists(_parse_file_path(args.resume)):
            resume = _read_text_file(_parse_file_path(args.resume))
            print(f"\n✅ 简历已读取: {args.resume}")
        else:
            resume = args.resume
            print(f"\n✅ 简历已接收（{len(resume)} 字）")
        materials = []
    else:
        resume, materials = collect_materials()

    # Step 3: 专业方向
    if args.major:
        major = args.major
        print(f"✅ 专业方向：{major}")
    else:
        major = select_major()
        print(f"✅ 专业方向：{major}")

    # Step 3.5: 选择输入方式（语音/文字）
    if args.text_only or args.no_stt:
        stt_enabled = False
    else:
        if check_stt_available():
            stt_enabled = _select_input_mode()
        else:
            print("  ⚠️  语音输入不可用，自动使用文字回答模式。")
            print("  💡 需要语音？确保麦克风已插入并安装: pip install sounddevice SpeechRecognition numpy")
            stt_enabled = False

    # Step 4: 初始化引擎
    claude_mode = args.claude
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if claude_mode and not api_key:
        print("\n⚠️  未检测到 ANTHROPIC_API_KEY 环境变量")
        print("   回退到规则模式。设置 API key: set ANTHROPIC_API_KEY=your_key")
        claude_mode = False

    if claude_mode:
        print("\n🤖 使用 Claude API 驱动模式（智能追问）")
        engine = ClaudeEngine(style, resume, materials, major, api_key)
    else:
        print("\n📋 使用规则驱动模式")
        engine = RuleBasedEngine(style, resume, materials, major)

    # Step 5: 确定 I/O 模式（TTS 输出 + STT 输入已在上面选择）
    tts_enabled = not args.text_only and not args.no_tts

    if tts_enabled and stt_enabled:
        print("🔊🎤 全语音模式 — 面试官说话，你口头回答")
    elif tts_enabled:
        print("🔊⌨️  TTS 语音提问 + 键盘打字回答")
    elif stt_enabled:
        print("📝🎤 文字提问 + 语音回答")
    else:
        print("📝⌨️  纯文字模式")

    # 等待用户准备
    print("\n" + "=" * 50)
    input("按回车键开始面试..." if style != "stress" else "准备好了就按回车，别磨蹭...")
    clear_screen()

    # Step 6: 运行面试
    try:
        await run_interview_loop(engine, stt_enabled, tts_enabled)
    except Exception as e:
        print(f"\n{'='*50}")
        print(f"⚠️  面试过程中出现异常：{e}")
        print(f"{'='*50}")
        import traceback
        traceback.print_exc()
        print("\n按回车键退出...")
        input()


if __name__ == "__main__":
    asyncio.run(main())
