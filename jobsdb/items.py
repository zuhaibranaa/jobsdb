# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsdbItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    date = scrapy.Field()
    company_name = scrapy.Field()
    name = scrapy.Field()
    loc = scrapy.Field()
    card_url = scrapy.Field()
    job_point_1 = scrapy.Field()
    job_point_2 = scrapy.Field()
    job_point_3 = scrapy.Field()