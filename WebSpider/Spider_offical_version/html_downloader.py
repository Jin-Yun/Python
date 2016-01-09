#coding:utf8
import urllib2

# 下载URL类
class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return
        response = urllib2.urlopen(new_url)
        if response.getcode() != 200:
            return
        elif response.getcode() == 200 :
            return response.read()