**请注意：该项目仅能在特定环境下运行，仅具有纪念意义，请不要期待该项目能在您的环境下运行，项目也不会继续维护，项目中的cluster1.py文件中有K-Means算法的经典实现**

## 简介

​        根据相关算法设计了一个文本聚类工具的原型，该工具利用网页爬虫从  http://www.leiphone.com 网站（注意：该网站已改版，这也是本项目不能运行的原因之一）获取大量文章的文本，经关键词提取步骤后再分别用两个不同的聚类器进行聚类，得到的结果以统计图等形式展现，其中，两个聚类器均基于K-Means算法设计，区别在于一个是K-Means算法的常规实现，另一个是针对本工具原型对K-Means算法的初始点选择方式进行了微调的实现。 

## 流程



1. 获取文章

 点击相应按钮后，能从 http://www.leiphone.com 上分别获取各个主题下的前10页文章，并将文章的纯文本部分提取出来后存放于对应的子文件目录中，每篇文章的文件名为其文章题目。

2. 中文分词

 点击相应按钮后，能对之前获取的文章进行分词和去除停用词，分词后的效果为每篇文章以空格隔开不同词语，最终结果保存在相应文件目录中。

3. 设置并提取关键词

 输入所要的关键词数量后，再点击相应执行按钮，将能以输入的数量要求提取关键词，并将每篇文章的关键词保存到对应文件中，每个文件的内容形式为：每个关键词和其权重占据一行，关键词后接一个制表符后加上它的TF-IDF权重。

4. 进行文本聚类

 这里将设计两个略微不同的聚类器，分别称为“1号聚类器 ”和“2号聚类器”，它们的区别在于初始点的选择方式不同，其中，“2号聚类器“所用的初始点选择方式为本文4.2.2节所述的初始点选择方式。两个聚类器的聚类结果存放在对应的文件中，其中，文件按不同类簇将文章题目进行划分。

5. 查看聚类结果

 聚类完毕后，可以通过条形图的形式展示每个聚类器的结果，也可以直接查看详细的统计结果。

## 模块



（1）文章获取模块。该模块实际上是一个网页爬虫，负责实现文章获取功能。

（2）分词模块。该模块负责实现中文分词功能和执行去停用词功能。

（3）停用词表模块。该模块事实上仅是一个简单的词表，结合分词模块使用。

（4）关键词提取模块。该模块利用TF-IDF算法对分词结果进行提取关键词。

（5）聚类器模块。这里设计了两个聚类器，实现对应的聚类功能。

 （6）聚类结果统计模块。该模块实现对结果进行简单汇总和计算功能。

（7）操作界面模块。该模块实现了简单的操作界面，能以可视化形式呈现各个类簇对应人工分类的结果，同时排布了一些按钮，方便执行某些操作。

## 各个模块的工作流程

（1）在操作模块中点击获取文章按钮，此时文章获取模块开始工作；

（2）文章获取模块将所获取的文章保存在相应目录中；

（3）在操作模块中点击分词按钮，此时分词模块开始工作；

（4）分词模块把切词结果保存在相应目录中；

（5）在操作模块中进行关键词提取操作，此时关键词提取模块开始工作；

（6）关键词提取模块将操作（4）得到的分词结果进行提取，结果保存在相应目录中；

（7）在操作模块中进行开始聚类操作，此时聚类器开始工作；

（8）聚类模块将操作（6）中得到的关键词结果进行聚类，结果保存在相应文件中；

（9）将操作（8）得到的结果反馈给操作模块。

## 开发和运行环境



 所用操作系统：Ubuntu 16.10(64bit)

 操作系统内核版本：Linux 4.8.0-49-generic

 所用的编程语言是Python，其中：

 语言版本：Python 3.5.2(64bit)

 语言解释器：CPython

 同时，由于开发需要，安装了以下第三方库：

 beautifulsoup4：版本号4.5.3

 jieba：版本号0.38

 numpy：版本号1.12.1

 scipy：版本号0.19.0

 scikit-learn：版本号0.18.1

 matplotlib：版本号2.0.0

 以上Linux下Python第三方库均使用Python包管理器pip安装，pip的版本号为：9.0.1。

