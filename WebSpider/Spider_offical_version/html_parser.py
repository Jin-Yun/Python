#coding:utf8
import urlparse
from bs4 import BeautifulSoup
import re
# 解析下载的网页content
class HtmlParser(object):
    def __init__(self):
        pass
    #解析主函数
    def parse(self, new_url, html_content):
        if new_url is None or html_content is None:
            return
        else:
            # 申明soup
            soup = BeautifulSoup(html_content, 'html.parser',from_encoding='utf-8' )
            new_urls = self.get_new_urls(new_url, soup)
            new_datas = self.get_new_datas(new_url, soup)
            return new_urls,new_datas

    def get_new_urls(self, new_url, soup):
        #正则匹配类似于 /view/12334.htm
        new_full_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/"))
        print u'正则匹配结果'
        print links
        for link in links:
            newone = link['href']
            new_full_url = urlparse.urljoin(new_url, newone)
            new_full_urls.add(new_full_url)
        return new_full_urls

    def get_new_datas(self, new_url, soup):
        res_datas={}

        res_datas['url'] = new_url
        #抓取网页标题
        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_datas['title'] = title_node.get_text()

        #抓取网页摘要
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_datas['summary'] = summary_node.get_text()

        return res_datas



