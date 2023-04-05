# 图神经网络进阶
## 一、图卷积网络 (Graph Convolutional Networks, GCN)：
  GCN是最早被提出的图神经网络，其主要思想是将神经网络中的卷积操作推广到图上。在GCN中，节点的表示是通过其相邻节点的表示加权和来计算的。GCN已被广泛应用于节点分类、图分类和链接预测等任务。
  - Paper:
    - [Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/abs/1609.02907)
    - [Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering](https://proceedings.neurips.cc/paper/2016/hash/04df4d434d481c5bb723be1b6df1ee65-Abstract.html)
    - [Spectral Networks and Locally Connected Networks on Graphs](https://arxiv.org/abs/1312.6203)
    
## 二、图注意力网络 (Graph Attention Networks, GAT)：
  GAT是一种基于注意力机制的图神经网络，其主要思想是在计算节点的表示时，给不同的邻居节点分配不同的权重。GAT通过引入注意力机制，可以更好地捕捉节点之间的复杂关系，同时提高了模型的鲁棒性。
  - Paper：
    - [Graph Attention Networks](https://arxiv.org/abs/1710.10903)
## 三、图自编码器 (Graph Autoencoder, GAE)：
  GAE是一种无监督学习方法，其主要思想是在保留原始图结构信息的同时，学习图的低维表示。GAE的训练过程分为编码器和解码器两个部分，其中编码器将原始图转换为低维表示，解码器将低维表示重构为原始图。
  - Paper：
    - [Variational Graph Auto-Encoders](https://arxiv.org/abs/1611.07308)
    - [Deep Autoencoding Gaussian Mixture Model for Unsupervised Anomaly Detection](https://openreview.net/forum?id=BJJLHbb0-)
## 四、图生成模型 (Graph Generative Models)：
  图生成模型主要用于生成具有特定结构的图，其中最为经典的是基于随机游走的模型，如DeepWalk和Node2Vec。这类模型通过学习节点之间的相似度来生成具有相似结构的图。
  - Paper:
    - [GraphGAN: Graph Representation Learning with Generative Adversarial Nets](https://ojs.aaai.org/index.php/AAAI/article/view/11872)
    - [Junction Tree Variational Autoencoder for Molecular Graph Generation](https://proceedings.mlr.press/v80/jin18a.html)
## 五、图强化学习 (Graph Reinforcement Learning)：
  图强化学习主要用于解决节点、边或图级别的任务。该领域的核心思想是将节点或边看作智能体，通过采取不同的动作来最大化累积奖励。近年来，基于强化学习的图分类和图生成方法取得了不错的效果。
  - Paper:
    - [Graph Convolutional Reinforcement Learning](https://arxiv.org/abs/1810.09202)
    
其他算法：还有一些其他的图神经网络算法，如GraphSAGE、DiffPool、GIN、TAGCN等，这些算法的主要特点是针对不同的任务，采用不同的图卷积方式和特征聚合方式。

以上只是图神经网络领域中的一些常见算法，还有很多其他的算法，如GraphSAGE、APPNP、GNN-LSTM等等。建议先从GCN、GAT和GAE入手，再逐渐扩展到其他算法。

## 六. 学习资源

书籍：《图神经网络实战》（王磊）

课程：CS224W: Machine Learning with Graphs (斯坦福大学)

- 视频教程：[CS224W: Machine Learning with Graphs (斯坦福大学)](https://www.bilibili.com/video/BV1s54y1H76H/?vd_source=ef6bc9d073dccb208fb608bc99286677)

## 七、框架
[PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/)、 [DGL](https://docs.dgl.ai/)

