# ***基础知识速通指南***
## *一、数学基础*
### 1.1 需掌握的基本能力
* 线性代数：了解矩阵、向量、行列式、特征值等基本概念

* 微积分：了解导数、偏导数、极值等基本概念

* 概率论与统计学：了解概率、条件概率、期望、方差等基本概念
## *二、编程基础（1 Week）*
### 2.1 需掌握的基本能力
- Python基础：了解Python基本语法、掌握基本数据类型、条件语句、循环语句、函数、列表、字典等
- Python需要了解的知识点及参考资料：
  - **编程环境配置**：IDE工具：vscode(简洁、可玩性高、可扩展性强)、pycharm(开发工具更多、更专业、且集成了环境管理工具)、JupyterNotbook(基于Web，基于ipython，支持markdown)，版本：Python3.4-Python3.10。初学可尝试使用JupyterNotebook，逻辑性较强；一般性实验推荐VScode，项目开发推荐Pycharm。
  - **基础语法知识点**：基本环境、变量和数据类型、列表、if判断、字典、标准输入输出、while循环、函数、类、文件、异常等。这些是保证能写出完整代码的必要保证。
  - **必要的工具库**：[Numpy（基础且通用的库，处理n维array）](https://github.com/lijin-THU/notes-python/blob/master/03-numpy/03.01-numpy-overview.ipynb)、[matplotlib(python绘图基础)](https://github.com/lijin-THU/notes-python/blob/master/03-numpy/03.02-matplotlib-basics.ipynb)等。
  - **环境管理**：推荐conda([使用指南](https://zhuanlan.zhihu.com/p/44398592))
### 2.2 学习资源
* 书籍：《Python基础教程》（廖雪峰）、《python编程：从入门到实战》（埃里克 • 马瑟斯）

* 文档：[Python3官方中文文档](https://docs.pythontab.com/python/python3.4/)

* 视频课程：[《Python零基础教程》](https://www.bilibili.com/video/BV1qW4y1a7fU/?spm_id_from=333.337.search-card.all.click)
* 说明：参照《Python编程：从入门到实战》Chapter1-Chapter11可快速入门，numpy和matplotlib需要掌握基本的使用方法，可阅读官方文档或者相关博客，学习过程中以实践为主。视频课程资料可参考B站黑马程序员。环境安装、配置等问题能问就问，尽量不要纯自己踩坑，费时且无用。
## *三、机器学习基础(3 Weeks)*

### 3.1 需掌握的基本能力
- 监督学习：了解基本的回归、分类算法（如线性回归、逻辑回归、决策树、支持向量机等）以及如何使用Python库实现
  
  了解监督学习和无监督学习的定义：参照-->[机器学习-吴恩达[P3-P4]](https://www.bilibili.com/video/BV1By4y1J7A5/?p=3)
  
  - **线性回归**：了解回归、损失函数的概念、学会使用最小二乘法你和线性回归函数-->参见 西瓜书[3.2]、[机器学习-吴恩达[P5]](https://www.bilibili.com/video/BV1By4y1J7A5/?p=5)、[知乎Blogs](https://zhuanlan.zhihu.com/p/488128941)
  
  - **Logistics回归**：logistic regression虽然被称为回归，但实际上是分类模型。它是一种用于解决二分类问题的机器学习方法，用于估计某种事物的可能性。 原理是用逻辑函数把线性回归的结果(-∞,∞)映射到(0,1)。--> 西瓜书[3.3]、机器学习-[吴恩达[P32]](https://www.bilibili.com/video/BV1By4y1J7A5/?p=32)、[参考博客](https://cloud.tencent.com/developer/article/1694338)
  
  - **多分类学习**：多分类是分类问题的延申，需了解类似问题的一般处理思路  --> 西瓜书[3.5]、机器学习-吴恩达[P38、P49]
  
  - **贝叶斯分类**：贝叶斯分类器是一类分类算法的总称，贝叶斯定理是这类算法的核心，统称为贝叶斯分类。主要分为贝叶斯决策论、极大似然估计、朴素贝叶斯分类器、半朴素贝叶斯分类器、贝叶斯网络等内容，初学了解贝叶斯定理、极大似然估计、朴素贝叶斯分类器即可。参见 --> 西瓜书[7.1-7.3], EM算法(可选)、[可参考博客](https://www.cnblogs.com/jpcflyer/p/11069659.html)
  
  - **支持向量机(可选)**：支持向量机（support vector machines, SVM）是一种二分类模型，基本模型是定义在特征空间上的间隔最大的线性分类器；SVM还包括核技巧，使其成为实质上的非线性分类器。SVM的的学习策略就是间隔最大化，可形式化为一个求解凸二次规划的问题，也等价于正则化的合页损失函数的最小化问题。SVM的的学习算法就是求解凸二次规划的最优化算法。有兴趣可以学习具体算法，非必需。参见 --> 西瓜书[6.]、[机器学习-吴恩达[P71-P75]](https://www.bilibili.com/video/BV1By4y1J7A5/?p=71)
  
  - **神经网络(感知机)**：西瓜书[5.1-5.4]

- 无监督学习：了解聚类、降维算法（如K-Means、PCA等）以及如何使用Python库实现
  
  - **K近邻学习**: KNN是一种经典分类和回归算法，算法逻辑很简单，入门必了解的算法。 西瓜书[10.1]、[可参考Blog](https://zhuanlan.zhihu.com/p/25994179)

  - **距离计算**：一些常见的距离度量方式。西瓜书[9.2-9.3]
  
  - **K-Means聚类**：[机器学习-吴恩达[P77]](https://www.bilibili.com/video/BV1By4y1J7A5/?p=77)，[可参考Blog](https://zhuanlan.zhihu.com/p/75477709)
  
  - **PCA降维**：西瓜书[10.3]、[吴恩达[P82-P87]](https://www.bilibili.com/video/BV1By4y1J7A5/?p=82)

- 模型评估与选择：了解常用的评估指标（如准确率、召回率、F1-score等）和交叉验证方法以及如何使用Python库实现
  - **验证集、训练集**：西瓜书[2.2]、机器学习-吴恩达[P60]
  
  - **经验误差、泛化误差、过拟合**：模型的预测输出与样本的真实输出之间的差异称作“误差”（error），模型在训练集上的误差称作训练误差，也叫**经验误差**；在新样本上的误差称作**泛化误差**, 当模型把训练样本学得“太好”时，很可能已经把训练样本自身的一些特点当作了所有潜在样本都会具有的一般性质，这样会致使泛化性能的下降，这种现象在机器学习中称作**过拟合(overfitting)**，与过拟合相对的是**欠拟合(underfitting)**，欠拟合是指对训练样本的一般性质尚未学好。-->西瓜书[2.1]、[吴恩达[P39]](https://www.bilibili.com/video/BV1By4y1J7A5/?p=39)
  
  - **正则化、偏差与方差**：偏差指的是预测值（估计值）的期望与真实值之间的差距，偏差越大，越偏离真实数据；方差指的是预测值的变化范围，离散程度，也就是离其期望值的距离，方差越大，数据的分布越分散。参见-->西瓜书[2.5]、机器学习-吴恩达[P41、P42、P61、P62]
  
  - **性能度量**：了解混淆矩阵、准确率、召回率、精度、F1-Score等度量学习效果好坏的概念，参见--> 西瓜书[2.3]、[参考博客](https://www.cnblogs.com/wuliytTaotao/p/9285227.html)

### 3.2 学习资源
- 书籍：《机器学习》(周志华)、《统计学习方法》（李航）、《机器学习实战》（Peter Harrington）

- 文档：[Sklearn官方中文文档](https://sklearn.apachecn.org/#/)

- 视频课程：[机器学习-吴恩达](https://www.bilibili.com/video/BV1By4y1J7A5/?spm_id_from=333.337.search-card.all.click&vd_source=ef6bc9d073dccb208fb608bc99286677)（[参考教程](https://momodel.cn/workspace/643e9c46dea202f32b3e7cf8/app)）[机器学习-李宏毅](https://www.bilibili.com/video/BV13x411v7US/?spm_id_from=333.337.search-card.all.click&vd_source=ef6bc9d073dccb208fb608bc99286677)
- 说明：所列基本能力是需要掌握的基础。sklearn库实现了绝大多数机器学习的算法，学习过程中尝试通过调用API进行案例实践。
## *四、深度学习基础(3 weeks)*
### 4.1 需掌握的基本能力
- 神经网络基础：首先了解感知机和多层感知机的原理，理解反向传播的基本原理和基本推导，掌握神经网络的基本组成部分(神经元、激活函数、损失等)，参照《神经网络与深度学习》(Michael Nielsen 著)Chapter1-Chapter2，学习相关概念，并根据开源项目跑通手写数字识别。其次掌握卷积神经网络、循环神经网络的相关概念，掌握基本概念和基本原理之后以项目为主导入手，推荐项目：
  - **感知机**：最初版本的感知机是一种线性分类器，但却是深度网络的基础，需要了解感知机的公式形式、迭代方法、线性性质等。神经网络与深度学习[1.1]、西瓜书[5.2]、[参考Blog](https://zhuanlan.zhihu.com/p/72040253)
  
  - **多层感知机(MLP)**：针对感知机无法解非线性分类问题，多层感知机引入激活函数，将感知机扩展到多层。需要了解多层感知机的改进点以及多层网络的作用。参见-->西瓜书[5.3]
  
  - **损失函数**：损失函数是神经网络优化的目标，需要掌握损失函数的概念，了解常见的损失函数的形式，推导过程，求导过程以及基础实现方法。参见-->  [参考Blog](https://zhuanlan.zhihu.com/p/261059231)、 [机器学习-吴恩达[P6-P8]](https://www.bilibili.com/video/BV1By4y1J7A5/?p=6)
  
  - **网络更新**：理解梯度下降算法的基本原理，掌握链式法则、参数梯度的计算。参见-->《神经网络与深度学习》[1.5、Ch.2]、[动手学深度学习[P7]](【07 自动求导【动手学深度学习v2】-哔哩哔哩】 https://b23.tv/GGvh4Yy)
  
  - **参考项目**：[动手学深度学习[P10]](https://www.bilibili.com/video/BV1hh411U7gn/?)

- 常用神经网络：理解不同的神经网络的结构和基础组成部分、理解批次的概念
  
  - **卷积神经网络(CNN)**：理解卷积、卷积核、池化等相关概念、理解LeNet、AlexNet、VGG、Inception、ResNet等经典网络的结构。动手实现LeNet和ResNet。-->动手学深度学习[P23、P29]、[LeNet参考项目](https://github.com/activatedgeek/LeNet-5)、[AlextNet](https://github.com/Lornatang/AlexNet-PyTorch)
  
  - **循环神经网络(RNN)**：理解循环网络的网络形式以及网络实现方法。-->[《动手学深度学习》(李沐)](https://zh-v2.d2l.ai/chapter_recurrent-neural-networks/index.html)、动手学深度学习[P54-P59]、[参考博客](https://zybuluo.com/hanbingtao/note/541458)
  
  - **注意力机制(Attention)**：注意力机制是Transformer的最基础的结构，最初用于NLP领域，但在计算机视觉领域以及图领域也表现出了极强的特征提取能力，推荐阅读《Attention is All You Need》原文。参见-->[《动手学深度学习》(李沐)](https://zh-v2.d2l.ai/chapter_attention-mechanisms/index.html)、[动手学深度学习[P68]](https://www.bilibili.com/video/BV1Kq4y1H7FL)、[参考论文](https://arxiv.org/abs/1706.03762)
  
  - **注**: 深度学习的学习需要配合具体项目进行，除了了解网络结构外，还要能够独立进行项目的运行demo。所列资源以及demo都是基于pytorch版本，学习过程中配合pytorch教程，了解网络实现逻辑，了解pytorch的框架结构。

- 模型训练与优化：了解常用的优化算法、网络改进策略
  
  - **优化算法**：理解神经网络优化的经典算法，如SGD、Adagrad、Adadelta、Adam等，理解梯度下降算法的基本原理。以及不同优化算法的区别以及改进思路。进一步学习，可参照《最优化及其应用》。 参见-->[《动手学深度学习》李沐](https://zh-v2.d2l.ai/chapter_optimization/index.html)、[动手学深度学习[P72]](https://www.bilibili.com/video/BV1bP4y1p7Gq)
  
  - **调参炼丹**：学习一般的调参方法，了解哪些属于可调参数，学习调参的基本方向是什么等技能。参见--> [Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook)、[DeepLearningTuning-中文译版](https://github.com/chunqiangqian/deepLearningTuning/blob/main/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E8%B0%83%E5%8F%82%E6%96%B9%E6%B3%95.md)
- 常用框架：了解PyTorch、TensorFlow等常用深度学习框架的基本用法
  
  - 系统性学习Pytorch可参照-->[Pytorch入门教程](https://www.bilibili.com/video/BV1rs4y1E7gx/?spm_id_from=333.337.search-card.all.click&vd_source=ef6bc9d073dccb208fb608bc99286677)

### 4.2 学习资源
* 书籍：《神经网络与深度学习》（Michael Nielsen）、《深度学习框架：Pytorch入门与实践》（陈云）、[《动手学深度学习》(李沐)](https://zh-v2.d2l.ai/index.html)

* 文档：[Pytorch官方中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)

* 课程： [Pytorch入门教程](https://www.bilibili.com/video/BV1rs4y1E7gx/?spm_id_from=333.337.search-card.all.click&vd_source=ef6bc9d073dccb208fb608bc99286677)、[动手学深度学习--李沐](https://space.bilibili.com/1567748478/channel/seriesdetail?sid=358497)

## 说明
本指南为在有一定数学基础下的速通指南，各部分之间会有些许交叉。总的来说机器学习是最重要的基础，可以参考西瓜书了解相关理论，其中的公式推导可以参考南瓜书的讲解，也可以参考统计学习方法，但对于本教程，不需要完全理解书中所有的内容和公式推导。深度学习更面向应用，推荐根据《神经网络与深度学习》（Michael Nielsen）以及《动手学深度学习》(李沐)课程进行系统学习，《动手学深度学习》有配套的教材和视频课程，尝试仿照例程跑一些demo实战能帮助理解，但需要有pytorch的相关基础。
