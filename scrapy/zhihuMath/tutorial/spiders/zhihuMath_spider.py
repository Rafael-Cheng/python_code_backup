import sys
import scrapy
from tutorial.items import ZhihuItem
reload(sys)
sys.setdefaultencoding('utf-8')

class ZhihuMathSpider(scrapy.Spider):
    name = "zhihu"
    start_urls = [
        'https://www.zhihu.com/topic/19554091/top-answers',
    ]
    index = 1

    def parse(self, response):
        for question in response.xpath('//div[@itemprop="question"]/div/div/h2/a'):
            item = ZhihuItem()
            item['question'] = question.xpath('text()').extract()[0]
            item['link'] = 'https://www.zhihu.com' + question.xpath('@href').extract()[0]
            yield item

        self.index += 1
        next_page = self.start_urls[0] + '?page=' + str(self.index)
        if self.index <= 10:
            yield scrapy.Request(next_page, callback=self.parse)

