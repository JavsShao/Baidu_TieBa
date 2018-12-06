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