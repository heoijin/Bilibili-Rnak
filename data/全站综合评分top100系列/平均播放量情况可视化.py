import pandas as pd
#构建图表用的库
from pyecharts import options as opts
from pyecharts.charts import  Bar

#调用js语句所需库
from pyecharts.commons.utils import JsCode

#转存为png所需库
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

#读取数据
def open_file():
    df=pd.read_csv('top100情况.csv','\t')
    title=df['genre'].tolist()
    view=df['view'].tolist()
    return title,view

#制作图表
def bar_border_radius(title,view):
    c=(
        Bar()
        .add_xaxis(title)
        .add_yaxis('平均播放量',view,category_gap=60)
        .set_series_opts(itemstyle_opts={
            'normal':{
            	#调用js语句，制作渐变颜色
                'color': JsCode("""new echarts.graphic.LinearGradient(0,0,0,1,[{
                    offset:0,
                    color:'rgba(0,244,255,1)'
                },{
                    offset:1,
                    color:'rgba(0,77,167,1)'
                }],false)"""),
                "barBorderRadius":[30,30,30,30],
                "shadowColor":'rgb(0,160,221)'
            }})
        .set_global_opts(title_opts=opts.TitleOpts(title='综合评分top100平均播放量情况'))
       )
    return c

if __name__ == '__main__':
    title,view=open_file()
    #正常情况下在调用制作图表的函数后添加.render()即可生成html文件
    #bar_border_radius(title,view).render()
    #这里一步将生成图表和转存为png
    make_snapshot(snapshot,bar_border_radius(title,view).render(),'全站top100播放量.png')
