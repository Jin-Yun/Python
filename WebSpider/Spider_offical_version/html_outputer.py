#coding:utf8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_datas):
        if new_datas is None:
            return
        else:
            self.datas.append(new_datas)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        #迭代输出数据
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td" %data['url'].encode('utf-8'))
            fout.write("<td>%s</td" %data['title'].encode('utf-8'))
            fout.write("<td>%s</td" %data['summary'].encode('utf-8'))
            fout.write("</tr>")


        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

