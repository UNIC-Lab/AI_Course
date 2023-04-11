# 联邦学习进阶
## 一. 联邦学习基础概念理解
联邦学习（Federated Learning）最初由Google的研究科学家Bonawitz等人在2016年提出，其旨在通过在设备上进行本地训练，并仅将更新的模型参数聚合起来，从而在不公开任何个人数据的情况下进行机器学习。

联邦学习的起源可以追溯到分散式学习（Decentralized Learning），分散式学习是在不同设备上训练模型并协作学习的过程，其中每个设备都拥有自己的本地数据集。然而，在分散式学习中，设备之间通常需要交换数据和模型，这可能导致隐私和安全问题。

因此，联邦学习被提出来解决这些问题，它通过让设备在本地训练模型，将更新的模型参数上传到云端进行聚合，从而保护个人隐私和数据安全。自从提出后，联邦学习已经被广泛应用于各种场景，如医疗、金融、智能交通等领域。

联邦学习的特点：
1.各方数据都保留在本地，不泄露隐私也不违反法规。

2.多个参与者联合数据建立虚拟的公有模型，并且共同获益的体系。

3.在联邦学习的体系下，各个参与者的身份和地位平等。

4.联邦学习的建模效果和将整个数据放在一处建模的效果相同，或相差不大（在各个数据的用户对齐（user alignment）或特征对齐（feature alignment）的条件下）
迁移学习是在用户或特征不对齐的情况下，也可以在数据间通过交换加密参数达到知识迁移的效果。

5.联邦学习使多个参与方在保护数据隐私、满足合法合规要求的前提下继续进行机器学习，解决数据孤岛问题。
## 二.联邦学习的学习路径
1.机器学习基础知识：在学习联邦学习之前，需要具备一定的机器学习基础知识，包括监督学习、无监督学习、深度学习等。

2.分布式系统基础知识：联邦学习是一种分散式学习方法，需要一定的分布式系统基础知识，如分布式计算、分布式数据库、分布式文件系统等。

3.隐私保护：联邦学习涉及到多个参与者之间的数据共享，因此需要对数据进行隐私保护。需要学习隐私保护的基本概念和技术，如差分隐私、同态加密、多方计算等。

4.联邦学习框架：学习联邦学习框架，如Google的Federated Learning框架、PyTorch的PySyft框架等。
## 三.联邦学习相关论文分类汇总
开坑论文：Communication-Efficient Learning of Deep Networks from Decentralized Data

综述：
Advances and Open Problems in Federated Learning

Federated machine learning: Concept and applications

联邦学习算法与通信优化：
Privacy-Preserving Deep Learning

Agnostic Federated Learning

Bayesian Nonparametric Federated Learning of Neural Networks

Federated learning with matched averaging (该文内容基于上面一篇文章的工作)

Federated learning: Strategies for improving communication efficiency

Federated multi-task learning

Federated optimization in heterogeneous networks

Fair resource allocation in federated learning （与上面一篇同作者）

Communication-Efficient Federated Learning with Sketching

FedBoost: Communication-Efficient Algorithms for Federated Learning

Federated Learning with Only Positive Labels

Scaffold: Stochastic controlled averaging for federated learning

Federated Meta-Learning for Fraudulent Credit Card Detection

Federated Learning with Communication Delay in Edge Networks

FLFE: A Communication-Efficient and Privacy-Preserving Federated Feature Engineering Framework

联邦元学习：
Federated learning with personalization layers

Improving federated learning personalization via model agnostic meta learning

联邦学习安全
Deep models under the GAN: information leakage from collaborative deep learning

How to backdoor federated learning

Quantification of the Leakage in Federated Learning

Analyzing federated learning through an adversarial lens

Deep leakage from gradients

联邦学习公平与贡献评估
A Multi-player Game for Studying Federated Learning Incentive Schemes

A Real-time Contribution Measurement Method for Participants in Federated Learning

Collaborative Fairness in Federated Learning

Hierarchically Fair Federated Learning

Incentive design for efficient federated learning in mobile networks: A contract theory approach

Measure contribution of participants in federated learning

Profit Allocation for Federated Learning

Interpret federated learning with shapley values

联邦学习与计算机视觉
Federated Learning for Vision-and-Language Grounding Problems.

Performance Optimization for Federated Person Re-identification via Benchmark Analysis

联邦学习与推荐系统
FedFast: Going Beyond Average for Faster Training of Federated Recommender Systems

Non-iid
On the convergence of fedavg on non-iid data

From Online to Non-iid Batch Learning

数据集
Real-world image datasets for federated learning

## 四.联邦学习与现有研究的关系
### 联邦学习与差分隐私理论的区别
联邦学习的特点使其可以被用来保护用户数据的隐私，但是它和大数据、数据挖掘领域中常用的隐私保护理论如差分隐私保护理论（Differential Privacy）、k 匿名（k-Anonymity）和 Ι 多样化（I-Diversity）等方法还是有较大的差别的。首先联邦学习与传统隐私保护方法的原理不同，联邦学习通过加密机制下的参数交换方式保护用户数据隐私，加密手段包括同态加密等。与Differential Privacy 不同，其数据和模型本身不会进行传输，因此在数据层面上不存在泄露的可能，也不违反更严格的数据保护法案如GDPR等。而差分隐私理论、k 匿名和I多样化等方法是通过在数据里加噪音，或者采用概括化的方法模糊某些敏感属性，直到第三方不能区分个体为止，从而以较高的概率使数据无法被还原，以此来保护用户隐私。但是，从本质上来说这些方法还是进行了原始数据的传输，存在着潜在被攻击的可能性，并且在GDPR等更严格的数据保护法案下这种数据隐私的保护方式可能不再适用。与之对应的，联邦学习是对用户数据隐私保护更为有力的手段。

### 联邦学习与分布式机器学习的区别
横向联邦学习中多方联合训练的方式与分布式机器学习（Distributed Machine Learning）有部分相似的地方。分布式机器学习涵盖了多个方面，包括把机器学习中的训练数据分布式存储、计算任务分布式运行、模型结果分布式发布等，参数服务器（Parameter Server） IP）是分布式机器学习中一个典型的例子。参数服务器作为加速机器学习模型训练过程的一种工具，它将数据存储在分布式的工作节点上，通过一个中心式的调度节点调配数据分布和分配计算资源，以便更高效的获得最终的训练模型。而对于联邦学习而言，首先在于横向联邦学习中的工作节点代表的是模型训练的数据拥有方，其对本地的数据具有完全的自治权限，可以自主决定何时加入联邦学习进行建模，相对地在参数服务器中，中心节点始终占据着主导地位，因此联邦学习面对的是一个更复杂的学习环境；其次，联邦学习则强调模型训练过程中对数据拥有方的数据隐私保护，是一种应对数据隐私保护的有效措施，能够更好地应对未来愈加严格的数据隐私和数据安全监管环境。

### 联邦学习与联邦数据库的关系
联邦数据库系统（Federated Database System）是将多个不同的单元数据库进行集成，并对集成后的整体进行管理的系统。它的提出是为了实现对多个独立的数据库进行相互操作。联邦数据库系统对单元数据库往往采用分布式存储的方式，并且在实际中各个单元数据库中的数据是异构的，因此，它和联邦学习在数据的类型与存储方式上有很多相似之处。但是，联邦数据库系统在各个单元数据库交互的过程中不涉及任何隐私保护机制，所有单元数据库对管理系统都是完全可见的。此外，联邦数据库系统的工作重心在包括插入、删除、查找、合并等各种数据库基本操作上面，而联邦学习的目的是在保护数据隐私的前提下对各个数据建立一个联合模型，使数据中蕴含的各种模式与规律更好地为我们服务。

### 联邦学习与区块链的关系
区块链是一个基于密码学安全的分布式账本，其方便验证，不可篡改。区块链 2.0是一个去中心化的应用，通过使用开源的代码及分布式的存储和运行，保证极高的透明度和安全性，使数据不会被篡改。区块链的典型应用包括比特币（BTC）、以太坊（ETH）等。区块链与联邦学习都是一种去中心化的网络，区块链是一种完全P2P （peer to peer）的网络结构，在联邦学习中，第三方会承担汇聚模型、管理等功能。联邦学习与区块链中，均涉及到密码学、加密算法等基础技术。根据技术的不同，区块链技术使用的加密算法包括哈希算法，非对称加密等；联邦学习中使用同态加密等。从数据角度上看，区块链上通过加密的方式在各个节点上记录了完整的数据，而联邦学习中，各方的数据均仅保留在本地。从奖励机制上看，区块链中，不同节点之间通过竞争记账来获得奖励；在联邦学习中，多个参与方通过共同学习，提高模型训练结果，依据每一方的贡献来分配奖励。

### 联邦学习与多方安全计算的关系
在联邦学习中，用户的隐私与安全是重中之重。为了保护用户隐私，防止联邦学习应用被恶意方攻击，多方安全计算技术可以在联邦学习中被应用，成为联邦学习技术框架中的一部分。学术界已经展开利用多方安全计算来增强联邦学习的安全性的研究。McMahan 指出，联邦学习可以通过差分隐私，多方安全计算，或它们的结合等技术来提供更强的安全保障。Bonawitz指出，联邦学习中，可以利用多方安全计算以安全的方式计算来自用户设备的模型参数更新的总和。Truex中提出了一种利用差分隐私和多方安全计算来保护隐私的联邦学习方法。Liu提出将加性同态加密（AHE）应用于神经网络的多方计算。微众银行提出的开源联邦学习框架FATE 中包含了多方安全计算的相关算子，方便应用方对多方安全计算进行高效的开发。
## 五.联邦学习的分类
### 横向联邦学习
在两个数据集的用户特征重叠较多而用户重叠较少的情况下，我们把数据集按照横向（即用户维度）切分，并取出双方用户特征相同而用户不完全相同的那部分数据进行训练。这种方法叫做横向联邦学习。比如有两家不同地区银行，它们的用户群体分别来自各自所在的地区，相互的交集很小。但是，它们的业务很相似，因此，记录的用户特征是相同的。此时，就可以使用横向联邦学习来构建联合模型。Google在2017年提出了一个针对安卓手机横型更新的数据联合建模方案；在单个用户使用安卓手机时，不断在本地更新模型参数并将参数上传到安卓云上，从而使特征维度相同的各数据拥有方建立联合模型的一种联邦学习方案。
### 纵向联邦学习
在两个数据集的用户重叠较多而用户特征重叠较少的情况下，我们把数据集按照纵向（即特征维度）切分，并取出双方用户相同而用户特征不完全相同的那部分数据进行训练。这种方法叫做纵向联邦学习。比如有两个不同机构，一家是某地的银行，另一家是同一个地方的电商。它们的用户群体很有可能包含该地的大部分居民，因此用户的交集较大。但是，由于银行记录的都是用户的收支行为与信用评级，而电商则保有用户的浏览与购买历史，因此它们的用户特征交集较小。纵向联邦学习就是将这些不同特征在加密的状态下加以聚合，以增强模型能力的联邦学习。目前，逻辑回归模型，树型结构模型和神经网络模型等众多机器学习模型已经逐渐被证实能够建立在这个联邦体系上
### 联邦迁移学习
在两个数据集的用户与用户特征重叠都较少的情况下，我们不对数据进行切分，而可以利用迁移学习来克服数据或标签不足的情况，这种方法叫作联邦迁移学习。
比如有两个不同机构，一家是位于中国的银行，另一家是位于美国的电商。由于受到地域限制，这两家机构的用户群体交集很小。同时，由于机构类型的不同，二者的数据特征也只有小部分重合。在这种情况下，要想进行有效的联邦学习，就必须引入迁移学习，来解决单边数据规模小和标签样本少的问题，从而提升模型的效果。
## 六.未来研究方向
将其他的技术引入联邦学习之中，从而有效解决联邦学习安全性，有效性的问题。
