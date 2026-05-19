"""
夏令营模拟面试 — 全9学科深度题库
每学科12道题，覆盖各子领域核心知识点
基于各大高校保研夏令营面试真题整理
"""

MAJOR_BASICS = {
    "计算机": {
        "q1": ("数据结构", "数组和链表的区别是什么？各自优缺点和适用场景？"),
        "q2": ("算法", "快速排序的思想？最好/最坏时间复杂度？什么情况下退化为O(n²)？"),
        "q3": ("数据结构", "哈希表原理是什么？哈希冲突的解决方式有哪些？"),
        "q4": ("算法", "DFS和BFS的区别？各用什么数据结构实现？分别适用于什么场景？"),
        "q5": ("操作系统", "进程和线程的区别是什么？进程间通信方式有哪些？"),
        "q6": ("操作系统", "死锁的四个必要条件是什么？如何预防和避免？"),
        "q7": ("操作系统", "虚拟内存的原理？页面置换算法有哪些（FIFO/LRU/CLOCK）？"),
        "q8": ("计算机网络", "TCP和UDP的核心区别？TCP如何保证可靠传输？"),
        "q9": ("计算机网络", "TCP三次握手和四次挥手的过程？为什么是三次和四次？"),
        "q10": ("计算机网络", "从浏览器输入URL到页面显示，经历了哪些步骤？"),
        "q11": ("计算机组成", "CPU缓存(Cache)的局部性原理是什么？时间局部性和空间局部性的区别？"),
        "q12": ("数据库", "数据库索引的底层数据结构是什么？为什么用B+树而不是二叉搜索树？"),
    },
    "电子": {
        "q1": ("电路分析", "基尔霍夫电压定律和电流定律的内容是什么？"),
        "q2": ("模拟电子", "运算放大器的虚短和虚断是什么？在什么条件下成立？"),
        "q3": ("模拟电子", "负反馈有哪四种组态？各有什么特点？"),
        "q4": ("数字电路", "组合逻辑电路和时序逻辑电路的区别？触发器的种类有哪些？"),
        "q5": ("数字电路", "Mealy型和Moore型状态机的区别？建立时间和保持时间是什么？"),
        "q6": ("信号处理", "傅里叶变换、拉普拉斯变换、Z变换的异同和适用范围？"),
        "q7": ("信号处理", "奈奎斯特采样定理的内容？不满足时会发生什么？FIR和IIR滤波器区别？"),
        "q8": ("通信原理", "香农公式及其物理意义？信道编码和信源编码的区别？"),
        "q9": ("通信原理", "OFDM中正交的含义是什么？多径效应如何影响通信？如何消除码间串扰？"),
        "q10": ("电磁场", "麦克斯韦方程组的四个方程分别对应什么物理定律？"),
        "q11": ("电磁场", "什么是趋肤效应？矩形波导的主模是什么？单模传输条件？"),
        "q12": ("综合", "设计一个便携式心电监测设备，从信号采集到无线传输的全链路方案？"),
    },
    "机械": {
        "q1": ("材料力学", "应力-应变曲线的四个阶段？屈服强度和抗拉强度的工程意义？"),
        "q2": ("材料力学", "梁弯曲正应力的分布规律？提高疲劳强度的措施有哪些？"),
        "q3": ("理论力学", "压杆稳定性是什么？如何提高压杆的临界载荷？"),
        "q4": ("机械原理", "铰链四杆机构有哪几种基本类型？曲柄存在的条件是什么？"),
        "q5": ("机械设计", "齿轮传动的失效形式有哪些？闭式软齿面和硬齿面的设计准则有何不同？"),
        "q6": ("机械设计", "轴的设计步骤？弯扭合成强度校核用什么强度理论？滚动轴承与滑动轴承区别？"),
        "q7": ("制造工艺", "退火、正火、淬火、回火的区别和目的？调质是什么？"),
        "q8": ("制造工艺", "传统加工（车铣刨磨）与增材制造（3D打印）的核心差异？薄壁零件如何控制变形？"),
        "q9": ("热力学", "热力学第一定律和第二定律分别是什么？卡诺循环的效率？"),
        "q10": ("流体力学", "雷诺数的物理意义？层流和湍流的判断标准？"),
        "q11": ("材料", "45号钢的含碳量是多少？铁碳相图中钢和铸铁的分界点是什么？"),
        "q12": ("综合", "设计一款轻量化折叠电动车，从结构、材料、动力三方面谈思路？"),
    },
    "材料": {
        "q1": ("晶体结构", "FCC、BCC、HCP三种晶体结构的配位数、致密度和滑移系数？典型金属各举一例？"),
        "q2": ("晶体缺陷", "刃型位错和螺型位错的核心区别？位错线与柏氏矢量的关系？"),
        "q3": ("晶体缺陷", "肖特基缺陷和弗伦克尔缺陷的区别？点缺陷有哪几种？"),
        "q4": ("相图", "铁碳相图中钢和铸铁的分界点是多少？共析成分是多少？室温组织分别是什么？"),
        "q5": ("相图", "二元相图中的杠杆定律是什么？T8钢为什么比40钢强度硬度高？"),
        "q6": ("强化机制", "四种强化方式（细晶强化、固溶强化、加工硬化、第二相强化）各自的原理和特点？"),
        "q7": ("热处理", "退火、正火、淬火、回火的目的和组织变化？淬火后为什么要回火？"),
        "q8": ("热处理", "渗碳的原理？渗碳后为什么还要淬火？冷变形金属加热时经历哪三个阶段？"),
        "q9": ("功能材料", "P型半导体和N型半导体的区别？P-N结的原理和应用？"),
        "q10": ("功能材料", "为什么陶瓷的导热率远低于金属？溶胶-凝胶法与水热法的区别？"),
        "q11": ("力学性能", "强度、硬度、韧性、疲劳强度的定义与区别？如何通过拉伸曲线获取？"),
        "q12": ("综合", "设计一种新型固态电解质用于锂金属电池，从材料体系到关键科学问题谈思路？"),
    },
    "生物": {
        "q1": ("生物化学", "酶催化的基本原理？米氏方程的内容和Km值的意义？"),
        "q2": ("分子生物学", "DNA复制的过程和保真性机制？原核与真核DNA复制的区别？"),
        "q3": ("分子生物学", "PCR的原理？引物设计的关键要素？qPCR与普通PCR的核心差异？"),
        "q4": ("分子生物学", "CRISPR-Cas9基因编辑的原理？sgRNA和PAM序列的作用？脱靶效应如何解决？"),
        "q5": ("细胞生物学", "细胞凋亡与坏死的区别？Caspase家族在凋亡中的作用？"),
        "q6": ("细胞生物学", "细胞周期各阶段的调控机制？CDK/Cyclin复合物的作用？"),
        "q7": ("细胞生物学", "细胞膜的流动镶嵌模型？主动运输和被动运输的差异？Na⁺-K⁺泵机制？"),
        "q8": ("遗传学", "孟德尔分离定律和自由组合定律的内容？不完全显性和共显性的区别？"),
        "q9": ("遗传学", "表观遗传学的概念？DNA甲基化和组蛋白修饰如何调控基因表达？"),
        "q10": ("微生物学", "革兰氏阳性菌和阴性菌细胞壁结构的区别？抗生素耐药的主要机制有哪些？"),
        "q11": ("微生物学", "病毒的结构和复制周期？灭活疫苗和mRNA疫苗的原理差异？"),
        "q12": ("综合", "如何利用合成生物学构建一个能高效降解塑料的工程菌株？从底盘选择到代谢通路优化？"),
    },
    "化学": {
        "q1": ("有机化学", "SN1和SN2反应机理的核心区别？什么情况下以取代为主、什么情况下以消除为主？"),
        "q2": ("有机化学", "Diels-Alder反应是什么？Wittig反应的机理和应用？"),
        "q3": ("有机化学", "亲核试剂和亲电试剂的定义？溶剂极性对SN1和SN2反应速率的影响？"),
        "q4": ("无机化学", "配位化合物的晶体场理论基本要点？高自旋和低自旋的形成条件？"),
        "q5": ("无机化学", "镧系收缩的原因和影响？物质为什么有颜色（d-d跃迁、电荷迁移）？"),
        "q6": ("物理化学", "热力学第一和第二定律的内容？吉布斯自由能的定义及其判据？"),
        "q7": ("物理化学", "化学吸附和物理吸附的区别？朗格缪尔吸附等温式的假设？"),
        "q8": ("物理化学", "什么是活化能和表观活化能？阿伦尼乌斯公式？催化剂如何改变反应路径？"),
        "q9": ("分析化学", "色谱法的基本原理？气相色谱和液相色谱的适用场景差异？"),
        "q10": ("分析化学", "准确度和精密度的区别？EDTA配位滴定中为什么要控制pH？"),
        "q11": ("高分子", "逐步聚合和连锁聚合的区别？聚乙烯的三种聚合方式（高压/低压/茂金属）？"),
        "q12": ("综合", "设计一种新型光催化剂用于水分解制氢，从能带调控到助催化剂负载谈策略？"),
    },
    "物理": {
        "q1": ("量子力学", "量子力学的基本假设有哪些？波函数的统计解释是什么？"),
        "q2": ("量子力学", "什么是不确定关系？什么是量子隧穿效应？什么是全同性原理？"),
        "q3": ("量子力学", "定态微扰论的基本思想？简并和非简并微扰的区别？"),
        "q4": ("热力学统计", "热力学四大定律分别是什么？熵的统计意义？玻尔兹曼关系？"),
        "q5": ("热力学统计", "玻尔兹曼系统、玻色系统、费米系统的区别？什么是费米子、玻色子？"),
        "q6": ("电磁学", "麦克斯韦方程组四个方程的物理意义？位移电流由谁引入、实质是什么？"),
        "q7": ("电磁学", "静电屏蔽的原理？顺磁质、抗磁质、铁磁质的区别？什么是居里点？"),
        "q8": ("固体物理", "能带论如何解释导体、半导体、绝缘体？布洛赫定理的内容？"),
        "q9": ("固体物理", "什么是声子？为什么说声子是准粒子？德拜温度的意义？"),
        "q10": ("理论力学", "虚功原理和达朗贝尔原理的内容？哈密顿原理与牛顿力学的区别？"),
        "q11": ("前沿", "什么是拓扑绝缘体？什么是超导现象和迈斯纳效应？BCS理论的核心思想？"),
        "q12": ("综合", "如果要设计一个量子计算实验演示量子优越性，你会选什么物理体系？核心挑战？"),
    },
    "数学": {
        "q1": ("数学分析", "用ε-δ语言叙述函数极限的定义？一致连续和逐点连续的区别？"),
        "q2": ("数学分析", "罗尔定理、拉格朗日中值定理、柯西中值定理的内容和关系？"),
        "q3": ("数学分析", "函数项级数的一致收敛性？黎曼可积的充要条件是什么？"),
        "q4": ("高等代数", "矩阵的秩的三种等价定义？特征值和特征向量的定义及求法？"),
        "q5": ("高等代数", "相似矩阵的性质？矩阵可对角化的充要条件？若尔当标准形？"),
        "q6": ("高等代数", "正定矩阵的定义和判别方法？二次型化为标准形的方法？"),
        "q7": ("概率论", "大数定律和中心极限定理的区别与应用？切比雪夫不等式的意义？"),
        "q8": ("概率论", "极大似然估计的思想？与矩估计的差异？假设检验的基本逻辑？"),
        "q9": ("抽象代数", "群、环、域的定义和区别？陪集、正规子群、商群的概念？"),
        "q10": ("拓扑学", "紧致性和连通性的定义？Hausdorff空间是什么？同胚的定义？"),
        "q11": ("实变函数", "勒贝格积分与黎曼积分的核心区别？可测函数和可测集的定义？"),
        "q12": ("综合/应用", "傅里叶变换在数学和应用中的意义？深度学习中的梯度消失问题从数学角度如何分析？"),
    },
    "经管": {
        "q1": ("微观经济", "供给需求曲线和市场均衡？价格弹性的概念和影响因素？"),
        "q2": ("微观经济", "完全竞争市场的均衡条件（P=MC）？垄断市场为什么造成社会福利损失？"),
        "q3": ("微观经济", "纳什均衡的定义？囚徒困境和智猪博弈的均衡解？"),
        "q4": ("微观经济", "外部性的概念？正外部性和负外部性各举一例？科斯定理的内容？"),
        "q5": ("宏观经济", "GDP的三种核算方法？名义GDP和实际GDP的区别？GDP的局限性？"),
        "q6": ("宏观经济", "通货膨胀的成因和影响？菲利普斯曲线描述的关系？"),
        "q7": ("宏观经济", "货币政策的三大工具？财政政策中自动稳定器和相机抉择的区别？"),
        "q8": ("金融学", "CAPM资本资产定价模型的核心公式？贝塔系数的含义？有效市场假说的三个层次？"),
        "q9": ("金融学", "投资组合理论的核心思想？为什么分散化投资能降低风险？期权定价模型的直觉解释？"),
        "q10": ("计量经济", "OLS回归的基本假设？BLUE性质是什么？异方差和自相关的后果？"),
        "q11": ("管理学", "波特五力模型的内容？SWOT分析的应用？"),
        "q12": ("综合", "当前中国面临人口老龄化的挑战，从经济学角度分析其对劳动力市场、社会保障和增长的影响？"),
    },
}

# 专业核心知识 — 开放性综合题（各学科前沿/设计类）
MAJOR_OPEN_QUESTIONS = {
    "计算机": "假设你要设计一个支持千万级DAU的实时推荐系统，延迟要求50ms以内。请从系统架构（缓存/CDN/微服务）、算法选择（协同过滤/深度学习）、数据存储（SQL/NoSQL/向量数据库）三个层面谈谈你的设计思路和可能的瓶颈。",
    "电子": "设计一个低功耗便携式心电监测设备，需要从信号采集（电极/仪表放大器）、滤波（高通/低通/陷波50Hz）、ADC转换（精度/采样率）、无线传输（BLE/WiFi选择）等环节出发，谈谈整体方案和每个环节的关键参数选择。",
    "机械": "设计一款面向城市短途出行的轻量化折叠电动车。请从结构设计（折叠机构/悬架）、材料选择（铝合金/碳纤维/镁合金的取舍）、动力系统（电机类型/电池/传动方式）、人机工程（骑行姿势/操控布局）等方面详细说明设计思路和关键计算。",
    "材料": "如果让你开发一种新型固态电解质用于锂金属电池，你会从哪些材料体系入手（氧化物/硫化物/聚合物）？为什么？需要解决哪些关键科学问题（离子电导率/界面稳定性/机械强度）？用什么实验手段来表征性能？",
    "生物": "如何利用合成生物学方法构建一个能高效降解PET塑料的工程菌株？请从底盘细胞选择（大肠杆菌/酵母/枯草芽孢杆菌）、关键酶设计与定向进化、代谢通路优化、以及工业化发酵条件等方面详细讨论。",
    "化学": "设计一种新型非贵金属单原子催化剂用于电催化CO2还原。请从载体选择（氮掺杂碳/金属氧化物）、金属中心选择（Fe/Co/Ni）、合成策略、以及如何通过 XAFS/STEM/DFT等表征分析活性位点配位环境和反应机理等方面展开。",
    "物理": "假设你要设计一个基于超导量子比特的量子计算实验来演示量子优越性，你会选择什么物理体系（Transmon/Fluxonium/拓扑量子比特）？需要解决哪些实验挑战（相干时间/门保真度/读出/可扩展性）？",
    "数学": "请解释深度学习中的梯度消失和梯度爆炸问题，从数学角度（链式法则/激活函数导数/权重初始化）分析其成因，并讨论各种解决方案（ReLU/BatchNorm/残差连接/Gradient Clipping）的数学原理和局限性。",
    "经管": "当前AI技术快速发展对劳动力市场产生深远影响。请从经济学角度分析：AI对高技能和低技能劳动力的替代效应与互补效应有何不同？这对收入分配和教育培训体系有什么启示？应如何设计公共政策来应对？",
}

# 英文文献摘要（按专业方向）
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
            "basics": "接下来我会考察你的专业基础知识。一共12道题，难度递进。准备好了吗？",
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
