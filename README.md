# 二次元属性被稀释，B站还剩什么？

文件介绍：
- blbl ：爬虫相关文件
    + scrapy.cfg ：项目的配置文件
    + blbl/blbl ：项目的Python模块，将会从这里引用代码
        + items.py ：项目的目标文件
        + pipelines.py ：项目的管道文件
        + settings.py ：项目的设置文件
        + spiders/ ：存储爬虫代码目录
            + bl.py ：爬虫文件，解析网页
- bilibili.csv: 爬取到的数据
- 数据分析实战部分：
    + 全站综合评分top100系列
    	+ 各分区占比情况可视化.py
    	+ 各分区平均情况数据处理.py
    	+ 平均三连情况可视化.py
    	+ 平均播放量情况可视化.py
    + 各区top100系列
    	+ 各分区播放量情况.py
    	+ 各分类情况.csv 
    + 数据预清洗
    + 热门标签.py
    + 热门标签词云.png
              