# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 在item中定义相关属性
    nickname = scrapy.Field()   # 用户名
    id = scrapy.Field() #用户id
    score = scrapy.Field()  # 星级
    content = scrapy.Field() # 评论内容
    time = scrapy.Field()   # 评论创建时间

    pass
