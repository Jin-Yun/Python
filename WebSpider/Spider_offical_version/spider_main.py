# coding:utf8

# 检测是否是主函数入口
import url_manager
import html_parser
import html_outputer
import html_downloader



class Spider(object):
    def __int__(self):
        self.urls = url_manager.UrlManager()
        self.downloder = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        pass


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = Spider()
    obj_spider.craw(root_url)
