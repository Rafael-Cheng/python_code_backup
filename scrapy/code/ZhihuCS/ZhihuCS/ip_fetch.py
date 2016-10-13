import os
import requests

class Spider():
    def __init__(self, url):
        self.url = url
        self.PROXIES = []

    def fetchAvailable(self):
        page = requests.get(self.url).text
        ip_list = page.replace('\r\n', ' ').split(' ')
        for ip in ip_list:
#            pure = ip.split(':')[0]
#            print pure
#            status = os.system('ping -c 1 %s' % pure)
#            if status == 0:
            item = {'ip_port': str(ip), 'user_pass': ''}
            self.PROXIES.append(item)

    def writeToSettings(self):
        with open('settings.py', 'a') as f:
            f.write('PROXIES =' + str(self.PROXIES))
            f.close()

if __name__ == '__main__':
    url = 'http://api.xicidaili.com/free2016.txt'
    spider = Spider(url)
    spider.fetchAvailable()
    spider.writeToSettings()
