# -*- coding: utf-8 -*-
import scrapy
from blbl.items import BlblItem
import json

class BlSpider(scrapy.Spider):
    name = 'bl'
    allowed_domains = ['bilibili.com']
#start_urls默认为'http：//'+allowed_domains[0]
    #所以这里我们要重写start_urls，把排行榜页面的url列表赋值给start_urls
    start_urls = [
        'https://www.bilibili.com/ranking/all/0/0/30',
        'https://www.bilibili.com/ranking/all/1/0/30',
        'https://www.bilibili.com/ranking/all/168/0/30',
        'https://www.bilibili.com/ranking/all/3/0/30',
        'https://www.bilibili.com/ranking/all/129/0/30',
        'https://www.bilibili.com/ranking/all/4/0/30',
        'https://www.bilibili.com/ranking/all/36/0/30',
        'https://www.bilibili.com/ranking/all/188/0/30',
        'https://www.bilibili.com/ranking/all/160/0/30',
        'https://www.bilibili.com/ranking/all/119/0/30',
        'https://www.bilibili.com/ranking/all/155/0/30',
        'https://www.bilibili.com/ranking/all/5/0/30',
        'https://www.bilibili.com/ranking/all/181/0/30'
                  ]

    def parse(self, response):
    	#获取当前爬取的榜单
        rank_tab=response.xpath('//ul[@class="rank-tab"]/li[@class="active"]/text()').getall()[0]
        print('='*50,'当前爬取榜单为:',rank_tab,'='*50)

        #视频的信息都放在li标签中，这里先获取所有的li标签
        #之后遍历rank_lists获取每个视频的信息
        rank_lists=response.xpath('//ul[@class="rank-list"]/li')
        for rank_list in rank_lists:
            rank_num=rank_list.xpath('div[@class="num"]/text()').get()
            title=rank_list.xpath('div/div[@class="info"]/a/text()').get()
            # 抓取视频的url，切片后获得视频的id
            id=rank_list.xpath('div/div[@class="info"]/a/@href').get().split('/av')[-1]
            # 拼接详情页api的url
            Detail_link=f'https://api.bilibili.com/x/web-interface/archive/stat?aid={id}'
            Labels_link=f'https://api.bilibili.com/x/tag/archive/tags?aid={id}'
            author=rank_list.xpath('div/div[@class="info"]/div[@class="detail"]/a/span/text()').get()
            score=rank_list.xpath('div/div[@class="info"]/div[@class="pts"]/div/text()').get()
            #如用requests库发送请求，要再写多一次请求头
            # 因此我们继续使用Scrapy向api发送请求
            # 这里创建一个字典去储存我们已经抓到的数据
            # 这样能保证我们的详细数据和排行数据能一 一对应无需进一步合并
            # 如果这里直接给到Scrapy的Item的话，最后排行页的数据会有缺失
            items={
                'rank_tab':rank_tab,
                'rank_num' : rank_num ,
                'title' :title ,
                'id' : id ,
                'author' : author ,
                'score' : score ,
                'Detail_link':Detail_link
            }
            # 将api发送给调度器进行详情页的请求，通过meta传递排行页数据
            yield scrapy.Request(url=Labels_link,callback=self.Get_labels,meta={'item':items},dont_filter=True)

    def Get_labels(self,response):
        items=response.meta['item']
        Detail_link=items['Detail_link']
        # 解析json数据
        html=json.loads(response.body)
        Tags=html['data'] #视频标签数据
        tag_name=','.join([i['tag_name'] for i in Tags])
        items['tag_name']=tag_name
        yield scrapy.Request(url=Detail_link,callback=self.Get_detail,meta={'item':items},dont_filter=True)

    def Get_detail(self,response):
        # 获取排行页数据
        items=response.meta['item']
        rank_tab=items['rank_tab']
        rank_num=items['rank_num']
        title=items['title']
        id=items['id']
        author=items['author']
        score=items['score']
        tag_name=items['tag_name']

        # 解析json数据
        html=json.loads(response.body)

        # 获取详细播放信息
        stat=html['data']

        view=stat['view']
        danmaku =stat['danmaku']
        reply =stat['reply']
        favorite =stat['favorite']
        coin =stat['coin']
        share =stat['share']
        like =stat['like']
		#利用逗号分割列表，返回字符串

        # 把所有爬取的信息传递给Item
        item=BlblItem(
            rank_tab=rank_tab,
            rank_num = rank_num ,
            title = title ,
            id = id ,
            author = author ,
            score = score ,
            view = view ,
            danmaku = danmaku ,
            reply = reply ,
            favorite = favorite ,
            coin = coin ,
            share = share ,
            like = like ,
            tag_name = tag_name
        )
        yield item
