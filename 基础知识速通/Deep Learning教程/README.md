- [*深度学习基础教程*](#深度学习基础教程)
  - [Pytorch快速入门](#pytorch快速入门)
    - [Pytorch安装](#pytorch安装)
    - [Pytorch 入门教程](#pytorch-入门教程)
  - [卷积神经网络](#卷积神经网络)
  - [循环神经网络](#循环神经网络)
  - [注意力机制](#注意力机制)
  - [优化算法](#优化算法)
  - [调参炼丹](#调参炼丹)

# *深度学习基础教程*
通过机器学习教程的学习，已经掌握了如如损失函数、梯度下降等神经网络的基础。本教程基于Pytorch框架和《动手学深度学习》第二版教材以及配套视频进行学习。首先通过Pytorch入门教程快速学习Pytorch的基础规则与代码逻辑，并尝试调试手写数字识别项目。然后学习三种主要的神经网络形式即卷积神经网络、循环神经网络、注意力机制。每一部分都有相应的demo项目，学习过程中可以尝试运行调试。然后学习几种优化算法，理解优化器的工作原理，学会如何调试选择优化器。最后学习深度学习的调参技巧。


## Pytorch快速入门
Pytorch是一个庞大的框架系统，无法在短时间内了解所有的框架内容，因此这部分旨在快速介绍Pytorch的基础知识以便于能够阅读和运行后续的示例代码，关于Pytorch的更详细的内容可以查阅[官方文档](https://pytorch123.com/)
### Pytorch安装
安装教程主要根据Windows系统
  - 1. CUDA和Cudnn安装
    参考[教程博客](https://blog.csdn.net/m0_45447650/article/details/123704930) 
    注：按照这个教程安装暂时没遇到什么问题，后续具体问题欢迎反馈
  - 2. Pytorch命令行安装
    - 1. 首先激活创建的Python环境，查看cuda版本
    - 2. 进入[官方启动引导页面](https://pytorch.org/get-started/locally/)，根据cuda版本获取安装命令
    ![image](https://github.com/UNIC-Lab/AI_Course/assets/90789521/9c250e82-e75d-4db2-8983-589bedd49475)

    此处`-c pytorch`指从Pytorch官网下载，下载很慢，可以通过配置镜像加速下载
    `conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/`
    配置完成后去掉`-c pytorch`即可
    
  - 3. Pytorch离线安装
    命令行安装失败，一般都是因为下载超时或者下载的版本，可以使用通过科学上网在[官方下载地址](https://download.pytorch.org/whl/torch/)中下载对应系统、python版本、cuda版本的离线安装包，其中python版本必须严格对应，cuda版本可以向下兼容。然后cd到离线安装包目录通过安装命令安装。
    安装命令：`pip install [torch_file] -i https://pypi.tuna.tsinghua.edu.cn/simple`或`conda install [torch_file]`
### Pytorch 入门教程
1. [参考教程](https://ptorch.com/docs/3/deep_learning_60min_blitz)
2. 参考[视频课程](https://www.bilibili.com/video/BV1AK4y1P7vs?p=5&vd_source=ef6bc9d073dccb208fb608bc99286677)
3. 运行手写数字识别项目
## 卷积神经网络
- 教材：[《动手学深度学习》Ch6-卷积神经网络](https://zh-v2.d2l.ai/chapter_convolutional-neural-networks/index.html)
- 视频：[动手学习深度学习v2[P19-P29]](https://www.bilibili.com/video/BV1264y1i7R1/?spm_id_from=333.999.0.0&vd_source=ef6bc9d073dccb208fb608bc99286677)
- Demo：调试运行[LeNet项目](https://github.com/UNIC-Lab/AI_Course/tree/main/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E9%80%9F%E9%80%9A/Deep%20Learning%E6%95%99%E7%A8%8B/Projects/LeNet)
## 循环神经网络
- 教材：[《动手学深度学习》Ch9-现代循环神经网络](https://zh-v2.d2l.ai/chapter_recurrent-modern/index.html)
- 视频：[动手学深度学习v2[P54-P59]](https://www.bilibili.com/video/BV1264y1i7R1/?spm_id_from=333.999.0.0&vd_source=ef6bc9d073dccb208fb608bc99286677)
- Demo：
## 注意力机制
- 教材：[《动手学深度学习》Ch10-注意力机制](https://zh-v2.d2l.ai/chapter_attention-mechanisms/index.html)
- 视频：[动手学深度学习v2[P64-P68]](https://www.bilibili.com/video/BV1264y1i7R1/?spm_id_from=333.999.0.0&vd_source=ef6bc9d073dccb208fb608bc99286677)
- Paper：[Attention is All You Need](https://arxiv.org/abs/1706.03762)
- Demo: 参考[Transformer](https://github.com/jadore801120/attention-is-all-you-need-pytorch)

## 优化算法
理解优化算法与网络优化的概念 了解相关优化算法，并理解Pytorch中的优化器
- 参考教材：[《动手学深度学习》Ch11-优化算法](https://zh-v2.d2l.ai/chapter_optimization/index.html)
- 参考课程：[动手学深度学习v2[P72]](https://www.bilibili.com/video/BV1bP4y1p7Gq/?spm_id_from=333.999.0.0&vd_source=ef6bc9d073dccb208fb608bc99286677)
## 调参炼丹
学习一般的调参方法，了解哪些属于可调参数，学习调参的基本方向是什么等技能。参见--> [Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook)、[DeepLearningTuning-中文译版](https://github.com/chunqiangqian/deepLearningTuning/blob/main/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E8%B0%83%E5%8F%82%E6%96%B9%E6%B3%95.md)
