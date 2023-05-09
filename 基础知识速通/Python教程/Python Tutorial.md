- [写在前面](#写在前面)
- [python介绍](#python介绍)
- [python环境管理工具](#python环境管理工具)
  - [Anaconda安装：](#anaconda安装)
  - [Anaconda使用：](#anaconda使用)
- [代码编辑器](#代码编辑器)
  - [Jupyter Notebook：](#jupyter-notebook)
- [VsCode：](#vscode)
  - [Pycharm:](#pycharm)
- [python基础知识](#python基础知识)
  - [第一阶段](#第一阶段)
  - [第二阶段\*：](#第二阶段)
  - [第三阶段：](#第三阶段)
- [基础知识视频教程](#基础知识视频教程)

# 写在前面
# python介绍

# python环境管理工具
介绍python环境的概念、conda安装、、命令集
## Anaconda安装：
  - 1. conda[下载地址](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)，注意后缀，下载符合系统的版本
  - 2. 安装过程选项：
      
      ![image](https://user-images.githubusercontent.com/90789521/236983479-e2d57e96-72a3-4cf3-87a1-83069a85661f.png)
      
      ![image](https://user-images.githubusercontent.com/90789521/236983517-c2456030-0923-4821-bda4-7e55da95f7ec.png)
      
      ![image](https://user-images.githubusercontent.com/90789521/236983670-3a8472fe-17e9-4ce8-95bf-0e5de8962f05.png)
      
      ![image](https://user-images.githubusercontent.com/90789521/236983691-85eb151f-f2e9-4245-8322-9b4da4b71d1a.png)
      
      ![image](https://user-images.githubusercontent.com/90789521/236983715-3c4bf730-bdc1-4490-b63b-04393dc6ff4c.png)
  - 3. 测试：

      cmd命令行输入：`conda --version`，输出conda版本即安装成功且环境变量配置成功
 
## Anaconda使用：
  
  conda可以理解为一个工具，也是一个可执行命令，其核心功能是包管理和环境管理。包管理与pip的使用方法类似，环境管理则是允许用户方便滴安装不同版本的python环境并在不同环境之间快速地切换。
  - 查看conda中的环境使用命令：
    `conda info -e`或者`conda env list`
    
    ![conda list](https://user-images.githubusercontent.com/90789521/236985934-5118e2f3-f2c9-4837-8baf-0ec9cc50cd99.png)
  - 创建环境：
    `conda create -n [env_name] python=x.x`，env_name为环境名，创建环境时可以直接指定python的版本
    
    或者克隆环境
    
     `conda create -n your_name --clone env_name`，将env_name的环境克隆到your_name环境
   - 激活环境：
    
      Linux:  `source activate [env_name]` `conda activate [env_name]`
    
      Windows: `activate [env_name]` `conda activate [env_name]`
    
    - conda环境中第三方库的安装：

      ```conda install -n env_name [package]  # 未激活环境```
    
      ```conda install [package]  # 如果已经激活环境```
      
      此外，也可以在激活环境后使用`pip install [package]`安装，但是注意尽量别混合使用`conda install`和`pip install`，存在依赖的包必须用同一种形式安装
    - 关闭环境：`conda deactivate`
    - 删除环境：`conda remove -n env_name --all`
    - 关于镜像：镜像网站主要作用是在安装第三方库的时候加速库的下载，初学可以对整个conda环境配置镜像，配置命令如下：
      ```
      conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/      
      conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/     
      conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/    
      conda config --set show_channel_urls yes
      ```
      
      但镜像不是万能的，具体项目可能会有些包不支持镜像，镜像删除命令如下：
      
      `conda config --remove-key channels`
      
      如果并不是所有时候都用到镜像，可以通过在安装具体库的时候指定镜像：`pip install [package] -i https://pypi.tuna.tsinghua.edu.cn/simple`

# 代码编辑器
主要推荐的编辑器和IDE包括`Jupyter Notebook`、`Visual studio code`、`Pycharm`，其中Jupyter Notebook是以网页的形式打开，可以在网页页面中直接编写代码和运行代码，代码的运行结果也会直接在代码块下显示的程序。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。VsCode是个简化高效的代码编辑器，同时支持调试、任务执行，版本管理等开发操作。Pycharm则是比较专业的针对Python的IDE
## Jupyter Notebook：
安装教程（命令行安装运行） 注：新手友好，流程简明

# VsCode：
  vscode的安装一般不会出现问题

## Pycharm:
pycharm相对于vscode更为专业，功能也更强大，但比较繁杂。Pycharm只有专业版可以连接远程服务器，所以尽量下载专业版，可以通过jetbrain的师生认证，也可以找一些都懂的资源。同时使用vscode和pycharm的话需要注意一点，两个编辑器识别文件路径的逻辑是不一样的。Pycharm可以针对项目创建环境（即解释器），也支持加载本地venv环境以及conda中环境。具体使用教程可以参考[Blog](https://zhuanlan.zhihu.com/p/231064736)。

# python基础知识

  ## 第一阶段
  
  第一阶段参照《Python编程：从入门到实践》中的第一部分，并参考知识点基于jupyter notebook进行编程运行，每个知识点有可供参考的notebook文件，教材中的知识点更细致。最好将项目git到本地进行运行，把一些可能遇到的环境配置的问题在学习初期就解决了。当然也可以使用Colab代码学习。
  [copyright](https://github.com/shibing624/python-tutorial/)

  | Notebook     |      知识点      |  Colab |
  |:----------|:-------------|---------:|
  | [01_字符串类型_str.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/01_字符串类型_str.ipynb)  | Python字符串类型  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/01_字符串类型_str.ipynb) |
  | [02_列表类型_list.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/02_列表类型_list.ipynb)  | Python列表类型  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/02_列表类型_list.ipynb) |
  | [03_元组类型_tuple.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/03_元组类型_tuple.ipynb)  | Python元组  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/03_元组类型_tuple.ipynb) |
  | [04_字典类型_dict.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/04_字典类型_dict.ipynb)  | Python字典  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/04_字典类型_dict.ipynb) |
  | [05_集合类型_set.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/05_集合类型_set.ipynb)  | Python集合  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/05_集合类型_set.ipynb) |
  | [06_条件判断_if.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/06_条件判断_if.ipynb)  | Python条件判断  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/06_条件判断_if.ipynb) |
  | [07_列表推导式.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/07_列表推导式.ipynb)  | Python列表推导式  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/07_列表推导式.ipynb) |
  | [08_循环结构_loop.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/08_循环结构_loop.ipynb)  | Python循环  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/08_循环结构_loop.ipynb) |
  | [09_函数和模块.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/09_函数和模块.ipynb)  | Python函数  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/09_函数和模块.ipynb) |
  | [10_文件和异常.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/10_文件和异常.ipynb)  | Python文件和异常  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/10_文件和异常.ipynb) |
  | [11_线程和进程.ipynb](https://github.com/shibing624/python-tutorial/blob/master/01_base/11_线程和进程.ipynb)  | Python多线程和多进程  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/01_base/11_线程和进程.ipynb) |
  | [12_面向对象编程.ipynb](https://github.com/shibing624/python-tutorial/blob/master/02_advanced/07_面向对象编程.ipynb)  | Python类  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/02_advanced/07_面向对象编程.ipynb) |

  ## 第二阶段*：
  
  掌握了Python的基础知识，并且对Python的运行逻辑具有一定的了解后，可以学习一些高级特性。这部分没有必须要求，如果感兴趣，可以选择性学习。推荐了解高阶函数和迭代器。
  [copyright](https://github.com/shibing624/python-tutorial/)

  | Notebook     |      知识点      |  Colab |
  |:----------|:-------------|---------:|
  | [01_系统交互_os.ipynb](https://github.com/shibing624/python-tutorial/blob/master/02_advanced/01_系统交互_os.ipynb)  | Python系统交互操作  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/02_advanced/01_系统交互_os.ipynb) |
  | [02_数据库_sql.ipynb](https://github.com/shibing624/python-tutorial/blob/master/02_advanced/02_数据库_sql.ipynb)  | Python操作mysql数据库  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/02_advanced/02_数据库_sql.ipynb) |
  | [03_高阶函数.ipynb](https://github.com/shibing624/python-tutorial/blob/master/02_advanced/03_高阶函数.ipynb)  | map、filter、lambda高阶函数  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/02_advanced/03_高阶函数.ipynb) |
  | [04_迭代器与生成器.ipynb](https://github.com/shibing624/python-tutorial/blob/master/02_advanced/04_迭代器与生成器.ipynb)  | 迭代器和yield生成器  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/02_advanced/04_迭代器与生成器.ipynb) |
  | [05_上下文管理器.ipynb](https://github.com/shibing624/python-tutorial/blob/master/02_advanced/05_上下文管理器.ipynb)  | with语句  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/02_advanced/05_上下文管理器.ipynb) |
  | [06_装饰器.ipynb](https://github.com/shibing624/python-tutorial/blob/master/02_advanced/06_装饰器.ipynb)  | Decorator装饰器  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/02_advanced/06_装饰器.ipynb) |
  
  ## 第三阶段：
  
  学习一些机器学习和数据科学需要用到的库，在后续机器学习和深度学习过程中，numpy和sklearn是必要的

  | Notebook     |      知识点      |  Colab |
  |:----------|:-------------|---------:|
  | [01_Numpy数组.ipynb](https://github.com/shibing624/python-tutorial/blob/master/03_data_science/01_Numpy数组.ipynb)  | Numpy array数组  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/03_data_science/01_Numpy数组.ipynb) |
  | [02_Numpy索引.ipynb](https://github.com/shibing624/python-tutorial/blob/master/03_data_science/02_Numpy索引.ipynb)  | Numpy index索引  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/03_data_science/02_Numpy索引.ipynb) |
  | [03_Numpy方法.ipynb](https://github.com/shibing624/python-tutorial/blob/master/03_data_science/03_Numpy方法.ipynb)  | Numpy 方法  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/03_data_science/03_Numpy方法.ipynb) |
  | [04_Matpoltlib画图.ipynb](https://github.com/shibing624/python-tutorial/blob/master/03_data_science/04_Matpoltlib画图.ipynb)  | Matpoltlib画图  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/03_data_science/04_Matpoltlib画图.ipynb) |
  | [05_SciPy统计分布.ipynb](https://github.com/shibing624/python-tutorial/blob/master/03_data_science/05_SciPy统计分布.ipynb)  | Scipy统计分布  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/03_data_science/05_SciPy统计分布.ipynb) |
  | [06_SciPy曲线拟合.ipynb](https://github.com/shibing624/python-tutorial/blob/master/03_data_science/06_SciPy曲线拟合.ipynb)  | Scipy曲线  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/03_data_science/06_SciPy曲线拟合.ipynb) |
  | [07_Pandas数据类型.ipynb](https://github.com/shibing624/python-tutorial/blob/master/03_data_science/07_Pandas数据类型.ipynb)  | Pandas数据类型  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/03_data_science/07_Pandas数据类型.ipynb) |
  | [08_Pandas数据操作.ipynb](https://github.com/shibing624/python-tutorial/blob/master/03_data_science/08_Pandas数据操作.ipynb)  | Pandas操作  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/03_data_science/08_Pandas数据操作.ipynb) |
  | [09_Scikit-Learn分类.ipynb](https://github.com/shibing624/python-tutorial/blob/master/03_data_science/09_Scikit-Learn分类.ipynb)  | Scikit-Learn数据分类  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/03_data_science/09_Scikit-Learn分类.ipynb) |
  | [10_Scikit-Learn聚类.ipynb](https://github.com/shibing624/python-tutorial/blob/master/03_data_science/10_Scikit-Learn聚类.ipynb)  | Scikit-Learn聚类  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shibing624/python-tutorial/blob/master/03_data_science/10_Scikit-Learn聚类.ipynb) |

# 基础知识视频教程
[视频教程](https://www.bilibili.com/video/BV1qW4y1a7fU/?spm_id_from=333.337.search-card.all.click)

