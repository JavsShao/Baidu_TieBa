import re
import urllib.request


# 基本配置
url = 'https://tieba.baidu.com/p/5968543034'


class Splider(object):
    def getHtml(url):
        '''
        获取网页源码
        :param url:
        :return:
        '''
        page = urllib.request.urlopen(url)
        html = page.read()
        return html




if __name__ == '__main__':
    splider = Splider()
    splider.getHtml()