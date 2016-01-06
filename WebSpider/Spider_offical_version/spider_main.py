# coding:utf8

# 检测是否是主函数入口
import url_manager
import html_parser
import html_outputer
import html_downloader

class Spider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 0
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print 'craw %d : %s' %(count,new_url)
            html_content = self.downloader.download(new_url)
            new_urls,new_datas = self.parser.parse(new_url, html_content)
            print new_urls
            print new_datas
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_datas)
            if count >= 1000:
                break
            count += 1
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = Spider()
    obj_spider.craw(root_url)
