# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlblItem(scrapy.Item):
    rank_tab=scrapy.Field()
    rank_num =scrapy.Field()
    id=scrapy.Field()
    title =scrapy.Field()
    author =scrapy.Field()
    score =scrapy.Field()
    view_num=scrapy.Field()
    danmaku=scrapy.Field()
    reply=scrapy.Field()
    favorite=scrapy.Field()
    coin=scrapy.Field()
    share_num=scrapy.Field()
    like_num=scrapy.Field()
    tag_name=scrapy.Field()