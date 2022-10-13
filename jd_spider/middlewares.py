# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from jd_spider.settings import USER_AGENT_LIST
import random

# 随机ua
class RandomUA(object):

    def process_request(self,request,spider):
        # print(request.headers['User-Agent'])
        ua = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = ua
        pass

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

