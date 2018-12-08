import re
import urllib.request

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