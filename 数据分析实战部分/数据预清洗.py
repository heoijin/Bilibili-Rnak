import pandas as pd


# 数据预清洗
def get_date():
    df=pd.read_csv('bilibili.csv')
    # print(df.info())
    #波浪线~表示不选取该部分
    df_without_all=df[~df['rank_tab'].isin(['全站'])]
    return df_without_all

# 获取各区平均情况数据处理
def genre_mean(df):
	genres_rank_df=df.sort_values(by='score',ascending=False)[:100]
	#将数据从float转为int来去除小数点
	genre_mean=genres_rank_df.groupby('rank_tab').mean().astype('int')
	genre_mean['genre']=genre_mean.index
	genre_mean.to_csv('top100情况.csv',encoding='utf-8-sig',index=False)

def get_rank_mean(df):
	df_group=df.groupby(by='rank_tab')
	rang_tab_mean=df_group.mean().drop(['id','rank_num'],axis=1)
	rang_tab_mean['genre']=rang_tab_mean.index
	rang_tab_mean.to_csv('各分类情况.csv',encoding='utf-8-sig',index=False)

if __name__ == '__main__':
    df_without_all=get_date()
    genre_mean(df_without_all)
    get_rank_mean(df_without_all)