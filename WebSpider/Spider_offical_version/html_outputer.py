#coding:utf8
# 输出类
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    # 将有效数据加入到datas【】中
    def collect_data(self, new_datas):
        if new_datas is None:
            return
        else:
            self.datas.append(new_datas)

    # 迭代输出data[]中的所有数据，注意encoding格式
    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        #迭代输出数据11111
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td" %data['url'].encode('utf-8'))
            fout.write("<td>%s</td" %data['title'].encode('utf-8'))
            fout.write("<td>%s</td" %data['summary'].encode('utf-8'))
            fout.write("</tr>")


        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

