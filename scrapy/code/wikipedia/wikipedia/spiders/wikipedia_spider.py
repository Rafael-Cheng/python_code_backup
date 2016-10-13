import scrapy
from wikipedia.items import WikipediaItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']

    rules = (
        Rule(LinkExtractor(allow=('en\.wikipedia\.org')), callback='parse_item'),
    )

    def parse_item(self, response):
        item = WikipediaItem()
        item['name'] = response.xpath('//h1/text()').extract()
        item['url'] = response.url
        box = response.xpath('//div[@id="bodyContent"]')
        content = box.xpath('string(.)').extract()[0]
        item['content'] = " ".join(content.split())
        print item['name']
        print item['url']
        print item['content']
        return item
