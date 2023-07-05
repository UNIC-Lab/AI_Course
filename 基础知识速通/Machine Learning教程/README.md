- [MachineLearning教程](#machinelearning教程)
  - [线性回归到神经网络](#线性回归到神经网络)
  - [传统机器学习算法](#传统机器学习算法)
  - [模型评估与调优](#模型评估与调优)

# MachineLearning教程
在开始本教程之前，请先了解机器学习的大致概念，并掌握一定的python基础，能够阅读并运行jupyter notebook文件。基于实验室的方向特性，我们在机器学习部分安排三部分内容，**神经网络机器学习基础**，**传统机器学习算法**，**模型评估与调优**。由于我们的最终目的是掌握深度神经网络及其原理，而深度学习是机器学习的子集，因此第一部分学习如何从最基础的机器学习即线性回归引入到深度神经网络。第二部分我们学习一些简单的其他机器学习机器，如贝叶斯分类、高斯混合模型，这些方法既是常用的工具，也能够从数学上更深的理解机器学习。第三部分学习模型的评估与调优，了解机器学习相关的评估指标，理解机器学习的中的偏差、方差的概念，并学习调优方法。

## 线性回归到神经网络
第一部分从**线性回归**逐渐引入到神经网络，这一部分是学习重点。首先从**线性回归**和**Logistic回归**理解拟合与分类两种任务的联系与区别并对机器学习有一个基础的认识。**（单层）感知机**是神经网络的雏形，了解感知机权重的本质是分界线的参数，并掌握更新权重的方法。**神经网络**即多层感知机，学习这一部分，需要理解神经网络和感知机之间的联系，理解深度网络激活函数的作用，为何深度神经网络相对感知机能够实现非线性分类。这一部分主要学习吴恩达机器学习课程，感知机部分参考《统计学习方法》(周志华)5.2节。配套的其余参考提供了一些博客以便于更轻松地理解相关概念。
|知识点|教材|视频|代码|
|:------|------|------|----:|
|线性回归|[机器学习讲义-线性回归](https://scruel.gitee.io/ml-andrewng-notes/week1.html)|[机器学习(吴恩达)[P10-P19]](https://www.bilibili.com/video/BV1cv4y1W7A3?p=9&vd_source=ef6bc9d073dccb208fb608bc99286677)|[线性回归notebook](https://github.com/UNIC-Lab/AI_Course/tree/main/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E9%80%9F%E9%80%9A/Machine%20Learning%E6%95%99%E7%A8%8B/NoteBooks/1.linear_regression)|
|Logistic回归|[机器学习讲义-Logistic回归](https://scruel.gitee.io/ml-andrewng-notes/week3.html)| [机器学习(吴恩达)[P32-P41]](https://www.bilibili.com/video/BV1cv4y1W7A3?p=32&vd_source=ef6bc9d073dccb208fb608bc99286677) |[Logistic回归notebook](https://github.com/UNIC-Lab/AI_Course/tree/main/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E9%80%9F%E9%80%9A/Machine%20Learning%E6%95%99%E7%A8%8B/NoteBooks/2.logistic_regression)|
|感知机|《机器学习》(周志华)|[解读西瓜书](https://www.bilibili.com/video/BV1dM411k7q5?p=24&vd_source=ef6bc9d073dccb208fb608bc99286677)|
|神经网络|[机器学习讲义-神经网络](https://scruel.gitee.io/ml-andrewng-notes/week4.html)|[机器学习(吴恩达)[P51-P58]](https://www.bilibili.com/video/BV1cv4y1W7A3?p=51&vd_source=ef6bc9d073dccb208fb608bc99286677)|[神经网络notebook](https://github.com/UNIC-Lab/AI_Course/tree/main/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E9%80%9F%E9%80%9A/Machine%20Learning%E6%95%99%E7%A8%8B/NoteBooks/4.nurual_network_back_propagation)|

## 传统机器学习算法
这一部分我们学习非神经网络的机器学习分支，只需要学习一些简单的算法，主要设计分类、聚类、降维三部分。首先从**K近邻**算法入手，KNN是最简单的分类算法之一，掌握其具体的算法步骤和概念即可。**K-Means**是最为常用的聚类算法，只需要学习最简单的线性K-Means分类即可。PCA算法是一种降维算法，可以实现。**支持向量机**是除神经网络外最常用的机器学习分类算法，速通阶段只需要学习线性的SVM即可。这一部分的教程主要参考西瓜书，配套b站解读西瓜书系列视频学习。学习完之后阅读并运行相关代码
|知识点|教程|视频|代码|
|:------|------|------|----:|
|KNN|《机器学习》(周志华)[10.1]|[解读西瓜书-K近邻](https://www.bilibili.com/video/BV1dM411k7q5?p=52&vd_source=ef6bc9d073dccb208fb608bc99286677)|[KNN notebook](https://github.com/UNIC-Lab/AI_Course/blob/main/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E9%80%9F%E9%80%9A/Machine%20Learning%E6%95%99%E7%A8%8B/NoteBooks/knn-notebook.ipynb)|
|K-Means|机器学习讲义|[KMeans聚类](https://www.bilibili.com/video/BV17Y4y1v7XH?p=3&vd_source=ef6bc9d073dccb208fb608bc99286677)|[K-Means notebook](https://github.com/UNIC-Lab/AI_Course/tree/main/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E9%80%9F%E9%80%9A/Machine%20Learning%E6%95%99%E7%A8%8B/NoteBooks/7.kmeans_and_PCA)|
|PCA降维|《机器学习》(周志华)[10.3]|[PCA降维](https://www.bilibili.com/video/BV1QS4y1e7y6/?spm_id_from=333.337.search-card.all.click&vd_source=ef6bc9d073dccb208fb608bc99286677)|[PCA notebook](https://github.com/UNIC-Lab/AI_Course/tree/main/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E9%80%9F%E9%80%9A/Machine%20Learning%E6%95%99%E7%A8%8B/NoteBooks/7.kmeans_and_PCA)|
|贝叶斯分类  |《机器学习》(周志华)[7.1-7.3]|[解读西瓜书-贝叶斯分类器](https://www.bilibili.com/video/BV1dM411k7q5?p=35&vd_source=ef6bc9d073dccb208fb608bc99286677)|
|*支持向量机|《机器学习》(周志华)[6.1-6.2]|[解读西瓜书-支持向量机](https://www.bilibili.com/video/BV1dM411k7q5?p=29&vd_source=ef6bc9d073dccb208fb608bc99286677)|


## 模型评估与调优

这一部分主要参考《机器学习》(周志华)
模型评估方面
性能度量：了解混淆矩阵的概念，精准率和召回率

|知识点|教程|视频|
|:------|------|------:|
|模型评估与交叉验证|《机器学习》(周志华)[2.2]|[机器学习初步(周志华)[P12]](https://www.bilibili.com/video/BV1xs4y1x7Uf?p=12&vd_source=ef6bc9d073dccb208fb608bc99286677)|
|过拟合、偏差与方差|《机器学习》(周志华)[2.1]|[机器学习初步(周志华)[P10]](https://www.bilibili.com/video/BV1xs4y1x7Uf?p=10&vd_source=ef6bc9d073dccb208fb608bc99286677)|
|性能度量|《机器学习》(周志华)[2.3]|[机器学习初步(周志华)[P14]](https://www.bilibili.com/video/BV1xs4y1x7Uf?p=14&vd_source=ef6bc9d073dccb208fb608bc99286677)|



