import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie

# 数据预清洗
def get_date():
    df=pd.read_csv('../bilibili.csv','\t')
    print(df.info())
    #波浪线~表示不选取该部分
    df_without_all=df[~df['rank_tab'].isin(['全站'])]
    return df_without_all

# 统计综合评分top100各区占比情况
def count_genre_top100(df):
    # 排序，切片，获取rank_tab列
    genres_rank_Series=df.sort_values(by='score',ascending=False)[:100]['rank_tab']
    #使用value_counts()方法快速求出各分区出现的次数
    geners_rank_count=genres_rank_Series.value_counts()
    print(geners_rank_count)
    print(type(geners_rank_count))
    return geners_rank_count

# 绘制玫瑰图
def pie_rosrtype(df):
    c=(
        Pie()
        .add(
            '',
            #添加数据，数据类型结构：[['生活', 30], ['动画', 20]]
            [list(z) for z in zip(df.index,df)],
            radius=['30%','75%'],
            center=['50%','50%'],
            rosetype="radius",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title='top100分类占比'))
        #设置标签，展现形式为 标签：数值
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    return c



if __name__ == '__main__':
    df_without_all=get_date()
    count_genre=count_genre_top100(df_without_all)
    pie=pie_rosrtype(count_genre)
    pie.render('综合评分top100各区占比情况.html')