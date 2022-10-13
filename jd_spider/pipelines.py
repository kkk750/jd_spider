# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

# 将数据存储到本地文件中
class JdSpiderPipeline(object):
    fp = None
    # 重写父类的方法，该方法只在开始爬虫时被调用一次
    def open_spider(self,spider):
        print('开始爬虫...')
        self.fp = open('./comment_data.txt','w',encoding='utf-8')

    # 接收提交的item对象
    # 每接收一个item就会被调用一次
    def process_item(self, item, spider):

        nickname = str(item['nickname'])
        id = str(item['id'])
        score = str(item['score'])
        content = str(item['content'])
        time = str(item['time'])
        self.fp.write('\n'+'nickname:'+nickname+\
                      '\n'+'id:'+id+\
                      '\n'+'score:'+score+\
                      '\n'+'content:'+content+\
                      '\n'+'time:'+time+\
                      '\n')
        # 传递给下一个即将被执行的管道类
        return item

    def close_spider(self,spider):
        print('结束爬虫')
        self.fp.close()



# 将数据存储到数据库中
class MysqlPipeLine(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='localhost',port=3306,user='root',password='0123698745',db='spider')

    def process_item(self,item,spider):
        # 创建一个游标对象
        self.cursor = self.conn.cursor()

        nickname = str(item['nickname'])
        id = str(item['id'])
        score = str(item['score'])
        content = str(item['content'])
        time = str(item['time'])

        try:
            self.cursor.execute('insert into comment values("%s","%s","%s","%s","%s")' %(nickname,id,score,content,time) )
            self.cursor.connection.commit()
        except Exception as e:
            print('data base failed:',e)
            self.conn.rollback()

        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
