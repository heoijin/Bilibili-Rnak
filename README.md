# 二次元属性被稀释，B站还剩什么？

Bilbili排行榜爬虫、数据分析和可视化实战

CSDN主页：https://me.csdn.net/weixin_40679090

系列文章：
- 上篇 - 爬虫篇：https://blog.csdn.net/weixin_40679090/article/details/104393399
- 下篇 - 对比分析和可视化：正在路上
- 番外篇 - 相关性分析：正在路上

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
              