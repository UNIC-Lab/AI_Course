# ***基础知识速通指南***
## *一、数学基础*
### 1.1 需掌握的基本能力
* 线性代数：了解矩阵、向量、行列式、特征值等基本概念

* 微积分：了解导数、偏导数、极值等基本概念

* 概率论与统计学：了解概率、条件概率、期望、方差等基本概念
## *二、编程基础（1 Weeks）*
### 2.1 需掌握的基本能力
- Python基础：了解Python基本语法、掌握基本数据类型、条件语句、循环语句、函数、列表、字典等
- Python需要了解的知识点及参考资料：
  - 编程环境配置：IDE工具：vscode(简洁、可玩性高、可扩展性强)、pycharm(开发工具更多、更专业、且集成了环境管理工具)、JupyterNotbook(基于Web，基于ipython，支持markdown)，版本：Python3.4-Python3.10。
  - 基础语法知识点：基本环境、变量和数据类型、列表、if判断、字典、标准输入输出、while循环、函数、类、文件、异常等。这些是保证能写出完整代码的必要保证。
  - 必要的工具库：[Numpy（基础且通用的库，处理n维array）](https://github.com/lijin-THU/notes-python/blob/master/03-numpy/03.01-numpy-overview.ipynb)、[matplotlib(python绘图基础)](https://github.com/lijin-THU/notes-python/blob/master/03-numpy/03.02-matplotlib-basics.ipynb)等。
  - 环境管理：推荐conda([使用指南](https://zhuanlan.zhihu.com/p/44398592))
### 2.2 学习资源
* 书籍：《Python基础教程》（廖雪峰）、《python编程：从入门到实战》（埃里克 • 马瑟斯）

* 文档：[Python3官方中文文档](https://docs.pythontab.com/python/python3.4/)

* 视频课程：[《Python零基础教程》](https://www.bilibili.com/video/BV1qW4y1a7fU/?spm_id_from=333.337.search-card.all.click)
* 说明：参照《Python编程：从入门到实战》Chapter1-Chapter11可快速入门，numpy和matplotlib需要掌握基本的使用方法，可阅读官方文档或者相关博客，学习过程中以实践为主。视频课程资料可参考B站黑马程序员。环境安装、配置等问题能问就问，尽量不要纯自己踩坑，费时且无用。
## *三、机器学习基础(3 Weeks)*

### 3.1 需掌握的基本能力
- 监督学习：了解基本的回归、分类算法（如线性回归、逻辑回归、决策树、支持向量机等）以及如何使用Python库实现
  - 机器学习-吴恩达[P3-P4]
  - 线性回归：
  - Logistics回归：
  - 多分类学习：
  - 贝叶斯分类：
  - 支持向量机(可选)：
  - 神经网络(感知机)：

- 无监督学习：了解聚类、降维算法（如K-Means、PCA等）以及如何使用Python库实现
  - K近邻学习:
  - 距离计算：
  - K-Means聚类：机器学习-吴恩达[P77]
  - PCA降维：

- 模型评估与选择：了解常用的评估指标（如准确率、召回率、F1-score等）和交叉验证方法以及如何使用Python库实现
  - 验证集、训练集：西瓜书[2.2]、机器学习-吴恩达[P60]
  - 经验误差：
  - 过拟合：
  - 正则化、偏差与方差：西瓜书[2.5]、机器学习-吴恩达[P61、P62]
  - 性能度量：混淆矩阵、准确率、召回率、精度、F1-Score等概念
  - 正则化：
### 3.2 学习资源
- 书籍：《机器学习》(周志华)、《统计学习方法》（李航）、《机器学习实战》（Peter Harrington）

- 文档：[Sklearn官方中文文档](https://sklearn.apachecn.org/#/)

- 视频课程：[机器学习-吴恩达](https://www.bilibili.com/video/BV1By4y1J7A5/?spm_id_from=333.337.search-card.all.click&vd_source=ef6bc9d073dccb208fb608bc99286677)、[机器学习-李宏毅](https://www.bilibili.com/video/BV13x411v7US/?spm_id_from=333.337.search-card.all.click&vd_source=ef6bc9d073dccb208fb608bc99286677)
- 说明：所列基本能力是需要掌握的基础。sklearn库实现了绝大多数机器学习的算法，学习过程中尝试通过调用API进行案例实践。
## *四、深度学习基础*
### 4.1 需掌握的基本能力
* 神经网络基础：了解神经网络的基本组成部分（如感知器、多层感知器等）以及如何使用Python库实现

* 模型训练与优化：了解常用的激活函数、损失函数、优化算法以及如何使用Python库实现

* 常用框架：了解PyTorch、TensorFlow等常用深度学习框架的基本用法

### 4.2 学习资源
* 书籍：《神经网络与深度学习》（Michael Nielsen）、《深度学习框架：Pytorch入门与实践》（陈云）

* 文档：[Pytorch官方中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)

* 课程： [Pytorch入门教程](https://www.bilibili.com/video/BV1rs4y1E7gx/?spm_id_from=333.337.search-card.all.click&vd_source=ef6bc9d073dccb208fb608bc99286677)、[动手学深度学习--李沐](https://space.bilibili.com/1567748478/channel/seriesdetail?sid=358497)

## 说明
本指南为在有一定数学基础下的速通指南，各部分之间会有些许交叉。总的来说机器学习是最重要的基础，可以参考西瓜书了解相关理论，其中的公式推导可以参考南瓜书的讲解。深度学习更面向应用，推荐根据《神经网络与深度学习》（Michael Nielsen）进行系统学习，同时尝试跑一些demo实战能帮助理解，深度学习框架方面推荐Pytorch。相关pdf资源已上传。
