import scrapy

from ..items import JobsdbItem

class Jobs(scrapy.Spider):
    name = 'jobs'
    start_urls = [
        'https://hk.jobsdb.com/hk/jobs/information-technology/1',
    ]
    def parse(self, response):
        cards = response.css('.lmSnC_0') # returning Company Names
        # yield {'card':cards}
        for card in cards:
            # yield {'card': card.extract()}
            item = JobsdbItem()
            date = card.css('time::attr(datetime)')
            company_name = card.css('div.sx2jih0.zcydq8bm>span.sx2jih0.zcydq84u._18qlyvc0._18qlyvc1x._18qlyvc1._18qlyvca::text')
            name = card.css('div.sx2jih0.l3gun70.l3gun74.l3gun72>span.sx2jih0::text')
            loc = card.css('div.sx2jih0>span.sx2jih0.zcydq84u._18qlyvc0._18qlyvc1x._18qlyvc3._18qlyvc7>span.sx2jih0.zcydq84u.zcydq80.iwjz4h0::text')
            card_url = card.css('div.sx2jih0.zcydq8bm>h1.sx2jih0.zcydq84u._18qlyvc0._18qlyvc1x._18qlyvc3._18qlyvca>a._1hr6tkx5._1hr6tkx8._1hr6tkxb.sx2jih0.sx2jihf.zcydq8h::attr(href)')
            job_point_1 = card.css('.zcydq86i:nth-child(1) .zcydq89i ._18qlyvc8::text')
            job_point_2 = card.css('.zcydq86i:nth-child(2) .zcydq89i ._18qlyvc8::text')
            job_point_3 = card.css('.zcydq86i~ .zcydq86i+ .zcydq86i ._18qlyvc8::text')
            id = card_url.extract()[0][-15:]
            
            item['id'] = id
            item['date'] = date.extract()[0]
            item['company_name'] = company_name.extract()[0]
            item['name'] = name.extract()[0]
            item['loc'] = loc.extract()
            item['card_url'] = card_url.extract()[0]
            item['job_point_1'] = job_point_1.extract()[0]
            item['job_point_2'] = job_point_2.extract()[0]
            item['job_point_3'] = job_point_3.extract()[0]
            yield item