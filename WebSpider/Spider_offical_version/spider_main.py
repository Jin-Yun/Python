# coding:utf8

import url_manager
import html_parser
import html_outputer
import html_downloader

class Spider(object):
    # 初始化爬虫类
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 记录爬取网页数量
        count = 0
        # 先将入口URL添加到URL管理器类中
        self.urls.add_new_url(root_url)
        # 判定是URL管理器中否有未抓取的URL
        while self.urls.has_new_url():
            # 从URL管理器pop一个未抓取队列中的一个URL
            new_url = self.urls.get_new_url()
            # 打印出是抓取个数 和当前 抓取网址
            print 'craw %d : %s' %(count,new_url)
            # 下载当前抓取的网址，并将下载内容返回给html_content
            html_content = self.downloader.download(new_url)
            # 解析下载的内容，并且将解析出的未抓取过得URL和符合正则匹配的数据返回
            new_urls,new_datas = self.parser.parse(new_url, html_content)
            print new_urls
            print new_datas
            # 将返回的未抓取的URL添加到URL未抓取队列中
            self.urls.add_new_urls(new_urls)
            #将返回的数据存储起来
            self.outputer.collect_data(new_datas)
            if count >= 1000:
                break
            count += 1
        # 迭代输出所有的有效数据
        self.outputer.output_html()

# 检测是否是主函数入口
if __name__ == "__main__":
    # 定义入口url
    root_url = "http://baike.baidu.com/view/21087.htm"
    # 实例化一个对象
    obj_spider = Spider()
    # 启动爬虫方法
    obj_spider.craw(root_url)
