#!/usr/bin/env python
# coding=utf-8

import scrapy
from scrapy.mail import MailSender

class ZhihuCSSpider(scrapy.Spider):
    name = "zhihu"
    start_urls = ["https://www.zhihu.com/topic/19580349/top-answers"]
    it = 0

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        nextfix = response.xpath('//div[@class="zm-invite-pager"]/span/a/@href').extract()[-1]
        if self.it < 50:
            self.it += 1
            yield scrapy.Request(response.urljoin(nextfix), callback=self.parse)
        suffixes = response.xpath('//div[@itemprop="question"]/link/@href').extract()
        for sufix in suffixes:
            url = response.urljoin(sufix)
            yield scrapy.Request(url, callback=self.parse_question)
    
    def parse_question(self, response):
        self.logger.info('Parse_question function called on %s', response.url)
        text = response.xpath('//div[@class="zm-editable-content clearfix"]')
        yield{
            'title': " ".join(response.xpath('//h2[@class="zm-item-title"]/a/text()').extract_first().split()),
            'url': response.url,
            'author': response.xpath('//a[@class="author-link"]/text()').extract_first(),
            'vote': response.xpath('//span[@class="count"]/text()').extract_first(),
            'content': " ".join(text.xpath('string(.)').extract_first().split()),
        }
    
#    def closed(self, spider):
#        self.logger.info('closed function called.')
#        stats = str(self.crawler.stats.get_stats())
#        mailer = MailSender(smtphost='smtp.qq.com', mailfrom='1092680402@qq.com', smtpuser='1092680402@qq.com', smtppass='xzdeelicvviybaee', smtpport=25)
#        mailer.send(to=["2443312135@qq.com"], subject="scrapy stats", body=stats)

