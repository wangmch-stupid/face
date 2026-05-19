"""
夏令营模拟面试 — 三种风格的完整配置
问题库和流程定义，驱动规则引擎
"""

# ============================================================
# 专业方向 → 基础知识点映射
# ============================================================
MAJOR_BASICS = {
    "计算机": {
        "q1": ("数据结构与算法", "请解释栈（Stack）和队列（Queue）的区别，各举一个应用场景。"),
        "q2": ("操作系统", "进程和线程的区别是什么？"),
        "q3": ("计算机网络", "TCP 和 UDP 的核心区别是什么？什么场景用哪个？"),
        "q4": ("数据库", "解释一下索引的原理，为什么索引能加速查询？"),
        "q5": ("计算机组成", "请解释 CPU 缓存（Cache）的局部性原理。"),
        "q6": ("综合", "从你在浏览器输入一个 URL 到页面显示，经历了哪些步骤？尽量详细。"),
    },
    "电子": {
        "q1": ("电路分析", "请解释基尔霍夫电压定律和电流定律。"),
        "q2": ("模拟电子", "解释运算放大器的虚短和虚断概念。"),
        "q3": ("数字电路", "组合逻辑电路和时序逻辑电路的区别是什么？"),
        "q4": ("信号处理", "时域分析和频域分析的区别？傅里叶变换的作用是什么？"),
        "q5": ("电磁场", "解释麦克斯韦方程组的物理意义。"),
        "q6": ("综合", "设计一个简单的模数转换系统（ADC），需要考虑哪些因素？"),
    },
    "机械": {
        "q1": ("材料力学", "解释应力和应变的概念，以及弹性模量的物理意义。"),
        "q2": ("机械原理", "四杆机构有哪几种基本类型？各自的运动特性？"),
        "q3": ("机械设计", "齿轮传动设计中，模数和压力角的作用是什么？"),
        "q4": ("热力学", "热力学第一定律和第二定律分别是什么？"),
        "q5": ("流体力学", "解释雷诺数的物理意义及其在流态判断中的应用。"),
        "q6": ("综合", "设计一个减速器需要考虑哪些关键因素？"),
    },
    "材料": {
        "q1": ("材料科学基础", "解释晶体和非晶体的区别。"),
        "q2": ("相图", "解释二元相图中的杠杆定律。"),
        "q3": ("力学性能", "硬度、强度、韧性的区别与联系？"),
        "q4": ("热处理", "退火、正火、淬火、回火的区别和目的？"),
        "q5": ("功能材料", "半导体材料和导体材料的能带结构有什么区别？"),
        "q6": ("综合", "如果要设计一种轻质高强度合金，你会从哪些方面考虑？"),
    },
    "生物": {
        "q1": ("生物化学", "解释酶催化的基本原理和米氏方程。"),
        "q2": ("分子生物学", "DNA 复制和转录的区别是什么？"),
        "q3": ("细胞生物学", "细胞膜的结构模型和主要功能。"),
        "q4": ("遗传学", "解释孟德尔遗传定律及其分子基础。"),
        "q5": ("微生物学", "革兰氏阳性菌和阴性菌细胞壁结构的区别。"),
        "q6": ("综合", "CRISPR-Cas9 基因编辑的原理是什么？有哪些应用和局限？"),
    },
    "化学": {
        "q1": ("有机化学", "解释亲核取代反应 SN1 和 SN2 机理的区别。"),
        "q2": ("物理化学", "解释热力学中的吉布斯自由能及其判据。"),
        "q3": ("分析化学", "色谱法的基本原理是什么？有哪些类型？"),
        "q4": ("无机化学", "配位化合物的晶体场理论基本要点。"),
        "q5": ("高分子", "解释聚合反应的逐步聚合和连锁聚合的区别。"),
        "q6": ("综合", "如何设计一个催化剂的表征实验方案？"),
    },
    "物理": {
        "q1": ("经典力学", "解释拉格朗日力学和牛顿力学的区别。"),
        "q2": ("电磁学", "麦克斯韦方程组四个方程的物理意义。"),
        "q3": ("量子力学", "解释波函数和薛定谔方程的基本概念。"),
        "q4": ("热力学统计", "解释熵的统计意义。"),
        "q5": ("固体物理", "能带理论的基本概念和导体/半导体/绝缘体的区别。"),
        "q6": ("综合", "什么是量子纠缠？它在量子信息中有哪些应用？"),
    },
    "数学": {
        "q1": ("数学分析", "解释一致连续和逐点连续的区别。"),
        "q2": ("线性代数", "特征值和特征向量的几何意义是什么？"),
        "q3": ("概率论", "大数定律和中心极限定理的区别与应用。"),
        "q4": ("抽象代数", "群、环、域的区别与联系。"),
        "q5": ("拓扑学", "解释紧致性和连通性的概念。"),
        "q6": ("综合", "什么是傅里叶变换？它在数学和应用中的意义？"),
    },
    "经管": {
        "q1": ("微观经济学", "解释供需曲线和市场均衡。"),
        "q2": ("宏观经济学", "GDP 的三种核算方法分别是什么？"),
        "q3": ("计量经济学", "解释OLS回归的基本假设和BLUE性质。"),
        "q4": ("管理学", "解释波特五力模型及其应用。"),
        "q5": ("金融学", "解释CAPM模型和无套利定价原理。"),
        "q6": ("综合", "如何评估一个企业的投资价值？请给出分析框架。"),
    },
}

# ============================================================
# 开放性问题（专业核心知识）— 按专业方向
# ============================================================
MAJOR_OPEN_QUESTIONS = {
    "计算机": "假设你要设计一个支持百万级并发的实时推荐系统，延迟要求 50ms 以内。请从系统架构、算法选择、数据存储三个层面谈谈你的设计思路。",
    "电子": "设计一个便携式心电监测设备，需要考虑信号采集、滤波、放大、AD转换和无线传输。谈谈你的整体设计方案和每个环节的关键考量。",
    "机械": "设计一款面向城市短途出行的轻量化折叠电动车。请从结构设计、材料选择、动力系统、人机工程等方面谈谈思路。",
    "材料": "如果让你开发一种新型固态电解质用于锂金属电池，你会从哪些材料体系入手？为什么？需要解决哪些关键科学问题？",
    "生物": "如何利用合成生物学的方法构建一个能高效降解塑料的工程菌株？请从底盘选择、酶设计、代谢通路优化等方面讨论。",
    "化学": "设计一种新型光催化剂用于水分解制氢，你会从哪些方面优化其性能？谈谈材料选择、能带调控和助催化剂负载策略。",
    "物理": "假设你要设计一个量子计算实验来演示量子优越性，你会选择什么物理体系？需要解决哪些实验挑战？",
    "数学": "请解释深度学习中的梯度消失问题，从数学角度分析其成因，并讨论各种解决方案的数学原理。",
    "经管": "当前中国面临人口老龄化的挑战，请从经济学的角度分析其对劳动力市场、社会保障体系和经济增长的影响，并提出你的政策建议。",
}

# ============================================================
# 英文文献摘要（按专业方向）
# ============================================================
MAJOR_PAPER_ABSTRACTS = {
    "计算机": """Deep learning has revolutionized the field of artificial intelligence, enabling remarkable advances in computer vision, natural language processing, and reinforcement learning. However, the success of deep neural networks often comes at the cost of massive computational resources and large-scale labeled datasets. In this paper, we propose a novel self-supervised learning framework that leverages unlabeled data to pretrain representations, significantly reducing the need for manual annotations. Our approach achieves state-of-the-art performance on multiple benchmarks while using only 10% of the labeled data required by supervised methods. We further demonstrate that the learned representations transfer effectively across different domains and tasks, suggesting that self-supervised learning may be a key step toward more data-efficient and generalizable artificial intelligence systems.""",

    "电子": """Wide-bandgap semiconductors, particularly gallium nitride (GaN) and silicon carbide (SiC), have emerged as promising materials for next-generation power electronics. Their superior material properties, including high breakdown electric field, high electron mobility, and excellent thermal conductivity, enable power devices with higher efficiency, higher switching frequency, and higher operating temperature compared to conventional silicon-based devices. This paper reviews recent advances in GaN and SiC power device technologies, focusing on device design, fabrication processes, and reliability challenges. We discuss the trade-offs between different device architectures and highlight key application areas including electric vehicles, renewable energy systems, and data center power supplies.""",

    "机械": """Additive manufacturing, commonly known as 3D printing, has transformed from a prototyping tool into a viable production technology for end-use parts. This paper presents a comprehensive investigation of the mechanical properties of Ti-6Al-4V alloy components fabricated by selective laser melting. We systematically characterize the effects of process parameters—including laser power, scan speed, and hatch spacing—on the microstructure, porosity, and resulting mechanical performance. Our results reveal that optimizing the energy density input can achieve tensile strengths comparable to wrought material, while the fatigue performance remains limited by process-induced defects. We propose a post-processing heat treatment protocol that significantly improves fatigue life while maintaining high static strength.""",

    "材料": """Perovskite solar cells have achieved power conversion efficiencies exceeding 25% in just over a decade of research, making them the fastest-advancing solar technology to date. The remarkable performance stems from the unique optoelectronic properties of metal halide perovskites, including high absorption coefficients, long carrier diffusion lengths, and tunable bandgaps. However, the long-term stability of perovskite solar cells under operational conditions remains the primary obstacle to commercialization. This review examines the fundamental degradation mechanisms—including moisture sensitivity, thermal instability, and ion migration—and critically evaluates recent strategies to enhance device stability through composition engineering, interface passivation, and encapsulation technologies.""",

    "生物": """The gut microbiome, comprising trillions of microorganisms inhabiting the human gastrointestinal tract, plays a fundamental role in host physiology, metabolism, and immunity. Recent advances in metagenomic sequencing and metabolomic profiling have revealed intricate connections between gut microbial dysbiosis and various diseases, including inflammatory bowel disease, obesity, type 2 diabetes, and even neurological disorders. This paper presents a large-scale multi-omics study integrating shotgun metagenomics, untargeted metabolomics, and host clinical parameters from a cohort of 1,200 individuals. We identify specific microbial species and metabolic pathways that are significantly associated with disease states and validate key findings in an independent replication cohort. Our results highlight the potential of microbiome-based biomarkers for early disease diagnosis and personalized therapeutic interventions.""",

    "化学": """Single-atom catalysts (SACs), featuring isolated metal atoms dispersed on solid supports, represent a new frontier in heterogeneous catalysis. Unlike conventional nanoparticle catalysts, SACs offer maximum atom efficiency, unique electronic structures, and well-defined active sites that bridge the gap between homogeneous and heterogeneous catalysis. This paper reports a general synthesis strategy for preparing a library of single-atom catalysts with different transition metals on nitrogen-doped carbon supports. Through a combination of advanced characterization techniques including aberration-corrected STEM, X-ray absorption spectroscopy, and DFT calculations, we elucidate the coordination environment and electronic structure of the active sites. The catalysts exhibit exceptional activity and selectivity for electrochemical CO2 reduction, with the Fe-N4 site showing nearly 100% CO Faradaic efficiency at low overpotentials.""",

    "物理": """Topological insulators represent a novel quantum state of matter characterized by an insulating bulk and conducting surface states protected by time-reversal symmetry. These topological surface states exhibit remarkable properties including spin-momentum locking and immunity to backscattering from non-magnetic impurities, making them promising platforms for spintronics and topological quantum computation. In this work, we use angle-resolved photoemission spectroscopy and scanning tunneling microscopy to investigate the electronic structure of the intrinsic topological insulator Bi2Se3. We observe clear evidence for the topological surface states and measure their dispersion relation with high precision. Furthermore, we demonstrate that the surface states remain robust against moderate levels of non-magnetic disorder, confirming their topological protection.""",

    "数学": """The theory of optimal transport, originating from the work of Monge and Kantorovich, has found profound applications across multiple disciplines including machine learning, image processing, and statistical inference. This paper addresses the computational challenges associated with large-scale optimal transport problems. We propose a novel entropic regularization scheme combined with a multiscale approach that achieves near-linear time complexity while maintaining rigorous approximation guarantees. The algorithm leverages the Sinkhorn iterations within a coarse-to-fine framework, adaptively refining the transport plan. We prove convergence rates and demonstrate the practical effectiveness of our method on real-world datasets, including single-cell RNA sequencing data and 3D shape matching problems.""",

    "经管": """The rise of digital platforms has fundamentally reshaped market structures and competitive dynamics across industries. Platform businesses benefit from strong network effects, where the value of the platform increases with the number of users on each side of the market. This paper develops a theoretical model to analyze the pricing strategies and welfare implications of two-sided platforms in the presence of both same-side and cross-side network effects. We show that the optimal pricing structure depends critically on the relative magnitude and direction of these network effects. Under certain conditions, platforms may find it optimal to subsidize one side of the market while extracting surplus from the other. We extend the model to consider platform competition, multi-homing behavior, and the implications for antitrust policy.""",
}

# ============================================================
# 综合素质问题库（所有风格共用）
# ============================================================
QUALITY_QUESTIONS = [
    "你经历过最大的一次失败是什么？怎么走出来的？",
    "你和导师或队友发生过最严重的一次冲突是什么？怎么处理的？",
    "你认为自己最大的缺点是什么？你为此做了什么努力？",
    "你为什么选择读研？你未来的学术或职业规划是什么？",
    "如果这次夏令营没有录取你，你觉得原因会是什么？",
    "你认为做科研最重要的品质是什么？你具备吗？举例说明。",
    "描述一个你主动走出舒适区的经历。",
    "你有没有什么想问我的？",
]

# ============================================================
# 各风格的过渡语和特色话术
# ============================================================
STYLE_CONFIG = {
    "stress": {
        "name": "压力面",
        "opening": "简历我扫了一眼，说实话没看出什么特别的。今天七个环节，每个限时。我问你答，别绕弯子，别背稿子，别浪费我时间。准备好了就开始。",
        "transitions": {
            "self_intro_cn": "给你90秒用中文介绍自己。计时。开始。",
            "self_intro_en": "Now introduce yourself in English. 90 seconds. Go.",
            "project": "挑一个你最拿得出手的项目。2分钟。讲。",
            "principle": "你刚才提的技术，底层原理是什么？不要背书，用你自己的理解。往深了说。",
            "basics": "下面考你基础概念。我看看你本科到底有没有在学。",
            "core_knowledge": "给你一个实际场景。让我看看你是真有料还是只会背书。",
            "english": "一段文献，60秒浏览，逐句翻译。开始。",
            "quality": "最后几个问题。希望你坦诚。别说套话。",
        },
        "fast_followups": [
            "就这？还有呢？",
            "太浅了。往深了挖。",
            "你确定？我给你一次重新回答的机会。",
            "不满意。换个思路。",
            "这不是我想听的。再说。",
            "你在逃避问题。直接回答。",
        ],
        "closing": "面试结束。坦率讲你今天问题不少。{feedback}。这是模拟，真实面试可能比这残酷得多。回去好好准备。",
    },
    "structured": {
        "name": "结构化评分",
        "opening": "欢迎参加今天的夏令营模拟面试。我是你今天的面试官。今天的面试将按照七个维度进行结构化评估，大约30分钟。每个环节结束后我会给出分数和简短反馈，最后提供完整的评估报告。准备好了吗？",
        "transitions": {
            "self_intro_cn": "首先请你用中文做一下自我介绍，2分钟左右。请重点突出你的学术背景和研究兴趣。",
            "self_intro_en": "接下来请你用英文做一下自我介绍。Please introduce yourself in English, about 2 minutes.",
            "project": "请详细介绍一个你最有代表性的项目，包括背景、你的角色、技术方案和成果。",
            "principle": "请深入解释你项目中核心技术或方法的底层原理。",
            "basics": "接下来我会考察你的专业基础知识。一共6道题，难度递进。准备好了吗？",
            "core_knowledge": "下面是一个开放性的专业问题，没有标准答案，我想听听你的分析思路。",
            "english": "请翻译以下这段英文文献摘要。先浏览60秒，然后逐句翻译成中文。",
            "quality": "最后我想了解一些你的个人特质和综合素质。",
        },
        "scoring_prompts": {
            "self_intro_cn": "中文自我介绍：{score}/10",
            "self_intro_en": "英文自我介绍：{score}/10",
            "project": "项目经历 — 深度：{score}/10",
            "principle": "项目原理 — 理解度：{score}/10",
            "basics": "专业基础 — 答对{correct}/{total}题：{score}/10",
            "core_knowledge": "专业核心知识 — 分析深度：{score}/10",
            "english": "英文文献翻译 — 准确度：{score}/10",
            "quality": "综合素质 — 整体评价：{score}/10",
        },
        "closing": "面试到此结束。下面我为你出具一份完整的评估报告。\n\n{report}",
    },
    "gentle": {
        "name": "温和引导式",
        "opening": "你好！欢迎来参加今天的模拟面试。放轻松，这就是一次聊天，没有对错，没有评判。我就是想通过对话多了解你一些。大概会聊半个小时，过程中你随时可以让我重复问题，或者给你一点时间思考，没关系的。准备好了我们就开始？",
        "transitions": {
            "self_intro_cn": "首先请你用中文介绍一下自己。不用紧张，就像跟朋友介绍自己一样自然就好。可以聊聊你的背景、兴趣，以及为什么想来这个夏令营。慢慢来，不赶时间。",
            "self_intro_en": "接下来我们用英文简单聊几句。不用追求完美，大胆说就行，就当练习。Could you tell me a bit about yourself in English?",
            "project": "我看到你在材料里提到了几个很有意思的项目。能挑一个你觉得最有意思的，跟我聊聊吗？就像讲故事一样，说说你是怎么参与进去的，做了什么，有什么收获。",
            "principle": "你刚才提到的技术很有意思。我其实也挺好奇的——它是怎么工作的呢？能不能用你理解的方式给我讲讲，就当我是外行。能把复杂的东西讲简单，才是真懂了。",
            "basics": "接下来我想和你一起过几个专业基础概念。从简单的开始，会就答，不会就说不会，我们一起看看哪些地方还可以加强。",
            "core_knowledge": "接下来我想跟你聊一个开放性的问题。没有唯一正确的答案，我感兴趣的是你思考的过程。你可以边想边说，也可以稍微整理一下再回答。",
            "english": "我们来试一小段英文文献的翻译。不用追求完美，大意准确就行。生词可以猜，或者根据上下文推断。",
            "quality": "技术方面的我们都聊完了。最后这段时间我想了解一下你这个人——你的故事、你的想法、你对未来的期待。就是朋友间的聊天。",
        },
        "encouragements": [
            "没关系，你已经说得很好了。",
            "这个确实不容易，很多人都会卡在这里。",
            "方向是对的，再往深想一点就好了。",
            "没关系，这个知识点回去看看就好。",
            "你说得很好，让我对你有了更深的理解。",
        ],
        "closing": "谢谢你今天这么真诚的分享。和你聊天很愉快，我觉得你是一个很有潜力的同学。\n\n{feedback}\n\n真正的面试可能会有各种风格，但请记住：面试官想看到的不是完美的你，而是真实的你。加油！",
    },
}
