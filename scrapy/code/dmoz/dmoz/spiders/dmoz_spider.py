# -*- coding: utf-8 -*-
import scrapy
from dmoz.items import DmozItem

class DmozSpiderSpider(scrapy.Spider):
    name = "dmoz_spider"
    allowed_domains = ["http://www.dmoz.org"]
    start_urls = (
        'http://www.dmoz.org/Science/Math/Reference/',
    )

    def parse(self, response):
        lists = response.xpath('//div[@class="title-and-desc"]')
        for ls in lists:
            item = DmozItem()
            item['title'] = ls.xpath('.//div[@class="site-title"]/text()').extract_first()
            item['link'] = ls.xpath('./a/@href').extract_first()
            rawDesc = ls.xpath('./div[@class="site-descr "]/text()').extract_first()
            item['describe'] = " ".join(rawDesc.split())
            yield(item)
