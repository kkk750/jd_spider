import scrapy
import json
from jd_spider.items import JdSpiderItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    # allowed_domains = ['item.jd.com']
    # start_urls = []

    # 原网址去掉 callback=fetchJSON_comment98 无用参数
    # 根据&page=转到不同评论页（0,99）
    url_head = 'https://club.jd.com/comment/productPageComments.action?&productId=100019125569&score=0&sortType=5'
    url_middle = '&page='
    url_end = '&pageSize=10&isShadowSku=0&fold=1'

    # 爬取100页评论数据
    def start_requests(self):
        for i in range(0,100): # (0,100)
            url = self.url_head +self.url_middle + str(i) + self.url_end
            yield scrapy.Request(url=url, callback = self.parse)

    # 爬取每一页的评论
    def parse(self, response):
        # 转为json
        json_string = response.text
        data = json.loads(json_string)
        # 根据key找到对应的商品评论信息
        comments = data['comments']
        # 将解析的数据封装到item对象
        for i in range(len(comments)):
            item = JdSpiderItem()
            jd_nickname = comments[i]['nickname']
            jd_id = comments[i]['id']
            jd_content = comments[i]['content']
            jd_score = comments[i]['score']
            jd_time = comments[i]['creationTime']

            # 转为字典
            item["nickname"] = jd_nickname
            item["id"] = jd_id
            item["content"] = jd_content
            item["score"] = jd_score
            item["time"] = jd_time

            # print(jd_nickname)
            yield item # 将item提交给管道

