# -*- coding: utf-8 -*-

# Scrapy settings for ZhihuCS project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ZhihuCS'

SPIDER_MODULES = ['ZhihuCS.spiders']
NEWSPIDER_MODULE = 'ZhihuCS.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ZhihuCS (+http://www.yourdomain.com)'
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ZhihuCS.middlewares.CustomMiddleWare': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#    'ZhihuCS.middlewares.RandomProxy.RandomProxy': 300,
    'ZhihuCS.middlewares.RandomUserAgent.RandomUserAgent': 200,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ZhihuCS.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
PROXIES =[{'ip_port': '111.240.246.59:8998', 'user_pass': ''}, {'ip_port': '121.31.103.156:8123', 'user_pass': ''}, {'ip_port': '60.162.39.142:8998', 'user_pass': ''}, {'ip_port': '115.29.37.86:8088', 'user_pass': ''}, {'ip_port': '111.206.81.248:80', 'user_pass': ''}, {'ip_port': '125.124.140.127:3128', 'user_pass': ''}, {'ip_port': '115.236.75.201:80', 'user_pass': ''}, {'ip_port': '121.31.174.113:8123', 'user_pass': ''}, {'ip_port': '156.17.77.166:3128', 'user_pass': ''}, {'ip_port': '120.24.62.9:808', 'user_pass': ''}, {'ip_port': '61.134.34.148:3128', 'user_pass': ''}, {'ip_port': '122.235.185.131:8118', 'user_pass': ''}, {'ip_port': '114.6.34.197:8080', 'user_pass': ''}, {'ip_port': '171.39.7.147:8123', 'user_pass': ''}, {'ip_port': '202.29.214.164:8080', 'user_pass': ''}, {'ip_port': '123.120.238.194:81', 'user_pass': ''}, {'ip_port': '212.122.189.90:3128', 'user_pass': ''}, {'ip_port': '112.232.14.35:8118', 'user_pass': ''}, {'ip_port': '43.243.112.87:3128', 'user_pass': ''}, {'ip_port': '122.193.77.194:81', 'user_pass': ''}, {'ip_port': '49.75.226.113:81', 'user_pass': ''}, {'ip_port': '180.109.15.183:8998', 'user_pass': ''}, {'ip_port': '61.160.212.74:3128', 'user_pass': ''}, {'ip_port': '49.64.175.180:8998', 'user_pass': ''}, {'ip_port': '171.38.197.112:8123', 'user_pass': ''}, {'ip_port': '143.202.76.72:8080', 'user_pass': ''}, {'ip_port': '124.93.222.71:8088', 'user_pass': ''}, {'ip_port': '101.109.79.102:8080', 'user_pass': ''}, {'ip_port': '182.90.74.228:8888', 'user_pass': ''}, {'ip_port': '200.205.13.82:8080', 'user_pass': ''}, {'ip_port': '113.250.109.103:8998', 'user_pass': ''}, {'ip_port': '94.179.60.178:3128', 'user_pass': ''}, {'ip_port': '185.5.223.48:8080', 'user_pass': ''}, {'ip_port': '103.24.127.198:8080', 'user_pass': ''}, {'ip_port': '62.45.248.11:80', 'user_pass': ''}, {'ip_port': '27.219.26.68:8888', 'user_pass': ''}, {'ip_port': '121.31.103.3:8123', 'user_pass': ''}, {'ip_port': '61.232.144.72:80', 'user_pass': ''}, {'ip_port': '119.53.126.249:8118', 'user_pass': ''}, {'ip_port': '202.93.128.58:3128', 'user_pass': ''}, {'ip_port': '1.182.232.203:8888', 'user_pass': ''}, {'ip_port': '123.201.210.36:8080', 'user_pass': ''}, {'ip_port': '120.1.73.35:81', 'user_pass': ''}, {'ip_port': '42.96.167.99:8088', 'user_pass': ''}, {'ip_port': '14.144.220.206:9999', 'user_pass': ''}, {'ip_port': '110.73.3.160:8123', 'user_pass': ''}, {'ip_port': '123.7.115.141:9999', 'user_pass': ''}, {'ip_port': '218.29.111.106:9999', 'user_pass': ''}, {'ip_port': '119.181.44.241:8888', 'user_pass': ''}, {'ip_port': '180.180.124.198:8080', 'user_pass': ''}, {'ip_port': '138.204.68.58:8080', 'user_pass': ''}, {'ip_port': '121.31.159.50:8123', 'user_pass': ''}, {'ip_port': '217.61.2.191:3128', 'user_pass': ''}, {'ip_port': '175.155.158.124:8118', 'user_pass': ''}, {'ip_port': '106.2.187.202:8080', 'user_pass': ''}, {'ip_port': '60.21.206.175:80', 'user_pass': ''}, {'ip_port': '202.107.238.51:3128', 'user_pass': ''}, {'ip_port': '182.90.111.121:80', 'user_pass': ''}, {'ip_port': '89.218.20.146:3128', 'user_pass': ''}, {'ip_port': '111.124.250.46:8888', 'user_pass': ''}, {'ip_port': '179.242.247.0:8080', 'user_pass': ''}, {'ip_port': '91.217.34.137:8080', 'user_pass': ''}, {'ip_port': '58.19.13.217:808', 'user_pass': ''}, {'ip_port': '27.207.1.89:81', 'user_pass': ''}, {'ip_port': '195.154.13.31:3128', 'user_pass': ''}, {'ip_port': '171.39.2.249:8123', 'user_pass': ''}, {'ip_port': '114.238.103.114:8998', 'user_pass': ''}, {'ip_port': '182.253.37.179:8080', 'user_pass': ''}, {'ip_port': '49.64.190.170:8998', 'user_pass': ''}, {'ip_port': '110.73.42.13:8123', 'user_pass': ''}, {'ip_port': '173.161.0.227:80', 'user_pass': ''}, {'ip_port': '222.128.154.252:81', 'user_pass': ''}, {'ip_port': '81.219.211.225:8080', 'user_pass': ''}, {'ip_port': '49.87.219.135:8998', 'user_pass': ''}, {'ip_port': '203.114.116.226:3128', 'user_pass': ''}, {'ip_port': '23.91.96.251:80', 'user_pass': ''}, {'ip_port': '119.130.31.24:9797', 'user_pass': ''}, {'ip_port': '37.46.85.149:80', 'user_pass': ''}, {'ip_port': '91.143.199.86:3128', 'user_pass': ''}, {'ip_port': '219.141.225.108:80', 'user_pass': ''}, {'ip_port': '103.21.77.118:8080', 'user_pass': ''}, {'ip_port': '121.248.112.20:3128', 'user_pass': ''}, {'ip_port': '82.139.108.47:80', 'user_pass': ''}, {'ip_port': '1.186.144.101:8080', 'user_pass': ''}, {'ip_port': '14.207.38.246:8080', 'user_pass': ''}, {'ip_port': '110.84.128.143:3128', 'user_pass': ''}, {'ip_port': '162.216.190.1:8080', 'user_pass': ''}, {'ip_port': '83.248.185.169:3128', 'user_pass': ''}, {'ip_port': '108.59.10.129:55555', 'user_pass': ''}, {'ip_port': '43.245.192.66:8080', 'user_pass': ''}, {'ip_port': '167.114.224.6:80', 'user_pass': ''}, {'ip_port': '171.38.242.82:8123', 'user_pass': ''}, {'ip_port': '39.1.37.125:8080', 'user_pass': ''}, {'ip_port': '13.67.211.33:3128', 'user_pass': ''}, {'ip_port': '163.25.107.65:808', 'user_pass': ''}, {'ip_port': '39.1.47.66:8080', 'user_pass': ''}, {'ip_port': '124.206.250.7:3128', 'user_pass': ''}, {'ip_port': '1.186.22.247:8080', 'user_pass': ''}, {'ip_port': '166.111.77.155:8998', 'user_pass': ''}, {'ip_port': '49.75.163.211:81', 'user_pass': ''}]
