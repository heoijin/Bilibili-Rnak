import pandas as pd
from pyecharts import  options as opts
from  pyecharts.charts import WordCloud


def get_date():
    df=pd.read_csv('bilibili.csv')
    # print(df.info())
    #波浪线~表示不选取该部分
    df_without_all=df[~df['rank_tab'].isin(['全站'])]
    return df_without_all

def build_tags_value(df):
	#获取tag_name标签下的数据
	#利用join为列表解嵌套，获得字符串
	#通过逗号对字符串进行拆分，获得无嵌套列表
	tag_list=','.join(df['tag_name']).split(',')
	#构造Series并调用.value_counts()
	tags_count=pd.Series(tag_list).value_counts()
	return tags_count

def wordcliud_base(df) :
    c=(
        WordCloud()
        .add(
            '',
            [list(z) for z in zip(df.index,df)],
            word_size_range=[5,100],
            shape='pentagon',
        )
        .set_global_opts(title_opts=opts.TitleOpts(title='热门标签'))
    )
    return c

if __name__ == '__main__':
    df_without_all=get_date()
    df_1=df_without_all.groupby(by='rank_tab')['title'].count()
    print(df_1)
    # tags_count=build_tags_value(df_without_all)
    # make_snapshot(snapshot,wordcliud_base(tags_count).render(),'热门标签词云.png')