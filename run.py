import os
import urllib
from lxml import etree


class Splider(object):
    def __init__(self):
        '''
        初始化
        '''
        self.tieba_name = input('请输入要访问的贴吧:')
        self.begin_page = input('请输入起始页：')
        self.end_page = input('请输入终止页:')

        self.url = 'https://tieba.baidu.com/f'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"
        }
        # 图片编号
        self.user_name = 1
