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

# 英文文献原文片段（含大量专业术语，用于文献翻译环节）
# 格式: {"title": "...", "source": "...", "text": "...", "terms": ["术语1", ...]}
MAJOR_PAPER_ABSTRACTS = {
    "计算机": [
        """[From "Attention Is All You Need" — Vaswani et al., NeurIPS 2017]

Recurrent neural networks, long short-term memory and gated recurrent neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation. Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states h_t, as a function of the previous hidden state h_{t-1} and the input for position t. This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples.

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs. We propose a new simple network architecture based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.

Key terms: recurrence, transduction, hidden states, parallelization, attention mechanism, encoder-decoder, sequence modeling, Transformer architecture, self-attention, multi-head attention, positional encoding, feed-forward networks, layer normalization, residual connections, beam search, BLEU score.""",
        """[From "BERT: Pre-training of Deep Bidirectional Transformers" - Devlin et al., NAACL 2019]

We introduce BERT, a new language representation model. BERT pre-trains deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers.

BERT uses a masked language model (MLM) pre-training objective. BERT-large achieves 11 new NLP benchmarks including SQuAD v1.1 question answering.

Key terms: BERT, pre-training, transformer, masked language model, fine-tuning, NLP, bidirectional, attention mechanism, transfer learning""",
        """[From "Generative Adversarial Networks" - Goodfellow et al., NeurIPS 2014]

We propose a framework for estimating generative models via an adversarial process, simultaneously training a generative model G and a discriminative model D.

The training procedure for G is to maximize the probability of D making a mistake. This corresponds to a minimax two-player game with a unique solution.

Key terms: generative adversarial network, generator, discriminator, minimax game, deep learning, image synthesis, Nash equilibrium, mode collapse""",
        """[From "Deep Residual Learning for Image Recognition" - He et al., CVPR 2016]

We present a residual learning framework to ease the training of substantially deeper networks. We reformulate layers as learning residual functions with reference to the layer inputs.

Our residual nets are easier to optimize and gain accuracy from increased depth. On ImageNet, we evaluate residual nets with depth up to 152 layers.

Key terms: residual learning, skip connections, deep neural network, ImageNet, vanishing gradient, batch normalization, convolutional neural network""",
        """[From "Dropout: Preventing Neural Networks from Overfitting" - Srivastava et al., JMLR 2014]

We propose dropout, a technique that addresses overfitting by randomly setting unit activations to zero with probability p during training.

This prevents units from co-adapting too much. Dropout improves performance across vision, speech, and NLP tasks.

Key terms: dropout, regularization, overfitting, ensemble learning, co-adaptation, neural network, generalization""",
        """[From "Adam: A Method for Stochastic Optimization" - Kingma & Ba, ICLR 2015]

We introduce Adam, an algorithm for first-order gradient-based optimization based on adaptive estimates of lower-order moments. Adam combines advantages of AdaGrad and RMSProp.

It maintains per-parameter learning rates adapted based on the first and second moments of the gradients.

Key terms: Adam optimizer, adaptive learning rate, stochastic optimization, momentum, RMSProp, gradient descent, convergence""",
        """[From "GPT-4 Technical Report" - OpenAI, arXiv 2023]

We report GPT-4, a large-scale multimodal model accepting image and text inputs. GPT-4 is a Transformer-based model pre-trained to predict the next token in a document.

GPT-4 exhibits human-level performance on professional and academic benchmarks, including passing a simulated bar exam in the top 10%.

Key terms: large language model, multimodal, alignment, RLHF, scaling laws, emergent capabilities, safety, transformer architecture""",
        """[From "MapReduce: Simplified Data Processing on Large Clusters" - Dean & Ghemawat, OSDI 2004]

MapReduce is a programming model for processing and generating large data sets. Users specify a map function and a reduce function.

The runtime handles partitioning, scheduling, fault tolerance, and inter-machine communication. Programs are automatically parallelized on large clusters.

Key terms: MapReduce, distributed computing, parallel processing, fault tolerance, data partitioning, cluster computing, Hadoop""",
        """[From "The Google File System" - Ghemawat, Gobioff & Leung, SOSP 2003]

We designed the Google File System, a scalable distributed file system for large data-intensive applications with fault tolerance on commodity hardware.

It treats component failures as the norm. Optimized for large files, append operations, and high sustained bandwidth.

Key terms: distributed file system, fault tolerance, chunk server, master node, replication, data-intensive, commodity hardware""",
        """[From "Dynamo: Amazon Highly Available Key-value Store" - DeCandia et al., SOSP 2007]

We describe Dynamo, a highly available key-value store used in Amazon production. High availability through consistent hashing, vector clocks, and sloppy quorum.

Uses an eventually consistent model. Powers several Amazon services including shopping cart.

Key terms: key-value store, eventual consistency, consistent hashing, vector clock, anti-entropy, availability, distributed system""",
        """[From "Raft: An Understandable Consensus Algorithm" - Ongaro & Ousterhout, USENIX ATC 2014]

Raft is a consensus algorithm for managing a replicated log. Equivalent to Paxos but more understandable.

Decomposes consensus into leader election, log replication, and safety. Strong leadership simplifies replicated log management.

Key terms: consensus algorithm, distributed systems, leader election, log replication, fault tolerance, Paxos""",
        """[From "k-means++: The Advantages of Careful Seeding" - Arthur & Vassilvitskii, SODA 2007]

We present a k-means variant achieving O(log k) competitive ratio by choosing initial centers that are spread out.

As fast as k-means in practice. Initialization significantly improves speed and accuracy.

Key terms: k-means, clustering, initialization, competitive ratio, approximation algorithm, unsupervised learning""",
        """[From "Random Forests" - Breiman, Machine Learning 2001]

Random forests combine tree predictors where each tree depends on a random vector sampled independently with the same distribution.

Resistant to overfitting. Provide internal estimates of variable importance. Competitive with boosting.

Key terms: random forest, ensemble method, bagging, decision tree, feature importance, classification, regression""",
        """[From "Support-Vector Networks" - Cortes & Vapnik, Machine Learning 1995]

The support-vector network maps input vectors into high-dimensional feature space and constructs an optimal separating hyperplane.

Incorporates structural risk minimization. Uses kernel functions for efficient dot products.

Key terms: support vector machine, kernel trick, margin maximization, structural risk minimization, classification""",
        """[From "Long Short-Term Memory" - Hochreiter & Schmidhuber, Neural Computation 1997]

We present LSTM, a novel architecture with multiplicative gates controlling information flow, overcoming the vanishing gradient problem.

Learns to bridge time intervals exceeding 1000 steps. Superior on music composition and speech recognition.

Key terms: LSTM, recurrent neural network, vanishing gradient, gating mechanism, memory cell, sequence learning""",
        """[From "ImageNet Classification with Deep CNNs" - Krizhevsky et al., NeurIPS 2012]

We trained a large deep CNN to classify 1.2 million images into 1000 classes. 60 million parameters and 650,000 neurons.

Achieved top-1 error 37.5% and top-5 error 17.0%, significantly better than previous approaches.

Key terms: AlexNet, convolutional neural network, ImageNet, ReLU, dropout, data augmentation, GPU training""",
        """[From "Deep Learning in Medical Image Analysis" - Litjens et al., Medical Image Analysis 2017]

We survey 300+ contributions applying deep learning to medical images: detection, classification, segmentation, registration.

Applied to X-ray, CT, MRI, ultrasound, microscopy. Transfer learning shows promising results.

Key terms: deep learning, medical imaging, CNN, transfer learning, segmentation, detection, U-Net, radiology""",
        """[From "YOLOv4: Optimal Speed and Accuracy of Object Detection" - Bochkovskiy et al., arXiv 2020]

We test various features and propose optimal architecture with CSPDarknet53 backbone, SPP neck, PANet.

Achieves 43.5% AP on MS COCO at 65 FPS. Fastest and most accurate real-time detector.

Key terms: YOLOv4, object detection, real-time, CSPDarknet, feature pyramid, data augmentation, COCO""",
        """[From "FlashAttention: Fast Memory-Efficient Exact Attention" - Dao et al., NeurIPS 2022]

We propose FlashAttention, IO-aware attention computing exact attention with far fewer memory accesses using tiling.

Trains Transformers 3x faster on sequence length 4K. Memory reduced from quadratic to linear.

Key terms: FlashAttention, IO-aware, tiling, memory-efficient, attention, GPU memory, Transformer""",
        """[From "Word2Vec: Efficient Word Representations" - Mikolov et al., ICLR 2013]

We propose architectures for continuous vector word representations from large datasets.

Captures semantic relationships: king - man + woman = queen. Training on 1.6 billion words takes less than a day.

Key terms: Word2Vec, word embeddings, Skip-gram, CBOW, distributed representation, semantic similarity, NLP"""
    ],

    "电子": [
        """[From "High-Performance GaN Vertical Fin Power Transistors on Bulk GaN Substrates" — Zhang et al., IEEE Electron Device Letters 2017]

Wide-bandgap semiconductors, particularly gallium nitride (GaN) and silicon carbide (SiC), have attracted significant attention for next-generation power electronics owing to their superior material properties. The critical electric field of GaN (~3.3 MV/cm) is approximately ten times higher than that of silicon, while the Baliga figure of merit (BFOM), which characterizes the specific on-resistance versus breakdown voltage trade-off, is over 800 times higher. Traditional lateral GaN high-electron-mobility transistors (HEMTs) utilize the two-dimensional electron gas (2DEG) formed at the AlGaN/GaN heterojunction, enabling high electron mobility exceeding 2000 cm^2/V·s and low on-resistance.

However, these lateral devices suffer from surface-state-related current collapse and dynamic on-resistance degradation. Recent advances in vertical GaN device architectures—including trench MOSFETs, fin-channel field-effect transistors (FinFETs), and vertical junction-gate field-effect transistors (VJFETs)—have demonstrated enhanced breakdown voltage capabilities exceeding 1200 V with specific on-resistances below 0.5 mΩ·cm^2. The development of high-quality bulk GaN substrates with threading dislocation densities below 10^6 cm^{-2} has been instrumental in realizing these performance milestones.

Key terms: wide-bandgap, gallium nitride (GaN), silicon carbide (SiC), critical electric field, Baliga figure of merit, on-resistance, breakdown voltage, HEMT, 2DEG, AlGaN/GaN heterojunction, mobility, FinFET, VJFET, MOSFET, threading dislocation, current collapse.""",
        """[From "5G Millimeter-Wave Antenna-in-Package Design" - Zhang & Liu, IEEE Trans. Antennas 2019]

We present an antenna-in-package solution integrating 64 elements with RFIC beamforming at 28 GHz. The phased array achieves 23 dBi gain with beam scanning from -60 to +60 degrees.

Measured radiation efficiency exceeds 85% across 26-30 GHz. LTCC substrate with air cavities enhances efficiency.

Key terms: 5G, millimeter-wave, antenna-in-package, phased array, beamforming, LTCC, gain, radiation efficiency""",
        """[From "FinFET: Self-Aligned Double-Gate MOSFET" - Huang et al., IEDM 2012]

FinFET technology provides a path to continue Moore Law. Tri-gate architecture offers superior electrostatic control, reducing short-channel effects and leakage.

We demonstrate 14nm FinFET with 42nm fin pitch. Drive current improved 37% over planar counterparts at matched leakage.

Key terms: FinFET, double-gate, short-channel effects, leakage current, electrostatic control, tri-gate, Moore Law""",
        """[From "MEMS Accelerometers for Automotive Applications" - Yazdi et al., Proc. IEEE 1998]

MEMS accelerometers have revolutionized automotive safety. We review capacitive, piezoresistive, and piezoelectric designs for crash detection and airbag deployment.

Capacitive accelerometers achieve 50g range, 2kHz bandwidth, 200 micro-g/root-Hz resolution. Temperature compensation and self-test are critical.

Key terms: MEMS, accelerometer, capacitive sensing, automotive, surface micromachining, inertial sensor, airbag""",
        """[From "Spin-Transfer Torque MRAM Technology" - Kent & Worledge, Nature Nanotechnology 2015]

STT-MRAM offers nanosecond switching, unlimited endurance, and CMOS compatibility. We discuss STT switching in magnetic tunnel junctions with MgO barriers.

TMR ratio exceeds 200%. Key challenges include reducing switching current while maintaining thermal stability.

Key terms: MRAM, spin-transfer torque, magnetic tunnel junction, MgO barrier, TMR ratio, non-volatile memory, spintronics""",
        """[From "Flexible OLED Display Technology" - Forrest, Nature 2004]

OLEDs are poised to become the dominant flat-panel display technology. Phosphorescent emitters achieve nearly 100% internal quantum efficiency.

Tandem structures enable white emission exceeding 100 lm/W. Flexible substrates using polyimide enable rollable displays.

Key terms: OLED, organic semiconductor, electroluminescence, flexible display, phosphorescence, quantum efficiency""",
        """[From "Power Amplifier Linearization Using Digital Predistortion" - Ghannouchi & Younes, IEEE Microwave Magazine 2014]

Digital predistortion is the most cost-effective linearization for wireless base stations. Memory polynomial DPD achieves 15dB ACLR improvement.

Indirect learning architecture with feedback receiver sampling at twice signal bandwidth.

Key terms: digital predistortion, power amplifier, nonlinearity, memory polynomial, ACLR, linearization, wireless base station""",
        """[From "Integrated Silicon Photonics for Data Communication" - Soref, IEEE JSTQE 2006]

Silicon photonics leverages CMOS infrastructure for optical components. We review waveguides, modulators, photodetectors for high-bandwidth communication.

Microring resonators enable WDM with 100 GHz channel spacing. MZI modulators achieve 50 Gbps.

Key terms: silicon photonics, optical interconnect, waveguide, modulator, microring, WDM, CMOS, data center""",
        """[From "Deep Learning for ECG Signal Classification" - Hannun et al., Nature Medicine 2019]

We develop a deep neural network to classify 12 rhythm classes from single-lead ECGs. Trained on 91,232 records from 53,549 patients.

Exceeds cardiologist performance. F1 score 0.837. VF detection sensitivity 97.4%, specificity 99.2%.

Key terms: ECG classification, deep learning, arrhythmia detection, CNN, residual network, clinical validation""",
        """[From "Radar Target Detection in Clutter Using Deep Learning" - Hyun et al., IEEE Trans. Aerospace 2020]

We apply deep learning to improve detection of small maritime targets in sea clutter. CNN processes range-Doppler maps.

Improves detection probability 12% over CFAR detectors at 10^-6 false alarm rate. Generalizes across sea states.

Key terms: radar detection, sea clutter, CFAR, deep learning, range-Doppler map, CNN, false alarm rate""",
        """[From "Edge AI: On-Demand Acceleration of Deep Learning Inference" - Chen & Ran, IEEE Micro 2019]

Edge computing brings AI inference closer to data sources. We survey GPU, FPGA, and ASIC accelerators for edge AI.

Knowledge distillation, pruning, quantization reduce model size 10-50x. TensorRT and ONNX enable cross-platform deployment.

Key terms: edge computing, AI accelerator, model compression, quantization, pruning, knowledge distillation, inference""",
        """[From "Wireless Power Transfer via Magnetic Resonance" - Kurs et al., Science 2007]

We demonstrate efficient wireless power transfer over mid-range distances using strongly coupled magnetic resonances.

Transfer 60W with 40% efficiency across 2 meters. Applications include consumer electronics and EV charging.

Key terms: wireless power transfer, magnetic resonance, resonant coupling, quality factor, efficiency, EV charging""",
        """[From "Terahertz Imaging for Non-Destructive Testing" - Mittleman, J. Applied Physics 2018]

Terahertz radiation penetrates non-conductive materials while being non-ionizing. We review THz imaging for NDT.

Time-domain THz spectroscopy enables depth-resolved imaging with 100 micrometer resolution at 30 fps.

Key terms: terahertz, non-destructive testing, time-domain spectroscopy, imaging, defect detection, aerospace""",
        """[From "IoT Sensor Networks for Smart Agriculture" - Tzounis et al., Biosystems Engineering 2017]

IoT sensor networks enable precision agriculture monitoring soil moisture, temperature, and crop health in real-time.

Reduces water consumption 30% through precision irrigation. ML predicts crop yield with 92% accuracy.

Key terms: IoT, wireless sensor network, precision agriculture, LoRa, soil moisture, irrigation, machine learning""",
        """[From "Reconfigurable Intelligent Surfaces for 6G" - Di Renzo et al., IEEE JSAC 2020]

RIS are planar arrays of passive elements dynamically modifying propagation environment. Enhance signal by 20 dB.

Energy consumption negligible compared to active relays. Channel estimation and phase control are key challenges.

Key terms: reconfigurable intelligent surface, 6G, passive beamforming, channel estimation, energy efficiency""",
        """[From "CMOS Image Sensor Technology" - Fossum, IEEE Trans. Electron Devices 1997]

CMOS active pixel sensors offer lower power, random access, and on-chip processing over CCDs.

Pinned photodiode pixels achieve read noise below 2 electrons. Backside illumination improves QE to 80%.

Key terms: CMOS image sensor, active pixel, pinned photodiode, quantum efficiency, read noise, dynamic range""",
        """[From "Quantum Dot Solar Cells" - Nozik, Physica E 2002]

Quantum dots offer tunable bandgap, multiple exciton generation, and solution processability for solar energy.

PbS QD solar cells achieve 12% efficiency. MEG could theoretically push efficiency beyond Shockley-Queisser limit.

Key terms: quantum dot, solar cell, multiple exciton generation, tunable bandgap, PbS, photovoltaic""",
        """[From "Plasma Etching for Semiconductor Manufacturing" - Coburn & Winters, J. Vac. Sci. 1979]

Plasma etching enables anisotropic pattern transfer for IC fabrication. We discuss ion-enhanced etching mechanisms.

RIE using fluorine chemistries achieves selectivity >10:1 for SiO2 over Si. ALE provides atomic-scale precision.

Key terms: plasma etching, reactive ion etching, anisotropic, selectivity, atomic layer etching, semiconductor""",
        """[From "MEMS Gyroscope Design and Applications" - Acar & Shkel, Wiley 2009]

MEMS gyroscopes measure angular rate using the Coriolis effect on vibrating structures. Quality factor and mode matching are critical.

Achieve bias stability of 1 degree/hr with quadrature error cancellation. Applications in automotive and navigation.

Key terms: MEMS gyroscope, Coriolis effect, tuning fork, quality factor, angular rate, navigation, automotive""",
        """[From "Thermal Barrier Coatings for Gas Turbines" - Padture et al., Science 2002]

YSZ coatings protect turbine blades from hot gas temperatures exceeding 1500C. We discuss TGO, sintering, and CMAS failure.

Reduce metal substrate temperature by 100-300C. EB-PVD produces columnar microstructure with superior strain tolerance.

Key terms: thermal barrier coating, YSZ, gas turbine, TGO, EB-PVD, thermal conductivity, strain tolerance"""
    ],

    "机械": [
        """[From "Additive Manufacturing of Ti-6Al-4V Alloy Components by Selective Laser Melting" — Thijs et al., Acta Materialia 2010]

Selective laser melting (SLM) is an additive manufacturing technique that utilizes a high-power laser to selectively fuse metallic powder particles in a layer-by-layer fashion, directly producing near-net-shape components from three-dimensional CAD models. The Ti-6Al-4V alloy, which belongs to the α+β titanium alloy class, is by far the most widely used titanium alloy, accounting for more than 50% of global titanium production, owing to its excellent combination of specific strength, corrosion resistance, and biocompatibility.

During SLM processing, the alloy undergoes rapid melting followed by extremely fast solidification at cooling rates on the order of 10^3–10^8 K/s. This results in the formation of a fine acicular martensitic α' phase within columnar prior-β grains that grow epitaxially across multiple powder layers in the direction of the thermal gradient. The resulting microstructure exhibits a hierarchical morphology, with the prior-β grain boundaries decorated by a continuous network of grain boundary α phase. Through optimization of process parameters—including laser power (100–400 W), scan speed (200–1200 mm/s), hatch spacing (50–150 μm), and layer thickness (30–60 μm)—the volumetric energy density can be controlled to minimize porosity and maximize density above 99.5%.

Key terms: selective laser melting (SLM), Ti-6Al-4V, α+β titanium alloy, specific strength, cooling rate, acicular martensitic α' phase, columnar prior-β grains, epitaxial growth, thermal gradient, hatch spacing, volumetric energy density, layer thickness, near-net-shape.""",
        """[From "Topology Optimization for Structural Design" - Bendsoe & Sigmund, Springer 2003]

Topology optimization optimizes material layout within a design space. The SIMP method interpolates material density.

We minimize compliance subject to volume constraint. Optimized structures exhibit organic, biomimetic forms.

Key terms: topology optimization, SIMP, compliance minimization, finite element method, biomimetic design, 3D printing""",
        """[From "Friction Stir Welding of Aluminum Alloys" - Mishra & Ma, Mater. Sci. Eng. 2005]

FSW is a solid-state joining process using a non-consumable tool. We review FSW of 2xxx, 6xxx, 7xxx aluminum alloys.

Produces joints with 90-100% efficiency. Stir zone exhibits fine equiaxed grains from dynamic recrystallization.

Key terms: friction stir welding, aluminum alloy, solid-state joining, dynamic recrystallization, aerospace""",
        """[From "Finite Element Analysis of Contact Problems" - Wrigley, J. Tribology 1985]

Contact mechanics problems are inherently nonlinear. We present FEM formulations using penalty and Lagrange multiplier methods.

Augmented Lagrangian combines advantages of both. Adaptive mesh refinement in contact zone improves accuracy.

Key terms: finite element analysis, contact mechanics, penalty method, Lagrange multiplier, friction, Hertzian contact""",
        """[From "Vibration-Based Condition Monitoring of Rotating Machinery" - Randall, Wiley 2011]

Vibration analysis is the most widely used technique for condition monitoring. We describe time-domain, frequency, and envelope methods.

Bearing faults produce characteristic frequencies. Gear faults appear as sidebands around gear mesh frequency.

Key terms: vibration analysis, condition monitoring, bearing fault, gear fault, spectral kurtosis, predictive maintenance""",
        """[From "CFD for Turbomachinery Design" - Denton, J. Turbomachinery 1992]

CFD is indispensable for turbomachinery design. We review Navier-Stokes solvers for turbine and compressor blade design.

RANS with k-omega SST provides reasonable loss and heat transfer predictions. LES resolves unsteady features.

Key terms: CFD, turbomachinery, Navier-Stokes, turbulence modeling, RANS, blade design, heat transfer""",
        """[From "Robot Manipulator Control: Theory and Practice" - Sciavicco & Siciliano, Springer 2000]

We present mathematical foundations of robot control including kinematics, dynamics, and trajectory planning.

Computed torque control achieves trajectory tracking by canceling nonlinear dynamics. Impedance control regulates interaction force.

Key terms: robot manipulator, kinematics, dynamics, Denavit-Hartenberg, computed torque, impedance control, trajectory planning""",
        """[From "Composite Materials: Design and Applications" - Daniel & Ishai, Wiley 2006]

Fiber-reinforced polymer composites offer high specific strength for aerospace and automotive. We present micromechanical models.

Classical lamination theory relates ply to laminate stiffness. Failure criteria include Tsai-Hill and Tsai-Wu.

Key terms: composite material, fiber reinforcement, lamination theory, failure criteria, carbon fiber, autoclave""",
        """[From "Hydraulic System Design for Mobile Equipment" - Manring, Wiley 2005]

Hydraulic systems provide high power density for excavators, loaders, and agricultural machinery.

Variable displacement piston pumps achieve 30% energy savings. Proportional valves enable precise flow control.

Key terms: hydraulic system, load sensing, variable displacement pump, mobile equipment, excavator, energy efficiency""",
        """[From "Heat Transfer Enhancement in Microchannels" - Kandlikar, Heat Transfer Eng. 2003]

Microchannel heat exchangers offer high heat transfer coefficients for electronics cooling.

Forced convection achieves coefficients exceeding 10,000 W/m2K. Flow boiling enables isothermal cooling.

Key terms: microchannel, heat transfer, electronics cooling, convection, boiling, heat exchanger, thermal management""",
        """[From "Bearing Selection and Life Calculation" - SKF, Technical Report 2018]

Rolling element bearing life is calculated using L10 = (C/P)^p. C is dynamic load rating, P is equivalent load.

Modified life calculation accounts for lubrication, contamination, and reliability factors.

Key terms: bearing life, L10 life, dynamic load rating, equivalent load, lubrication, contamination, reliability""",
        """[From "Stress Analysis of Bolted Joints" - Bickford, CRC Press 2007]

Bolted joints are the most common fastening method. Load distribution uses joint constant C = kb/(kb+km).

Torque-tension: T = K*d*F where K is nut factor (0.15-0.3). Proper tightening ensures consistent preload.

Key terms: bolted joint, preload, torque-tension, joint constant, gasket, fatigue, vibration loosening""",
        """[From "CNC Machining of Hardened Steels" - Tonshoff et al., CIRP Annals 2006]

Hard turning and milling of steels above 45 HRC eliminates grinding. We investigate tool wear with CBN tools.

CBN achieves Ra 0.2 micrometer surface finish with 15 min tool life. White layer formation affects fatigue life.

Key terms: CNC machining, hard turning, CBN tool, tool wear, surface integrity, white layer, bearing steel""",
        """[From "Stochastic Fatigue Analysis Using Rainflow Counting" - Downing & Socie, Int. J. Fatigue 1982]

Random loading causes variable amplitude fatigue damage. Rainflow counting identifies hysteresis loops from irregular histories.

Rainflow produces more accurate fatigue life predictions than level crossing or range counting methods.

Key terms: fatigue, rainflow counting, variable amplitude, Miner rule, hysteresis loop, damage accumulation, S-N curve""",
        """[From "Topology Optimization of Compliant Mechanisms" - Sigmund, Mech. Structures 2001]

Compliant mechanisms achieve motion through elastic deformation. We apply topology optimization for specified input-output displacement.

Maximize geometric advantage subject to stress constraints. Flexure hinges concentrate strain for large deflection.

Key terms: compliant mechanism, topology optimization, flexure, large deflection, geometric advantage, MEMS, microgripper""",
        """[From "Laser Surface Treatment for Wear Resistance" - Steen & Mazumder, Springer 2010]

Laser surface treatment including hardening, alloying, and cladding improves wear resistance.

Laser hardening produces martensitic surface with 60 HRC over 0.5mm depth. Self-quenching with minimal distortion.

Key terms: laser surface treatment, hardening, wear resistance, martensite, diode laser, self-quenching, tribology""",
        """[From "3D Printing of Patient-Specific Medical Implants" - Sing et al., Acta Biomaterialia 2016]

Additive manufacturing enables patient-specific implants with controlled porous structures.

Lattice structures with 60% porosity achieve elastic modulus matching bone (10-30 GPa), reducing stress shielding.

Key terms: 3D printing, medical implant, patient-specific, porous structure, Ti-6Al-4V, stress shielding, osseointegration""",
        """[From "Corrosion of Stainless Steels in Aggressive Environments" - Marcus, Wiley 2002]

Stainless steels rely on passive chromium oxide film. We discuss pitting and crevice corrosion by chloride ions.

Duplex stainless steels (2205, 2507) offer superior SCC resistance. Mo and N improve PREN.

Key terms: stainless steel, corrosion, pitting, crevice corrosion, passivity, duplex, SCC, PREN, chloride""",
        """[From "Aerodynamic Design of Wind Turbine Blades" - Hansen, Cambridge 2008]

Wind turbine blade design balances aerodynamic efficiency with structural integrity. We use BEM theory for initial design.

Airfoil selection affects power coefficient and noise. Pitch control regulates power above rated wind speed.

Key terms: wind turbine, blade design, BEM theory, airfoil, power coefficient, pitch control, aerodynamic""",
        """[From "Gear Design and Failure Modes" - Dudley, McGraw-Hill 1962]

Gear design must consider bending fatigue, surface wear, and scoring. We analyze Hertzian contact stress at tooth surfaces.

AGMA standards provide design procedures for spur, helical, and bevel gears. Lubrication is critical for scuffing prevention.

Key terms: gear design, bending fatigue, surface wear, Hertzian contact, AGMA, spur gear, helical gear, lubrication"""
    ],

    "材料": [
        """[From "Lead Iodide Perovskite Sensitized All-Solid-State Submicron Thin Film Mesoscopic Solar Cell with Efficiency Exceeding 9%" — Kim, Gratzel, Park et al., Scientific Reports 2012]

We report on solid-state mesoscopic heterojunction solar cells employing nanoparticles (NPs) of methyl ammonium lead iodide (CH3NH3)PbI3 as light harvesters. The perovskite NPs were produced by reaction of methylammonium iodide with PbI2 and deposited onto a submicron-thick mesoscopic TiO2 film, whose pores were infiltrated with the hole-conductor spiro-MeOTAD. Illumination with standard AM-1.5 sunlight generated large photocurrents (J_SC) exceeding 17 mA/cm^2, an open circuit photovoltage (V_OC) of 0.888 V and a fill factor (FF) of 0.62, yielding a power conversion efficiency (PCE) of 9.7%.

Femtosecond laser studies combined with photo-induced absorption measurements showed charge separation to proceed via hole injection from the excited (CH3NH3)PbI3 NPs into the spiro-MeOTAD, followed by electron transfer to the mesoscopic TiO2 film. The use of a solid hole conductor dramatically improved the device stability compared to liquid junction cells. Further optimization through compositional engineering—including mixed cation (FA, MA, Cs) and mixed halide (I, Br, Cl) formulations—has since pushed certified PCE beyond 25%, rivaling established thin-film technologies such as copper indium gallium selenide (CIGS) and cadmium telluride (CdTe).

Key terms: perovskite, mesoscopic, heterojunction, methylammonium lead iodide, spiro-MeOTAD, AM-1.5, photocurrent, open circuit voltage, fill factor, PCE, femtosecond spectroscopy, charge separation, hole injection, compositional engineering, mixed cation, mixed halide.""",
        """[From "Carbon Nanotube Synthesis and Applications" - Iijima, Nature 1991]

We observe helical microtubules of graphitic carbon using HRTEM. Multi-wall nanotubes consist of coaxial graphitic sheets.

Tubules grow by plasma arc discharge. Applications in field emission, composites, and nanoelectronics.

Key terms: carbon nanotube, graphene, arc discharge, TEM, nanostructure, field emission, nanoelectronics""",
        """[From "Metal-Organic Frameworks for Gas Storage" - Yaghi et al., Chem. Rev. 2012]

MOFs are crystalline porous materials with surface areas exceeding 7000 m2/g. We review reticular chemistry for tailored design.

MOFs achieve methane storage of 200 cm3/cm3 at 65 bar. CO2/N2 selectivity exceeds 100 in amine-functionalized MOFs.

Key terms: metal-organic framework, porous material, gas storage, gas separation, reticular chemistry, CO2 capture""",
        """[From "Biodegradable Polymers for Biomedical Applications" - Middleton & Tipton, Biomaterials 2000]

We review PLA, PGA, and PLGA for medical devices and drug delivery. Degradation by hydrolysis over weeks to months.

Degradation rate controlled by monomer ratio, crystallinity, and molecular weight. FDA-approved for sutures and scaffolds.

Key terms: biodegradable polymer, PLA, PGA, PLGA, hydrolysis, drug delivery, scaffold, biomedical""",
        """[From "Shape Memory Alloys: Properties and Applications" - Otsuka & Wayman, Cambridge 1999]

SMAs recover original shape upon heating after deformation. We review martensitic transformation in NiTi, Cu-based, and Fe-based SMAs.

NiTi exhibits excellent biocompatibility for stents and orthodontic wires. Superelasticity enables 8% recoverable strain.

Key terms: shape memory alloy, NiTi, martensitic transformation, superelasticity, biocompatibility, stent, actuator""",
        """[From "Graphene: Properties, Synthesis, and Applications" - Novoselov et al., Science 2004]

We report graphene, a single atomic layer of carbon. Extracted by mechanical exfoliation. Carrier mobility exceeding 15,000 cm2/Vs.

Young modulus 1 TPa, intrinsic strength 130 GPa, thermal conductivity 5000 W/mK.

Key terms: graphene, exfoliation, mobility, mechanical properties, thermal conductivity, transparent electrode, transistor""",
        """[From "High-Entropy Alloys: A New Frontier" - Yeh et al., Adv. Eng. Mater. 2004]

HEAs contain five or more principal elements in equimolar ratios. High mixing entropy stabilizes solid solutions.

CoCrFeMnNi HEA exhibits tensile strength >1 GPa with 60% ductility. Cryogenic temperature enhances properties through TWIP.

Key terms: high-entropy alloy, solid solution, mixing entropy, lattice distortion, twinning, cryogenic, phase stability""",
        """[From "Quantum Dots: Synthesis, Properties, and Applications" - Murray et al., Ann. Rev. Mater. Sci. 2000]

Semiconductor QDs exhibit size-dependent properties from quantum confinement. Hot-injection synthesis produces <5% size distribution.

CdSe/ZnS core-shell structures improve stability and QY to >50%. Applications in labeling, LEDs, and solar cells.

Key terms: quantum dot, CdSe, quantum confinement, hot-injection, photoluminescence, core-shell, nanocrystal""",
        """[From "Thermoelectric Materials for Waste Heat Recovery" - Snyder & Toberer, Nature Mater. 2008]

Thermoelectric materials convert temperature gradients to voltage via Seebeck effect. ZT = S2sigma*T/kappa.

Bi2Te3 achieves ZT of 1.0 near room temperature. PbTe reaches ZT of 2.0 at 700K.

Key terms: thermoelectric, Seebeck effect, figure of merit, ZT, thermal conductivity, nanostructuring, waste heat recovery""",
        """[From "Superconducting Materials for High-Field Magnets" - Foltyn et al., Nature Mater. 2007]

HTS including YBCO enable magnetic fields exceeding 20T. We review coated conductor fabrication.

YBCO carries Jc of 1000 A/mm2 at 77K. At 4K, exceeds NbTi and Nb3Sn above 23T.

Key terms: superconductor, YBCO, coated conductor, critical current, high magnetic field, HTS, fusion magnet""",
        """[From "Polymer Nanocomposites: Processing and Properties" - Paul & Robeson, Polymer 2008]

Polymer nanocomposites with 1-5 wt% nanofillers show dramatically improved properties.

Melt compounding and in-situ polymerization are scalable. Applications in packaging, automotive, and aerospace.

Key terms: polymer nanocomposite, clay, carbon nanotube, graphene, exfoliation, melt compounding, mechanical properties""",
        """[From "Transparent Conducting Oxides for Optoelectronics" - Minami, Semicond. Sci. Technol. 2005]

TCOs including ITO, ZnO, SnO2 are essential for displays, solar cells, and touchscreens.

ITO achieves 10 ohm/sq sheet resistance with 90% transmittance. Al-doped ZnO offers cost advantages.

Key terms: transparent conductor, ITO, ZnO, SnO2, sputtering, sheet resistance, transmittance, display, solar cell""",
        """[From "Bioceramics for Bone Tissue Engineering" - Hench, JACS 1998]

Bioactive ceramics including HA and TCP bond directly to bone. We review porous scaffolds for bone regeneration.

HA scaffolds with 60% porosity and 500 micrometer pores support osteoblast colonization.

Key terms: bioceramic, hydroxyapatite, tricalcium phosphate, bioactive, bone scaffold, porosity, tissue engineering""",
        """[From "Thermal Spray Coatings for Engineering" - Pawlowski, Wiley 2008]

Thermal spray processes deposit coatings from 50 micrometers to several mm thickness.

WC-Co by HVOF achieves 1200 HV hardness. YSZ protects hot-section components.

Key terms: thermal spray, plasma spray, HVOF, WC-Co, YSZ, coating, wear resistance, hardness""",
        """[From "Electrospinning of Nanofiber Scaffolds" - Li & Xia, Adv. Mater. 2004]

Electrospinning produces nanofibers with diameters from 3nm to 5 micrometers using high electric fields.

Aligned scaffolds guide cell orientation. High surface area and tunable porosity.

Key terms: electrospinning, nanofiber, scaffold, tissue engineering, filtration, drug delivery, aligned fiber""",
        """[From "Magnesium Alloys for Lightweight Automotive" - Kulekci, Int. J. Adv. Manuf. 2008]

Mg alloys offer lowest density (1.74 g/cm3) among structural metals. We review die casting and sheet forming.

Challenges include limited room-temperature formability, high corrosion rate, and flammability.

Key terms: magnesium alloy, lightweight, die casting, automotive, formability, corrosion, creep resistance""",
        """[From "Self-Healing Polymers and Composites" - White et al., Nature 2001]

We report a self-healing polymer using microencapsulated dicyclopentadiene monomer and Grubbs catalyst.

Capsules rupture when cracks propagate, releasing healing agent. Recovery of 75% fracture toughness.

Key terms: self-healing, microcapsule, healing agent, catalyst, polymer composite, fracture toughness""",
        """[From "Lithium-Ion Battery Electrode Materials" - Goodenough & Kim, Chem. Mater. 2010]

We review cathode and anode materials for Li-ion batteries. Layered oxides, spinel, and olivine cathodes offer different trade-offs.

Graphite anodes: 372 mAh/g capacity. Silicon anodes offer 10x theoretical capacity but suffer volume expansion.

Key terms: lithium-ion battery, cathode, anode, LiCoO2, LiFePO4, graphite, silicon, energy density""",
        """[From "Biodegradable Magnesium Implants" - Staiger et al., Biomaterials 2006]

Mg and alloys are biodegradable metals absorbable in vivo. We review orthopedic implant applications.

Alloying with Zn, Ca, rare earth reduces degradation rate. Mg ions promote osteoblast activity.

Key terms: magnesium implant, biodegradable, orthopedic, corrosion rate, alloying, surface coating, osteoblast""",
        """[From "Additive Manufacturing of Ti-6Al-4V by SLM" - Thijs et al., Acta Materialia 2010]

SLM produces near-fully dense metal parts from powder. We investigate microstructure and properties of Ti-6Al-4V.

Columnar beta grains with strong <100> texture. Tensile strength >1000 MPa with 10% elongation.

Key terms: selective laser melting, Ti-6Al-4V, additive manufacturing, microstructure, mechanical properties, porosity"""
    ],

    "生物": [
        """[From "Genome engineering using the CRISPR-Cas9 system" — Ran, Hsu, Wright, Agarwala, Scott & Zhang, Nature Protocols 2013]

Targeted nucleases are powerful tools for mediating genome alteration with high precision. The RNA-guided Cas9 nuclease from the microbial clustered regularly interspaced short palindromic repeats (CRISPR) adaptive immune system can be used to facilitate efficient genome engineering in eukaryotic cells by simply specifying a 20-nucleotide targeting sequence within its guide RNA. Here we describe a set of tools for Cas9-mediated genome editing via nonhomologous end joining (NHEJ) or homology-directed repair (HDR) in mammalian cells, as well as generation of modified clonal cell lines for downstream functional studies.

The specificity of the Cas9 nuclease is determined by the 20-nt guide sequence within the sgRNA. For the S. pyogenes system, the target sequence must immediately precede a 5'-NGG protospacer adjacent motif (PAM), and the 20-nt guide sequence base pairs with the opposite strand to mediate Cas9 cleavage at ~3 bp upstream of the PAM. To minimize off-target cleavage, we further describe a double-nicking strategy using the Cas9 nickase mutant (Cas9n) with paired guide RNAs. An aspartate-to-alanine (D10A) mutation in the RuvC catalytic domain allows Cas9n to nick rather than cleave DNA, and when two nicks are introduced in close proximity on opposite strands, a double-strand break (DSB) with long overhangs is generated, significantly improving targeting specificity.

Key terms: CRISPR, Cas9 nuclease, guide RNA (sgRNA), protospacer adjacent motif (PAM), nonhomologous end joining (NHEJ), homology-directed repair (HDR), nickase, RuvC domain, D10A mutation, double-strand break (DSB), off-target cleavage, clonal cell lines, SURVEYOR assay.""",
        """[From "Single-Cell RNA Sequencing Reveals Cell Type Diversity" - Macosko et al., Cell 2015]

The mammalian retina has 60+ neuronal subtypes. Bulk RNA-seq masks heterogeneity. Droplet-based scRNA-seq enables high-throughput profiling.

UMAP and t-SNE reveal transcriptionally distinct clusters. Pseudotime ordering reconstructs developmental trajectories.

Key terms: single-cell RNA sequencing, droplet microfluidics, UMAP, t-SNE, pseudotime, cellular heterogeneity""",
        """[From "AlphaFold: Accurate Protein Structure Prediction" - Jumper et al., Nature 2021]

Predicting 3D protein structure from sequence is a grand challenge. AlphaFold uses deep neural networks on MSA features.

Achieved median GDT 92.4 on CASP14. Predicted structures for 200+ million proteins.

Key terms: protein folding, multiple sequence alignment, Evoformer, attention mechanism, GDT score, CASP, deep learning""",
        """[From "CAR T Cell Therapy for B-Cell Malignancies" - June et al., NEJM 2018]

CAR T cell therapy is a paradigm shift in cancer immunotherapy. Tisagenlecleucel targeting CD19 achieves 83% complete remission.

Cytokine release syndrome and neurotoxicity are manageable. Long-term persistence enables durable remissions.

Key terms: CAR T cell, immunotherapy, CD19, chimeric antigen receptor, cytokine release syndrome, adoptive cell transfer""",
        """[From "DNA Methylation Dynamics During Development" - Smith et al., Nature 2014]

DNA methylation at CpG dinucleotides is a key epigenetic mark. Whole-genome bisulfite sequencing reveals methylome dynamics.

Global demethylation after fertilization, then re-establishment. TET enzymes catalyze 5mC oxidation.

Key terms: DNA methylation, CpG, bisulfite sequencing, TET enzyme, epigenetics, imprinting, reprogramming""",
        """[From "Gut Microbiome Signatures of Metabolic Syndrome" - Qin et al., Nature 2012]

We characterize metagenome of 124 Europeans, identifying 3.3 million unique genes.

T2D patients show decreased butyrate producers and increased pathogens. FMT improves insulin sensitivity.

Key terms: gut microbiome, metagenomics, metabolic syndrome, type 2 diabetes, butyrate, fecal transplant, insulin resistance""",
        """[From "Optogenetic Control of Neural Circuits" - Deisseroth et al., Nature Methods 2010]

Optogenetics enables millisecond control of genetically defined neural populations using light-sensitive opsins.

Channelrhodopsin-2 depolarizes neurons with blue light. Halorhodopsin enables hyperpolarization with yellow light.

Key terms: optogenetics, channelrhodopsin, halorhodopsin, neural circuit, light-activated, behavior, neuroscience""",
        """[From "Cerebral Organoids Reveal Early Brain Development" - Lancaster et al., Nature 2013]

We establish 3D culture generating cerebral organoids from human pluripotent stem cells.

Organoids develop distinct brain regions including cerebral cortex. Model microcephaly using patient-derived iPSCs.

Key terms: cerebral organoid, pluripotent stem cell, brain development, microcephaly, self-organization, iPSC""",
        """[From "AAV Gene Therapy for Spinal Muscular Atrophy" - Mendell et al., NEJM 2017]

We deliver SMN1 gene via AAV9 to 15 infants with SMA type 1. All achieved motor milestones including sitting and standing.

Survival without permanent ventilation 100% at 20 months.

Key terms: gene therapy, AAV9, spinal muscular atrophy, SMN1, motor neuron, viral vector, motor milestones""",
        """[From "Mass Cytometry for Immune Profiling" - Bandura et al., Anal. Chem. 2009]

Mass cytometry combines TOF mass spectrometry with flow cytometry. Metal-conjugated antibodies measure 40+ parameters per cell.

High-dimensional analysis reveals novel cell populations. Clinical applications in transplantation monitoring.

Key terms: mass cytometry, CyTOF, immune profiling, metal-conjugated antibody, flow cytometry, high-dimensional analysis""",
        """[From "Quantitative Western Blot Analysis" - Mahmood et al., Methods Mol. Biol. 2012]

Western blotting is fundamental for protein detection. We describe optimized protocols for quantitative analysis.

Near-infrared fluorescent detection provides wider dynamic range than chemiluminescence.

Key terms: Western blot, SDS-PAGE, immunodetection, fluorescent detection, quantitative analysis, protein normalization""",
        """[From "Real-Time Quantitative PCR" - Heid et al., Genome Research 1996]

Real-time qPCR measures DNA amplification during each cycle. TaqMan assay uses fluorescent probes for specific detection.

Threshold cycle (Ct) inversely proportional to initial template quantity. Validated for gene expression and viral load.

Key terms: qPCR, TaqMan, real-time PCR, threshold cycle, fluorescence, gene expression, viral load""",
        """[From "Multiplex IHC for Tumor Microenvironment" - Tsujikawa et al., Nat. Commun. 2017]

Multiplex IHC enables simultaneous detection of multiple biomarkers on a single tissue section.

We map spatial organization of immune cells in tumor microenvironment. Proximity predicts immunotherapy response.

Key terms: multiplex IHC, immunohistochemistry, tumor microenvironment, immune cell, biomarker, spatial analysis""",
        """[From "Sandwich ELISA for Cytokine Detection" - Voller et al., Bull. WHO 1976]

ELISA is a plate-based assay for detecting and quantifying soluble proteins. Sandwich format uses capture and detection antibodies.

Biotinylated detection with streptavidin-HRP achieves 1 pg/mL sensitivity. Multiplex platforms measure dozens of analytes.

Key terms: ELISA, sandwich assay, cytokine, capture antibody, detection antibody, HRP, immunoassay, multiplex""",
        """[From "ChIP-Seq for Protein-DNA Interactions" - Johnson et al., Science 2007]

ChIP-seq maps protein-DNA interactions genome-wide. We present the first ChIP-seq study of NRSF binding.

10,000 binding sites identified with 50 bp resolution. Peak calling algorithms distinguish true binding from background.

Key terms: ChIP-seq, chromatin immunoprecipitation, transcription factor, binding site, peak calling, genome-wide""",
        """[From "Cryo-EM Structure Determination" - Dubochet et al., Ann. Rev. Biophys. 2017]

Cryo-EM enables structure determination of macromolecules in near-native states. Vitrify samples in thin ice.

Direct electron detectors push resolution below 2 Angstroms. Single-particle analysis without crystallization.

Key terms: cryo-EM, vitrification, single-particle analysis, direct electron detector, 3D reconstruction, resolution""",
        """[From "Label-Free Quantitative Proteomics by LC-MS/MS" - Cox et al., Nat. Biotechnol. 2014]

Label-free quantitative proteomics using LC-MS/MS. MaxLFQ enables accurate quantification without metabolic labeling.

Over 10,000 proteins identified from human cell lines. Intensity-based absolute quantification estimates copy numbers.

Key terms: proteomics, LC-MS/MS, label-free quantification, MaxLFQ, protein identification, mass spectrometry""",
        """[From "BLAST: Fast Local Sequence Alignment" - Altschul et al., J. Mol. Biol. 1990]

BLAST finds regions of local similarity between biological sequences. Uses substitution matrix and statistical framework.

100x faster than Smith-Waterman with comparable sensitivity. E-value provides statistical significance measure.

Key terms: BLAST, sequence alignment, homology, substitution matrix, E-value, database search, local alignment""",
        """[From "Induction of Pluripotent Stem Cells" - Takahashi & Yamanaka, Cell 2006]

Somatic cells reprogrammed to pluripotent stem cells by introducing Oct3/4, Sox2, Klf4, c-Myc.

iPSCs form teratomas and contribute to chimeric mice. Enables patient-specific disease modeling.

Key terms: induced pluripotent stem cell, iPSC, reprogramming, Yamanaka factors, Oct4, Sox2, pluripotency""",
        """[From "Pig-to-Human Xenotransplantation with CRISPR" - Montgomery et al., NEJM 2022]

First pig-to-human heart xenotransplant using genetically modified porcine donor with 10 gene modifications.

Heart functioned 2 months without hyperacute rejection. Path toward clinical xenotransplantation.

Key terms: xenotransplantation, pig heart, CRISPR, gene editing, hyperacute rejection, immunosuppression, organ shortage"""
    ],

    "化学": [
        """[From "Palladium-Catalyzed Cross-Coupling Reactions of Organoboron Compounds" — Miyaura & Suzuki, Chemical Reviews 1995]

The palladium-catalyzed cross-coupling reaction of organoboron compounds with organic electrophiles—now widely recognized as the Suzuki-Miyaura coupling—has emerged as one of the most powerful and versatile methods for the construction of carbon-carbon bonds in organic synthesis. The reaction proceeds through a well-established catalytic cycle involving three fundamental organometallic transformations: (i) oxidative addition of an organic halide or triflate to a Pd(0) species to form a Pd(II) intermediate; (ii) transmetallation, wherein the organoboron reagent transfers its organic group to palladium, typically facilitated by a Brønsted base (e.g., K2CO3, K3PO4, or KF) that converts the neutral boronic acid to a more nucleophilic boronate species; and (iii) reductive elimination, which couples the two carbon ligands on Pd(II) to regenerate the Pd(0) catalyst while forming the desired C-C bond.

The broad functional group tolerance of organoboronic acids, their air and moisture stability, low toxicity compared to organotin (Stille) and organozinc (Negishi) reagents, and the mild reaction conditions have rendered the Suzuki coupling indispensable in both academic laboratories and industrial-scale pharmaceutical manufacturing.

Key terms: palladium-catalyzed, cross-coupling, organoboron, electrophile, oxidative addition, transmetallation, reductive elimination, Pd(0)/Pd(II), boronate, Brønsted base, boronic acid, Suzuki-Miyaura, Stille coupling, Negishi coupling, functional group tolerance, triflate.""",
        """[From "Copper(I)-Catalyzed Azide-Alkyne Cycloaddition" - Kolb, Finn & Sharpless, Angew. Chem. 2001]

We introduce Cu(I)-catalyzed Huisgen 1,3-dipolar cycloaddition. Completely regioselective, producing only 1,4-disubstituted triazoles.

Proceeds in water at room temperature with high yield. One of the most widely used click chemistry reactions.

Key terms: click chemistry, copper catalysis, azide-alkyne cycloaddition, triazole, regioselective, bioconjugation""",
        """[From "CRISPR-Cas9 as a Programmable DNA Endonuclease" - Jinek et al., Science 2012]

Cas9 is an RNA-guided DNA endonuclease using base pairing for target recognition. We program it with single guide RNAs.

Dual-RNA simplified into single chimeric guide. Cleavage site mapped to 3 bp upstream of PAM.

Key terms: CRISPR-Cas9, programmable nuclease, guide RNA, DNA cleavage, PAM, genome editing""",
        """[From "Reticular Synthesis of Metal-Organic Frameworks" - Yaghi et al., Nature 2003]

We introduce MOF synthesis by reticular chemistry using SBUs as rigid nodes connected by organic linkers.

MOF-5: pore volume 1.3 cm3/g, surface area 3800 m2/g. Isoreticular expansion by varying linker length.

Key terms: metal-organic framework, reticular chemistry, secondary building unit, porous material, surface area""",
        """[From "Visible-Light Photocatalysis with N-doped TiO2" - Asahi et al., Science 2001]

Nitrogen-doped TiO2 absorbs visible light and decomposes organic pollutants. Band gap narrowed from 3.2 to 2.4 eV.

Photocatalytic activity under visible light (lambda < 500 nm). Applications in water purification.

Key terms: photocatalysis, TiO2, nitrogen doping, visible light, band gap, organic pollutant, water purification""",
        """[From "LiFePO4 as a Cathode Material" - Padhi et al., J. Electrochem. Soc. 1997]

Olivine LiFePO4 is a promising cathode with flat voltage at 3.4V and theoretical capacity 170 mAh/g.

Excellent thermal stability, low cost, environmental friendliness. Carbon coating overcomes low conductivity.

Key terms: LiFePO4, lithium-ion battery, cathode, olivine, iron phosphate, capacity, thermal stability""",
        """[From "Host-Guest Recognition in Supramolecular Chemistry" - Whitesides et al., JACS 1991]

Supramolecular chemistry studies non-covalent interactions. Crown ethers bind alkali cations. Cyclodextrins form inclusion complexes.

Applications in molecular recognition, sensing, and catalysis. Thermodynamic basis of selectivity analyzed.

Key terms: supramolecular chemistry, host-guest, crown ether, cyclodextrin, non-covalent interaction, molecular recognition""",
        """[From "Solvent-Free Organic Reactions" - Tanaka, Springer 2003]

Solvent-free reactions reduce waste and improve atom economy. Ball milling drives chemical transformations.

Liquid-assisted grinding improves yields. Demonstrates aldol condensation, Michael addition, click chemistry.

Key terms: solvent-free, mechanochemistry, ball milling, green chemistry, atom economy, liquid-assisted grinding""",
        """[From "Asymmetric Catalysis with Chiral Complexes" - Noyori, Angew. Chem. 2002]

Chiral catalysts enable enantioselective synthesis. BINAP-Ru complexes for asymmetric hydrogenation of beta-keto esters.

Achieves >99% ee. Industrial applications including naproxen and menthol synthesis.

Key terms: asymmetric catalysis, enantioselective, BINAP, ruthenium, hydrogenation, enantiomeric excess""",
        """[From "RAFT Polymerization" - Chiefari et al., Macromolecules 1998]

RAFT enables controlled molecular weight and narrow dispersity. Dithioester chain transfer agents mediate radical polymerization.

Applicable to styrene, acrylates, acrylamides. Block copolymer synthesis with predictable molecular weight.

Key terms: RAFT polymerization, controlled radical polymerization, chain transfer agent, molecular weight control""",
        """[From "HPLC in Pharmaceutical Analysis" - Snyder, Kirkland & Dolan, Wiley 2010]

HPLC is the workhorse for pharmaceutical analysis. Reversed-phase C18 with gradient elution.

UV detection at 210-260 nm. Validate for specificity, linearity, accuracy, precision. ICH guidelines.

Key terms: HPLC, reversed-phase, C18 column, gradient elution, UV detection, pharmaceutical analysis, method validation""",
        """[From "Multidimensional NMR Spectroscopy" - Ernst, Bodenhausen & Wokaun, Oxford 1987]

2D NMR spreads peaks into two frequency dimensions. COSY, NOESY, HSQC, HMBC for structure elucidation.

HSQC correlates 1H with 13C. HMBC reveals long-range correlations. NOESY provides distance information.

Key terms: NMR spectroscopy, 2D NMR, COSY, NOESY, HSQC, HMBC, chemical shift, structure elucidation""",
        """[From "Self-Assembled Monolayers on Gold" - Ulman, Chem. Rev. 1996]

SAMs of alkanethiols on gold form well-ordered organic thin films. We review structure, kinetics, and applications.

SAMs control wettability, corrosion resistance, biocompatibility. Applications in biosensors and molecular electronics.

Key terms: self-assembled monolayer, alkanethiol, gold, surface modification, wettability, biosensor, molecular electronics""",
        """[From "Colloidal Quantum Dots: CdSe Synthesis" - Murray et al., JACS 1993]

CdSe nanocrystals with <5% size distribution using hot-injection in coordinating solvents.

Size controlled by reaction time and temperature. Size-dependent fluorescence from blue to red.

Key terms: CdSe, quantum dot, hot-injection, nanocrystal, size control, monodisperse, photoluminescence""",
        """[From "Enzyme Kinetics: Michaelis-Menten Model" - Segel, Wiley 1975]

Michaelis-Menten equation: v = Vmax[S]/(Km + [S]). Derived using steady-state assumption.

Km is substrate concentration at half-maximal velocity. Discuss competitive, uncompetitive, mixed inhibition.

Key terms: enzyme kinetics, Michaelis-Menten, Km, Vmax, steady-state, Lineweaver-Burk, inhibition""",
        """[From "Density Functional Theory" - Kohn & Sham, Phys. Rev. 1964]

We formulate DFT as a practical method for electronic structure calculations. Exchange-correlation as functional of electron density.

Kohn-Sham equations map to non-interacting particles. LDA provides simplest functional.

Key terms: density functional theory, Kohn-Sham, exchange-correlation, local density approximation, electronic structure""",
        """[From "PEM Fuel Cells: ORR Electrocatalysis" - Gasteiger et al., J. Power Sources 2005]

PEM fuel cells convert H2 and O2 to electricity. ORR at cathode is the performance-limiting step.

Pt/C with 3-5 nm particles: 0.2 A/mgPt mass activity. Degradation from Pt dissolution and carbon corrosion.

Key terms: PEM fuel cell, oxygen reduction reaction, platinum catalyst, Nafion membrane, mass activity""",
        """[From "Gold Nanoparticle Catalysis" - Hashmi & Hutchings, Angew. Chem. 2006]

Au NPs <5 nm on metal oxides show remarkable catalytic activity. Bulk gold is inert.

Au-Pd bimetallic NPs show synergistic effects in H2O2 synthesis. Size-dependent: 2-5 nm optimal.

Key terms: gold nanoparticle, size-dependent catalysis, CO oxidation, support interaction, bimetallic catalyst""",
        """[From "Antibody-Drug Conjugates" - Carter & Senter, Cancer Journal 2008]

ADCs combine antibody specificity with cytotoxic potency. Three components: antibody, payload, linker.

DAR 2-8. Cleavable linkers exploit endosomal pH, glutathione, cathepsin B. Brentuximab vedotin FDA-approved.

Key terms: antibody-drug conjugate, monoclonal antibody, cytotoxic payload, DAR, cleavable linker, cancer therapy""",
        """[From "Singlet Oxygen in Synthesis and PDT" - DeRosa, Coord. Chem. Rev. 2002]

Singlet oxygen generated via energy transfer from triplet sensitizers. Lifetime 2 micro-s to 700 micro-s.

[4+2] cycloaddition with dienes. In PDT, induces oxidative damage triggering cancer cell apoptosis.

Key terms: singlet oxygen, photosensitizer, energy transfer, cycloaddition, photodynamic therapy, Rose Bengal"""
    ],

    "物理": [
        """[From "Implementing the Quantum von Neumann Architecture with Superconducting Circuits" — Mariantoni et al., Science 2011]

The von Neumann architecture for a classical computer comprises a central processing unit and a memory holding instructions and data. We demonstrate a quantum central processing unit that exchanges data with a quantum random-access memory integrated on a chip, with instructions stored on a classical computer. We test our quantum machine by executing codes that involve seven quantum elements: two superconducting qubits coupled through a quantum bus, two quantum memories, and two zeroing registers.

The superconducting qubits employed in this work are of the transmon type, featuring a capacitively shunted Josephson junction that renders the qubit exponentially insensitive to charge noise while maintaining sufficient anharmonicity for fast gate operations. The qubit transition frequency is approximately 6 GHz, with anharmonicities (α/2π) of roughly 200–250 MHz, permitting microwave pulses of 10–20 ns duration to implement single-qubit gates with fidelities exceeding 99%. Two vital algorithms for quantum computing are demonstrated: the quantum Fourier transform (QFT), achieving 66% process fidelity, and the three-qubit Toffoli-class OR phase gate, with 98% phase fidelity.

Key terms: superconducting qubit, transmon, Josephson junction, anharmonicity, quantum bus, quantum Fourier transform (QFT), Toffoli gate, process fidelity, charge noise, quantum random-access memory (QRAM), coherence time (T1, T2), gate fidelity, microwave pulses, dispersive readout.""",
        """[From "Gravitational Waves from Binary Black Hole Mergers" - Abbott et al. (LIGO), PRL 2016]

On September 14, 2015, LIGO observed a gravitational-wave signal matching binary black hole inspiral and merger.

Source: 36 and 29 solar mass black holes merging to 62 solar masses, radiating 3 solar masses as gravitational waves.

Key terms: gravitational wave, LIGO, black hole merger, general relativity, interferometer, chirp mass, inspiral""",
        """[From "Quantum Entanglement and Bell Inequality" - Aspect, Dalibard & Roger, PRL 1982]

We test Bell inequality using time-varying analyzers for photon polarization correlations. Results violate Bell inequality by 5 sigma.

The experiment closes the locality loophole. Rules out local hidden variable theories.

Key terms: quantum entanglement, Bell inequality, EPR paradox, hidden variables, polarization correlation, photon pairs""",
        """[From "Bose-Einstein Condensation in Sodium Atoms" - Davis et al., PRL 1995]

We observe BEC in dilute sodium atoms. Magnetic trap confines atoms while evaporative cooling reaches 2 micro-K.

Below Tc, a sharp peak appears in velocity distribution. Condensate contains 2x10^6 atoms.

Key terms: Bose-Einstein condensation, ultracold atoms, evaporative cooling, magnetic trap, quantum degeneracy""",
        """[From "Topological Insulators and Topological Superconductors" - Bernevig, Princeton 2013]

Topological insulators are insulating in bulk with conducting surface states protected by time-reversal symmetry.

Surface states exhibit Dirac cone with spin-momentum locking. Verified by ARPES and transport measurements.

Key terms: topological insulator, surface state, Dirac cone, spin-momentum locking, Berry phase, ARPES""",
        """[From "Quantum Hall Effect in Graphene" - Novoselov et al., Nature 2005]

Graphene exhibits quantum Hall effect observable at room temperature. Half-integer QHE from relativistic Dirac fermions.

Hall conductivity quantized as sigma_xy = 4(n+1/2)e2/h. Anomalous sequence reflects Berry phase of pi.

Key terms: quantum Hall effect, graphene, Dirac fermion, Berry phase, half-integer quantization, Landau level""",
        """[From "Higgs Boson Observation at the LHC" - ATLAS & CMS, Phys. Lett. B 2012]

We observe a new particle at 125 GeV consistent with the Standard Model Higgs boson in multiple decay channels.

Combined significance exceeds 5 sigma. Measured cross section and branching ratios agree with Standard Model.

Key terms: Higgs boson, LHC, ATLAS, CMS, Standard Model, electroweak symmetry breaking, decay channel""",
        """[From "Dark Energy and the Accelerating Universe" - Riess et al., Astronomical J. 1998]

Type Ia supernova observations at z=0.16-0.62 show luminosity distances larger than expected in a decelerating universe.

Data favor Omega_M ~ 0.3 and Omega_Lambda ~ 0.7. Universe expansion is accelerating.

Key terms: dark energy, cosmological constant, Type Ia supernova, accelerating universe, redshift, Omega_Lambda""",
        """[From "Black Hole Thermodynamics and Hawking Radiation" - Hawking, Commun. Math. Phys. 1975]

Black holes emit thermal radiation due to quantum effects near the event horizon. Temperature inversely proportional to mass.

Entropy S = kB*c3*A/(4G*hbar) proportional to horizon area. Generalized second law preserved.

Key terms: Hawking radiation, black hole, event horizon, temperature, entropy, quantum gravity, information paradox""",
        """[From "Quantum Computing with Superconducting Qubits" - Devoret & Schoelkopf, Science 2013]

Superconducting qubits are artificial atoms from Josephson junctions coupled to microwave resonators.

Transmon achieves coherence times >100 microseconds. Two-qubit gate fidelity >99% with parametric coupling.

Key terms: superconducting qubit, transmon, Josephson junction, coherence time, two-qubit gate, surface code""",
        """[From "Quantum Simulation with Ultracold Atoms" - Bloch et al., Rev. Mod. Phys. 2008]

Ultracold atoms in optical lattices simulate condensed matter Hamiltonians. We review the superfluid-Mott insulator transition.

Single-site resolved imaging studies quantum magnetism and topological phases.

Key terms: quantum simulation, optical lattice, ultracold atoms, Bose-Hubbard, Mott insulator, superfluid""",
        """[From "Neutrino Oscillations and Mass" - Fukuda et al. (Super-K), PRL 1998]

Upward-going muon neutrinos are fewer than downward-going, indicating oscillation to tau neutrinos.

Data consistent with maximal mixing, Delta_m2 ~ 2.5x10^-3 eV2. Neutrinos have nonzero mass.

Key terms: neutrino oscillation, neutrino mass, atmospheric neutrino, muon neutrino, tau neutrino, mixing angle""",
        """[From "CMB and Inflation" - Planck Collaboration, A&A 2014]

Planck satellite observations of CMB are consistent with six-parameter LCDM model with unprecedented precision.

Spectral index ns = 0.965 supports inflation. Tensor-to-scalar ratio r < 0.11 constrains simple inflation models.

Key terms: cosmic microwave background, Planck satellite, cosmological parameters, LCDM, spectral index, inflation""",
        """[From "Quantum Error Correction and Fault-Tolerant QC" - Shor, Phys. Rev. A 1995]

Quantum error correction encodes logical qubits into multiple physical qubits. The 9-qubit Shor code corrects arbitrary single-qubit errors.

Threshold theorem: if error rate < ~10^-4, arbitrarily long quantum computation is possible.

Key terms: quantum error correction, fault tolerance, threshold theorem, stabilizer code, surface code, logical qubit""",
        """[From "Precision Measurement of Electron g-Factor" - Hanneke et al., PRL 2008]

We measure electron magnetic moment to 0.28 parts per trillion using a single electron in a Penning trap.

g/2 = 1.00115965218073, agreeing with QED to 10 significant figures. Most precise QED test.

Key terms: electron magnetic moment, g-factor, Penning trap, quantum electrodynamics, precision measurement""",
        """[From "BEC of Exciton-Polaritons" - Kasprzak et al., Nature 2006]

We observe BEC of exciton-polaritons in semiconductor microcavity. Polaritons are hybrid light-matter quasiparticles.

Condensation above 10K. Long-range spatial coherence and spontaneous polarization observed.

Key terms: exciton-polariton, Bose-Einstein condensation, semiconductor microcavity, polariton lasing, coherence""",
        """[From "Quantum Teleportation" - Bouwmeester et al., Nature 1997]

We realize quantum teleportation of a photon. Quantum state transferred to distant photon using entanglement and classical communication.

Fidelity 0.80 +/- 0.05. Original state destroyed per no-cloning theorem.

Key terms: quantum teleportation, entanglement, Bell state measurement, no-cloning theorem, quantum communication""",
        """[From "Higgs Boson Decay to Fermions" - Chatrchyan et al. (CMS), PLB 2014]

First observation of Higgs decaying to bottom quarks and tau leptons using full LHC Run 1 data.

Signal strength H->bb: 1.0 +/- 0.2, H->tau tau: 1.1 +/- 0.2. Confirms Higgs mechanism generates fermion masses.

Key terms: Higgs boson, fermion decay, bottom quark, tau lepton, LHC, CMS, Yukawa coupling""",
        """[From "AdS/CFT and the Information Paradox" - Maldacena, IJTP 2003]

AdS/CFT correspondence provides non-perturbative quantum gravity in anti-de Sitter space. Holographic duality relates string theory to CFT.

Resolves information paradox by encoding information in boundary correlations. Ryu-Takayanagi formula relates entropy to minimal surfaces.

Key terms: AdS/CFT, holographic principle, quantum gravity, information paradox, string theory, entanglement entropy""",
        """[From "Quantum Sensing with NV Centers in Diamond" - Degen et al., Rev. Mod. Phys. 2017]

NV centers in diamond are point defects with optically readable electron spin states at room temperature.

DC magnetic sensitivity 1 micro-T/root-Hz with nanometer spatial resolution. Applications in neural activity imaging.

Key terms: nitrogen-vacancy center, diamond, quantum sensing, magnetic field, optical readout, nanoscale""",
        """[From "Quantum Simulation of Lattice Gauge Theories" - Martinez et al., Nature 2016]

We use trapped-ion quantum simulator to study the Schwinger model, a 1+1D QED.

We observe real-time dynamics of string breaking and pair creation. Probes topological theta-vacuum structure.

Key terms: quantum simulation, lattice gauge theory, Schwinger model, trapped ion, string breaking, pair creation"""
    ],

    "数学": [
        """[From "Optimal Transport: Old and New" — Villani, Grundlehren der mathematischen Wissenschaften 2009]

The Monge-Kantorovich optimal transport problem seeks the most economical way to transport a probability measure μ onto another probability measure ν, with respect to a given cost function c(x, y). In its modern formulation, one minimizes the functional ∫_{X×Y} c(x, y) dπ(x, y) over all probability measures π on the product space X×Y having μ and ν as marginals—the so-called transport plans. Under mild regularity conditions on the cost function (notably the twist condition), the optimal transport plan is unique and induced by a mapping T: X → Y, known as the Brenier map in the quadratic cost case, which is the gradient of a convex function.

The interplay between optimal transport and partial differential equations manifests most elegantly through the Wasserstein gradient flow formulation. Specifically, the Fokker-Planck equation describing the evolution of a probability density under Brownian motion can be reinterpreted as the gradient flow of the Boltzmann entropy functional with respect to the Wasserstein metric. Entropic regularization, pioneered by Cuturi (2013), replaces the linear programming formulation with a strictly convex problem solvable via Sinkhorn iterations, achieving O(N²) complexity and enabling large-scale machine learning applications including domain adaptation and generative modeling.

Key terms: Monge-Kantorovich, probability measure, marginal, transport plan, Brenier map, Wasserstein metric, gradient flow, Fokker-Planck equation, Boltzmann entropy, entropic regularization, Sinkhorn iterations, twist condition, convex function, domain adaptation.""",
        """[From "Fermat Last Theorem" - Wiles, Annals of Mathematics 1995]

Fermat Last Theorem: no positive integers satisfy a^n+b^n=c^n for n>2. Taniyama-Shimura conjecture connects elliptic curves to modular forms.

Wiles proved modularity for semistable elliptic curves using Galois deformations and Taylor-Wiles patching.

Key terms: Fermat Last Theorem, elliptic curves, modular forms, Galois representations, deformation ring, Taylor-Wiles patching""",
        """[From "The Entropy Formula for Ricci Flow" - Perelman, arXiv:math/0211159, 2002]

Poincare conjecture: every simply connected closed 3-manifold is homeomorphic to S3.

Perelman introduced W-entropy functional on Ricci flow solutions. Monotonicity formula enabled complete surgery procedure.

Key terms: Ricci flow, entropy functional, three-manifold, singularity formation, surgery procedure, Poincare conjecture""",
        """[From "Universal Approximation by Neural Networks" - Hornik et al., Neural Networks 1989]

A feedforward network with single hidden layer can approximate any continuous function on compact subsets of Rn.

Applies to sigmoid, tanh, and ReLU activations. We discuss width, depth, and approximation error.

Key terms: universal approximation, feedforward network, hidden layer, activation function, continuous function""",
        """[From "Compressed Sensing" - Candes & Tao, IEEE Trans. Info. Theory 2006]

Sparse signals can be recovered from far fewer samples than Nyquist theorem requires. RIP guarantees exact recovery via L1 minimization.

Random matrices satisfy RIP. O(k log(n/k)) Gaussian measurements suffice for k-sparse signals.

Key terms: compressed sensing, sparsity, restricted isometry property, L1 minimization, random matrix, MRI""",
        """[From "Stochastic Differential Equations" - Oksendal, Springer 2003]

Theory of SDEs driven by Brownian motion. Ito integral and Ito formula are fundamental tools.

We derive Black-Scholes equation for option pricing. Existence and uniqueness theorems proved.

Key terms: stochastic differential equation, Brownian motion, Ito integral, Ito formula, Black-Scholes, martingale""",
        """[From "Fourier Analysis on Number Fields" - Ramakrishnan & Williams, Springer 2000]

Fourier analysis on locally compact abelian groups with applications to number theory.

Applied to Riemann zeta function and L-functions. Functional equation from Poisson summation.

Key terms: Fourier analysis, Pontryagin duality, Plancherel theorem, Riemann zeta function, L-function, Poisson summation""",
        """[From "Algebraic Geometry" - Hartshorne, Springer 1977]

Scheme-theoretic algebraic geometry using commutative algebra. A scheme is a locally ringed space.

Riemann-Roch theorem computes dimension of global sections. Serre duality relates cohomology groups.

Key terms: algebraic geometry, scheme, spectrum, commutative algebra, cohomology, Riemann-Roch, Serre duality""",
        """[From "Nonlinear Partial Differential Equations" - Evans, AMS 1998]

Theory of nonlinear PDEs including Hamilton-Jacobi, conservation laws, elliptic regularity.

Viscosity solution framework for non-smooth solutions. Schauder fixed point theorem for existence.

Key terms: nonlinear PDE, Hamilton-Jacobi, viscosity solution, conservation law, Sobolev space, weak solution""",
        """[From "Random Matrix Theory" - Mehta, Academic Press 2004]

Statistical properties of eigenvalues of large random matrices. Wigner semicircle law describes bulk distribution.

Level spacing statistics are universal. Tracy-Widom distribution describes largest eigenvalue fluctuations.

Key terms: random matrix, eigenvalue, Wigner semicircle, level spacing, Tracy-Widom, universality, Gaussian ensemble""",
        """[From "Geometric Measure Theory" - Federer, AMS 1969]

Currents generalize oriented surfaces and boundaries. Rectifiable currents for minimal surfaces and variational problems.

Compactness theorem proves existence of area-minimizing surfaces. Applications to Plateau problem.

Key terms: geometric measure theory, current, rectifiable, minimal surface, area-minimizing, compactness, Plateau problem""",
        """[From "Harmonic Analysis" - Stein, Princeton 1993]

Modern harmonic analysis including Littlewood-Paley theory, singular integrals, Hardy spaces.

Calderon-Zygmund decomposition for singular integral operators. H1-BMO duality and John-Nirenberg inequality.

Key terms: harmonic analysis, singular integral, Calderon-Zygmund, Hardy space, BMO, Littlewood-Paley, wavelet""",
        """[From "Ergodic Theory" - Walters, Springer 1982]

Long-term average behavior of dynamical systems. Birkhoff ergodic theorem: time averages converge to space averages.

Ergodic decomposition theorem characterizes invariant measures. Applications in statistical mechanics.

Key terms: ergodic theory, Birkhoff theorem, mixing, entropy, invariant measure, variational principle, dynamical system""",
        """[From "Differential Geometry of Curves and Surfaces" - Do Carmo, Prentice Hall 1976]

Differential geometry in R3. Frenet-Serret formulas describe local geometry of curves.

Gauss-Bonnet theorem relates total curvature to topology. Theorema Egregium: Gaussian curvature is intrinsic.

Key terms: differential geometry, curvature, Frenet-Serret, Gauss-Bonnet, Gaussian curvature, geodesic, intrinsic""",
        """[From "Probability Theory" - Chow & Teicher, Springer 1978]

Measure-theoretic probability. Kolmogorov extension theorem for infinite product spaces.

Martingale convergence theorem and optional stopping theorem. Applications in random walks and finance.

Key terms: probability theory, measure theory, Kolmogorov extension, martingale, convergence theorem, conditional expectation""",
        """[From "Graph Theory" - Diestel, Springer 2000]

Theory of finite and infinite graphs: connectivity, coloring, planarity. Menger theorem, max-flow min-cut, Hall marriage.

Graph minors, Robertson-Seymour theorem, four-color theorem. Ramsey theory studies order in large structures.

Key terms: graph theory, connectivity, coloring, planarity, Menger theorem, Ramsey theory, graph minor""",
        """[From "Numerical Linear Algebra" - Trefethen & Bau, SIAM 1997]

Algorithms for matrix computations: LU, QR, SVD. Conditioning and backward stability are central.

Iterative methods: Jacobi, Gauss-Seidel, conjugate gradient. QR algorithm for eigenvalues with cubic convergence.

Key terms: numerical linear algebra, LU decomposition, QR algorithm, SVD, conditioning, conjugate gradient""",
        """[From "Algebraic Topology" - Hatcher, Cambridge 2002]

Fundamental group, covering spaces, homology theory. Seifert-van Kampen theorem computes fundamental groups.

Mayer-Vietoris sequence and excision theorem. Applications to Brouwer fixed point and Jordan curve theorems.

Key terms: algebraic topology, fundamental group, homology, cohomology, Seifert-van Kampen, Mayer-Vietoris, Poincare duality""",
        """[From "PDEs and Boundary Value Problems" - Haberman, SIAM 2012]

Classical PDEs: heat, wave, Laplace equations via separation of variables and Fourier series.

Sturm-Liouville theory provides eigenfunction expansions. Green functions for integral representations.

Key terms: PDE, heat equation, wave equation, Laplace equation, separation of variables, Fourier series, Green function""",
        """[From "Mathematical Statistics" - Bickel & Doksum, Prentice Hall 2001]

Statistical inference: point estimation, hypothesis testing, confidence intervals. Neyman-Pearson lemma for most powerful tests.

MLEs are asymptotically efficient. Delta method derives asymptotic distributions. Bayesian inference and decision theory.

Key terms: mathematical statistics, maximum likelihood, Neyman-Pearson, hypothesis testing, confidence interval, delta method"""
    ],

    "经管": [
        """[From "Platform Competition in Two-Sided Markets" — Rochet & Tirole, Journal of the European Economic Association 2003]

Many if not most markets with network externalities are two-sided. To succeed, platforms in industries such as software, portals and media, payment systems, and the Internet must court both sides of the market. This paper builds a model of platform competition with two-sided markets, elucidating the determinants of price allocation and end-user surplus for different governance structures.

A two-sided market is characterized by the presence of indirect network externalities: the value that an end-user on one side derives from the platform depends on the number of end-users on the other side. The price structure—the decomposition of the total price between the two sides—matters because the platform must bring both sides on board. The optimal pricing structure is governed by a modified Lerner formula that accounts for the positive feedback loop between the two sides. Under certain conditions—specifically when the elasticity of demand on one side is sufficiently low relative to the strength of the cross-side network effect—the platform may rationally choose to subsidize that side below marginal cost (or even offer negative prices) while extracting surplus from the other side. This pricing pattern, known as divide-and-conquer or loss-leader strategy, is pervasive in the digital economy.

Key terms: two-sided market, network externality, indirect network effect, cross-side effect, price structure, Lerner formula, marginal cost, subsidy, elasticity of demand, divide-and-conquer, loss-leader, platform governance, end-user surplus, multi-homing, competitive bottleneck.""",
        """[From "The Market for Lemons" - Akerlof, QJE 1970]

Information asymmetry between buyers and sellers can cause market failure. In used cars, sellers know more about quality.

Adverse selection drives out high-quality cars. Solutions: warranties, certification, reputation mechanisms.

Key terms: information asymmetry, adverse selection, market for lemons, quality uncertainty, warranty, signaling""",
        """[From "Prospect Theory: Decision under Risk" - Kahneman & Tversky, Econometrica 1979]

Prospect theory as alternative to expected utility. People evaluate outcomes relative to a reference point.

Loss aversion: losses loom larger than equivalent gains. Probability weighting overweights small probabilities.

Key terms: prospect theory, loss aversion, reference point, probability weighting, framing effect, cognitive bias""",
        """[From "Optimal Capital Structure" - Modigliani & Miller, AER 1958]

In perfect capital markets, firm value is independent of capital structure. Total cash flow to investors is the same.

With taxes, debt provides tax shield. Trade-off theory balances tax benefits against bankruptcy costs.

Key terms: capital structure, Modigliani-Miller, tax shield, trade-off theory, pecking order, debt-equity ratio""",
        """[From "The Capital Asset Pricing Model" - Sharpe, J. Finance 1964]

CAPM relates expected return to systematic risk (beta). Security market line: E(Ri) = Rf + beta_i*(E(Rm) - Rf).

Derived from mean-variance portfolio theory. Only systematic risk is priced.

Key terms: CAPM, beta, systematic risk, security market line, expected return, risk premium, Sharpe ratio""",
        """[From "The Efficient Market Hypothesis" - Fama, J. Finance 1970]

An efficient market fully reflects available information. Three forms: weak, semi-strong, strong.

Empirical evidence supports weak and semi-strong efficiency. Anomalies including momentum challenge the hypothesis.

Key terms: efficient market hypothesis, weak form, semi-strong form, strong form, random walk, anomaly, momentum""",
        """[From "Options Pricing: Black-Scholes Model" - Black & Scholes, JPE 1973]

We derive a formula for European call and put option prices. Black-Scholes PDE relates option price to stock price, volatility, time.

Formula: C = S*N(d1) - K*e^(-rT)*N(d2). Construct risk-free portfolio by dynamic hedging.

Key terms: Black-Scholes, option pricing, call option, volatility, delta hedging, risk-neutral valuation, European option""",
        """[From "Agency Theory: Principal-Agent Relationships" - Jensen & Meckling, JFE 1976]

Agency relationship: one party engages another for decision-making. Agency costs from divergent interests.

Monitoring and bonding costs reduce but do not eliminate agency problems. Stock compensation aligns interests.

Key terms: agency theory, principal-agent, agency cost, monitoring, moral hazard, corporate governance, stock compensation""",
        """[From "Game Theory and Economic Behavior" - von Neumann & Morgenstern, Princeton 1944]

Game theory as mathematical framework for strategic interactions. Games have players, strategies, payoffs.

Minimax theorem for two-player zero-sum games. Nash equilibrium: no player can improve by unilateral deviation.

Key terms: game theory, Nash equilibrium, minimax, zero-sum game, strategy, payoff matrix, auction""",
        """[From "Asymmetric Information in Insurance" - Rothschild & Stiglitz, QJE 1976]

Insurance markets with private information about risk type. High-risk prefer full insurance, low-risk prefer partial.

Separating equilibrium: different types choose different contracts. Market may not provide efficient risk sharing.

Key terms: insurance, asymmetric information, adverse selection, screening, separating equilibrium, risk type""",
        """[From "Endogenous Growth Theory" - Romer, JPE 1990]

Endogenous technological change driven by intentional R&D investment. Long-run growth determined by economic incentives.

Increasing returns in ideas sector lead to sustained growth. Government policy affects growth rates.

Key terms: endogenous growth, R&D investment, technological change, increasing returns, knowledge spillover, innovation policy""",
        """[From "Behavioral Finance: Limits of Arbitrage" - Shleifer & Vishny, J. Finance 1997]

Professional arbitrageurs may fail to correct mispricing. Noise trader risk and fundamental limit arbitrage.

Arbitrage is risky, limited, costly. Short-term performance evaluation constrains arbitrageurs.

Key terms: behavioral finance, limits of arbitrage, noise trader, fundamental risk, mispricing, bubble, crash""",
        """[From "Real Options and Investment Under Uncertainty" - Dixit & Pindyck, Princeton 1994]

Option pricing theory applied to irreversible investment. Option to wait has value because uncertainty may resolve favorably.

Investment triggers higher than NPV suggests. Analogous to exercising American call option.

Key terms: real options, irreversible investment, uncertainty, option to wait, NPV, investment trigger, flexibility""",
        """[From "Social Capital and Economic Performance" - Putnam, Princeton 1993]

Social capital: features of social organization including trust, norms, networks that improve cooperation.

Regions with stronger civic traditions have better institutions. Trust reduces transaction costs.

Key terms: social capital, trust, civic engagement, networks, institutional performance, cooperation, norms""",
        """[From "The Theory of the Firm" - Coase, Economica 1937]

Firms exist as alternative to market transactions. Transaction costs determine whether production is within firms or markets.

Firms expand until internal organization cost equals market transaction cost.

Key terms: theory of the firm, transaction cost, Coase theorem, market vs. hierarchy, property rights, coordination""",
        """[From "Auction Theory and Design" - Milgrom, Princeton 2004]

We analyze first-price, second-price (Vickrey), English, Dutch auctions. Revenue equivalence theorem.

Optimal auction design depends on valuations and information. Common value auctions and winner curse.

Key terms: auction theory, Vickrey auction, revenue equivalence, winner curse, optimal auction, spectrum auction, bidding""",
        """[From "New Trade Theory" - Krugman, JPE 1980]

Trade based on increasing returns and product differentiation. Trade arises even between identical countries.

Intra-industry trade dominates among developed nations. Home market effect predicts export patterns.

Key terms: new trade theory, increasing returns, product differentiation, intra-industry trade, home market effect""",
        """[From "Natural Experiments in Economics" - Angrist & Pischke, Princeton 2009]

Instrumental variables and natural experiments for causal inference. Regression discontinuity exploits arbitrary thresholds.

Difference-in-differences for policy evaluation. Credibility revolution emphasizes research design.

Key terms: natural experiment, instrumental variable, regression discontinuity, difference-in-differences, causal inference""",
        """[From "Market Microstructure" - O'Hara, Blackwell 1995]

Process and outcomes of exchanging assets under explicit trading rules. How information is incorporated into prices.

Bid-ask spreads compensate for inventory risk and adverse selection. High-frequency trading transformed market structure.

Key terms: market microstructure, bid-ask spread, market maker, limit order, adverse selection, price discovery, liquidity""",
        """[From "Corporate Governance and Firm Performance" - La Porta et al., J. Finance 2000]

Legal protection of investor rights affects corporate governance and firm valuation. Stronger protection means more developed capital markets.

Common law countries provide stronger investor protection than civil law. Tunneling prevalent where protections are weak.

Key terms: corporate governance, investor protection, legal origin, common law, civil law, tunneling, agency cost"""
    ],
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
            "basics": "下面考你基础概念，每题60秒。我看看你本科到底有没有在学。",
            "core_knowledge": "给你一个实际场景，3分钟。让我看看你是真有料还是只会背书。",
            "english": "一段文献，5分钟阅读加翻译。开始。",
            "quality": "最后几个问题，每题90秒。希望你坦诚。别说套话。",
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
            "self_intro_cn": "首先请你用中文做一下自我介绍，90秒。请重点突出你的学术背景和研究兴趣。",
            "self_intro_en": "接下来请你用英文做一下自我介绍。Please introduce yourself in English. You have 90 seconds.",
            "project": "请详细介绍一个你最有代表性的项目，2分钟。包括背景、你的角色、技术方案和成果。",
            "principle": "请深入解释你项目中核心技术或方法的底层原理，90秒。",
            "basics": "接下来我会考察你的专业基础知识，每题60秒限时回答。准备好了吗？",
            "core_knowledge": "下面是一个开放性的专业问题，没有标准答案，给你3分钟展开分析。",
            "english": "请翻译以下这段英文文献原文。你将有5分钟时间阅读和翻译。",
            "quality": "最后我想了解一些你的个人特质和综合素质，每题90秒。",
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
            "self_intro_cn": "首先请你用中文介绍一下自己，90秒左右。不用紧张，就像跟朋友介绍自己一样自然就好。可以聊聊你的背景、兴趣，以及为什么想来这个夏令营。",
            "self_intro_en": "接下来我们用英文简单聊几句，90秒。不用追求完美，大胆说就行。Could you tell me a bit about yourself in English?",
            "project": "我看到你在材料里提到了几个很有意思的项目。能挑一个你觉得最有意思的，用2分钟左右跟我聊聊吗？就像讲故事一样，说说你是怎么参与进去的，做了什么，有什么收获。",
            "principle": "你刚才提到的技术很有意思。我其实也挺好奇的——它是怎么工作的呢？用90秒左右给我讲讲，就当我是外行。能把复杂的东西讲简单，才是真懂了。",
            "basics": "接下来我想和你一起过几个专业基础概念，每题60秒。会就答，不会就说不会，我们一起看看哪些地方还可以加强。",
            "core_knowledge": "接下来我想跟你聊一个开放性的问题，给你3分钟。没有唯一正确的答案，我感兴趣的是你思考的过程。",
            "english": "我们来试一小段英文文献的翻译，你有5分钟。不用追求完美，大意准确就行。生词可以猜，或者根据上下文推断。",
            "quality": "技术方面的我们都聊完了。最后这段时间我想了解一下你这个人——你的故事、你的想法、你对未来的期待。每题90秒，就是朋友间的聊天。",
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
