import os
import urllib
from lxml import etree


class Spider(object):
    def __init__(self):
        '''
        初始化
        '''
        self.Tieba_Name = input('请输入要访问的贴吧:')
        self.bengin_Page = int(input('请输入起始页:'))
        self.end_Page = int(input('请输入终止页:'))

        self.url = 'https://tieba.baidu.com/f'
        self.ua_header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

        # 图片编码
        self.user_name = 1

    def tiebaSpider(self):
        '''

        :return:
        '''
        for page in range(self.bengin_Page, self.end_Page + 1):
            pn = (page - 1) * 50
            word = {'pn' : pn, 'kw':self.Tieba_Name}

            word = urllib.urlencode(word)
            my_url = self.url + "?" + word

            links = self.loadPage(my_url)

    def loadPage(self, url):
        '''
        读取页面
        :param url:
        :return:
        '''
        request = urllib.Request(url, headers=self.ua_header)
        html = urllib.urlopen(request).read()

        selector = etree.HTML(html)
        links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        for link in links:
            link = "http://tieba.baidu.com" + link
            self.loadImages(link)