#coding:utf8
# URL管理器类
class UrlManager(object):
    # 定义类的两个属性，set()不会重复， 可以用XXXin SET()快速判断是否在其中
    def __init__(self):
        # 一个为抓取队列一个已经抓取的队列
            self.new_urls = set()
            self.old_urls = set()
    # 添加一个未抓取过得URL
    def add_new_url(self, root_url):
        if root_url is None:
            return
        elif (root_url not in self.new_urls) and (root_url not in self.old_urls):
            self.new_urls.add(root_url)

    # 添加一批URL
    def add_new_urls(self, new_urls):
            if new_urls is None or len(new_urls)==0:
                return
            else:
                for urls in new_urls:
                    self.new_urls.add(urls)
    # 判断是否有未抓取的URL
    def has_new_url(self):
        return (len(self.new_urls) != 0)

    # pop一个未抓取的URL
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
