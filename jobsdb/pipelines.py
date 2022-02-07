# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class JobsdbPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'mongodb://localhost:27017/*' 
        )
        self.db = self.conn['jobs']
        self.collection = self.db['jobs_list']
    
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
