# ***强化学习进阶***
## 一、强化学习基础理论与核心概念

第一节中所介绍的值函数、MC方法、TD方法等都是基于算法的，是对算法的归类，因此与后续介绍的QLearning、Sarsa等比较基础的算法有交叉，学习过程中需要对应具体算法的教程进行学习，理解算法具体流程的同时学习归纳基于值函数和基于策略的概念，以及基于MC和基于TD的区别与优劣。
- 1.0 **强化学习基础理论**: 第一阶段需要理解强化学习的核心理论，学习强化学习的四要素以及策略迭代、策略梯度两种方式。可以参照教材，然后理解值函数和策略的概念，并掌握基于蒙特卡洛的强化学习方法和基于TD的方法，并理解基于蒙特卡洛和基于TD两种方法中方差和偏差的概念。-->西瓜书[Ch.16]
- 1.1 **Markov决策过程**
  - Blogs: [马尔可夫决策过程原理与代码实现](https://blog.csdn.net/qq_41297934/article/details/105104684)
  - Paper: [Markov decision processes: Concepts and algorithms](https://www.writebug.com/git/awan/aicar/raw/commit/f779d0e788f6ba0aeb45d8d31f1384c09c236afe/references/Markov%20Decision%20Processes%20Concepts%20and%20Algorithms.pdf)
- 1.2 值函数和策略
  - Blogs: [基于值和策略的强化学习入坑](https://zhuanlan.zhihu.com/p/54825295)
- 1.4 蒙特卡罗方法
  - Blogs: [强化学习 - 蒙特卡罗法(Monte Carlo Methods)](https://zhuanlan.zhihu.com/p/72715842)
- 1.5 时间差分方法
  - Blogs：[强化学习 - 时间差分学习(Temporal-Difference Learning)](https://zhuanlan.zhihu.com/p/73083240)
  - Paper: [Temporal difference learning and TD-gammon](https://dl.acm.org/doi/10.1145/203330.203343)
- 1.6 动态规划方法
  - Blogs: [强化学习 - 动态规划(Dynamic Programming)](https://zhuanlan.zhihu.com/p/72360992)
## 二、基于值函数的强化学习算法
- **Q-Learning算法**
  - Paper: [Q Learning](https://link.springer.com/article/10.1007/BF00992698)
- **Sarsa算法**
  - Paper: [On-line Q-learning using connectionist systems](https://www.researchgate.net/profile/Mahesan-Niranjan/publication/2500611_On-Line_Q-Learning_Using_Connectionist_Systems/links/5438d5db0cf204cab1d6db0f/On-Line-Q-Learning-Using-Connectionist-Systems.pdf?_sg%5B0%5D=HYd0h230b7WOR6m4hj5yx01K97aS61Z0DufUURMQr9ZqMqcEVZ0dNpG84h6uCfRl_M40FNkXgRX-GnpnxH31Ww.jBF3fgrlhaJYs3bDEaHQU22nRpKP0zKeF_oOsqh7WddL8pfxAomPSbeANzdmLP9YPB26HbLeSaEJqhFgzIxvWQ&_sg%5B1%5D=CZtZhHTEMgSwBZrpZU_7BACd8RH04JUKiITdXRQJ6MQ9SFS27jreZmcsuNcqYYWRoxcwBE-xBMbrfl1QobmEZ65bmkmpzonq5JoLRIIUKXne.jBF3fgrlhaJYs3bDEaHQU22nRpKP0zKeF_oOsqh7WddL8pfxAomPSbeANzdmLP9YPB26HbLeSaEJqhFgzIxvWQ&_iepl=)
- **DQN算法**
  - Paper: [Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236/?source=post_page---------------------------)
- Double DQN算法
  - Paper: [Deep Reinforcement Learning with Double Q-Learning](https://ojs.aaai.org/index.php/AAAI/article/view/10295)
- Dueling DQN算法
  - Paper: [Dueling Network Architectures for Deep Reinforcement Learning](http://proceedings.mlr.press/v48/wangf16.html)
- Prioritized Experience Replay算法
  - Paper: [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952)
- Rainbow算法
  - Paper: [Rainbow: Combining Improvements in Deep Reinforcement Learning.](https://ojs.aaai.org/index.php/AAAI/article/view/11796)
## 三、基于策略梯度的强化学习算法
- **REINFORCE算法**
  - Paper: [Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning](https://link.springer.com/chapter/10.1007/978-1-4615-3618-5_2)
- **Actor-Critic算法**
  - Paper: [Actor-Critic Algorithms](https://proceedings.neurips.cc/paper/1999/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html)
- A3C算法
  - Paper: [Asynchronous Methods for Deep Reinforcement Learning.](http://proceedings.mlr.press/v48/mniha16.html?ref=https://githubhelp.com)
- TRPO算法
  - Paper: [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html)
- PPO算法
  - Paper: [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
## 四、基于动作价值和策略梯度的强化学习算法
- **DDPG算法**
  - Paper: [Deterministic Policy Gradient Algorithms](http://proceedings.mlr.press/v32/silver14.html)、 [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971)
- TD3算法
  - Paper: [Addressing Function Approximation Error in Actor-Critic Methods](https://proceedings.mlr.press/v80/fujimoto18a.html)
- SAC算法
  - Paper: [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b)
## 五、基于模型的强化学习算法
- Model-Based RL
- MBRL with Planning and Prediction
- MBRL with World Models

## 六、相关学习资源：

- 书籍与教程

  - 《深度强化学习》（丁负、贾志刚等）

  - [《强化学习导论》（Sutton著）](https://rl.qiwihui.com/zh_CN/latest/)

  - 《强化学习：原理、算法与应用》（李宏毅、王宇飞、李剑飞著）

  - 《深度强化学习实战》（王汝建等著）

  -  [OpenAI spinningup强化学习教程](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)

- 视频课程

  - [UCB CS285](https://www.bilibili.com/video/BV12341167kL/?spm_id_from=333.337.search-card.all.click&vd_source=ef6bc9d073dccb208fb608bc99286677)

  - [《Reinforcement Learning》(UCL. David Silver)](https://www.davidsilver.uk/teaching/)

  - [深度强化学习-李宏毅](https://www.bilibili.com/video/av24724071/?from=search&seid=9547815852611563503&vd_source=ef6bc9d073dccb208fb608bc99286677)
## 说明

文档给出了强化学习的大致概念和经典的论文，速通可以参考博客，当然博客质量参差不齐，需要细细斟酌。基础理论如Bellman方程等建议手动推一遍。相关算法是比较重要的需要掌握的强化学习模型，速通可以参考相关博客，给出的论文都是影响力比较高的，大多有比较严格的理论推导和证明，有兴趣可以细推，加粗的算法是必须掌握的，其余的是影响比较高的。当然也可以跟着课程或者书籍更系统性的学习，其中CS285和Reinforcement Learning是公认质量比较高的课程。比较推荐的是根据openai spinningup教程进行系统性学习相关算法，以及实现方法。

基础理论和几个核心概念的是强化学习的重点基础，理解不清楚可能会在后面的学习中逐渐懵逼。。建议先从Markov决策过程的原理和概念入手，掌握值函数、策略的概念，理解蒙特卡罗方法、时间差分方法和动态规划方法的异同与优劣。

基于值函数的强化学习算法部分，建议先学习Q-Learning算法和Sarsa算法，这两个算法是强化学习中比较基础的算法，对于理解和掌握基于值函数的强化学习算法有很大的帮助。然后学习DQN算法、Double DQN算法、Dueling DQN算法、Prioritized Experience Replay算法和Rainbow算法等高级算法。

基于策略梯度的强化学习算法部分，建议先学习REINFORCE算法和Actor-Critic算法，这两个算法是基于策略梯度的强化学习算法中比较基础的算法，对于理解和掌握基于策略梯度的强化学习算法有很大的帮助。然后学习A3C算法、TRPO算法和PPO算法等高级算法。

基于动作价值和策略梯度的强化学习算法部分，建议先学习DPG和DDPG算法，这两个算法是基于动作价值和策略梯度的强化学习算法中比较基础的算法，对于理解和掌握这类算法有很大的帮助。接着，可以学习TD3算法和SAC算法等高级算法。
