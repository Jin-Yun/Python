#coding:utf8
import urllib2
import cookielib

url = "https://www.hao123.com/"

print(u"第一种URL下载方法")
response1 = urllib2.urlopen(url)
print response1.getcode()
# print len(response1.read())
html = response1.read()
print html

print(u"第二种下载网页方法-增加浏览器信息，伪装成浏览器")
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())
print response2.read()

# print(u"第三种方法-增加cookie信息")
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# urllib2.install_opener(opener)
# response3 = urllib2.urlopen(url)
# print response3.read()