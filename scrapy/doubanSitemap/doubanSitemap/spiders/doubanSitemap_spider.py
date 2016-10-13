from scrapy.spiders import SitemapSpider

class DoubanSpider(SitemapSpider):
    stemap_urls = ['https://www.douban.com/robots.txt']

    def start_requests(self):
        requests = list(super(MySpider, self).start_requests())
        requests += [scrapy.Request(x, selff.parse_other) for x in self.other_urls]
        return requests
