import scrapy

from ..items import JobsdbItem

class Jobs(scrapy.Spider):
    name = 'jobs'
    end_page = None
    start_page = input('Enter Your Start Range :  ')
    dump = input('Do You Want To Using End Limit Y/N :  ')
    if dump[0].upper() == 'Y':
        end_page = input('Enter Your End Range :  ')
    start_urls = [
        'https://hk.jobsdb.com/hk/jobs/information-technology/'+start_page,
    ]
    def parse(self, response):
        cards = response.css('.lmSnC_0') # Returning Individual Cards
        for card in cards: # Iterate Through Each Card
            item = JobsdbItem() # Item Object To Use Pipeline 
            # Data Extraction Using CSS Selector
            date = card.css('time::attr(datetime)')
            company_name = card.css('div.sx2jih0.zcydq8bm>span.sx2jih0.zcydq84u._18qlyvc0._18qlyvc1x._18qlyvc1._18qlyvca::text')
            name = card.css('div.sx2jih0.l3gun70.l3gun74.l3gun72>span.sx2jih0::text')
            loc = card.css('div.sx2jih0>span.sx2jih0.zcydq84u._18qlyvc0._18qlyvc1x._18qlyvc3._18qlyvc7>span.sx2jih0.zcydq84u.zcydq80.iwjz4h0::text')
            card_url = card.css('div.sx2jih0.zcydq8bm>h1.sx2jih0.zcydq84u._18qlyvc0._18qlyvc1x._18qlyvc3._18qlyvca>a._1hr6tkx5._1hr6tkx8._1hr6tkxb.sx2jih0.sx2jihf.zcydq8h::attr(href)')
            job_point_1 = card.css('.zcydq86i:nth-child(1) .zcydq89i ._18qlyvc8::text')
            job_point_2 = card.css('.zcydq86i:nth-child(2) .zcydq89i ._18qlyvc8::text')
            job_point_3 = card.css('.zcydq86i~ .zcydq86i+ .zcydq86i ._18qlyvc8::text')
            _id = card_url.extract()[0][-15:]
            # Passing Data To Item
            item['id'] = _id
            item['date'] = date.extract()[0]
            item['company_name'] = company_name.extract()
            item['name'] = name.extract()[0]
            item['loc'] = loc.extract()
            item['card_url'] = 'https://hk.jobsdb.com'+card_url.extract()[0]
            item['job_point_1'] = job_point_1.extract()
            item['job_point_2'] = job_point_2.extract()
            item['job_point_3'] = job_point_3.extract()
            yield item # Yielding Items
        # Preparing CallBack Functionality
        next_page = response.css('div.sx2jih0.zcydq856.zcydq8em>a.sx2jih0.zcydq896.zcydq886.zcydq8o.zcydq856.zcydq8ea.zcydq8h.zcydq8y.zcydq8x.IQYn5_0._18qlyvc14._18qlyvc17.zcydq832.zcydq835::attr(href)').getall()[-1]
        if next_page is not None:# Check If Value is Null
            if self.end_page is None:
                next_page = 'https://hk.jobsdb.com'+next_page
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
            else:
                if next_page[-1] <= self.end_page: # Check Page Limit Described
                    next_page = 'https://hk.jobsdb.com'+next_page
                    yield scrapy.Request(
                        response.urljoin(next_page),
                        callback=self.parse
                    )