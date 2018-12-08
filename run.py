import os
import urllib
from lxml import etree


class Spider:
    def __init__(self):
        self.tiebaName = input("请需要访问的贴吧：")
        self.beginPage = int(input("请输入起始页："))
        self.endPage = int(input("请输入终止页："))

        self.url = 'http://tieba.baidu.com/f'
        self.ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}