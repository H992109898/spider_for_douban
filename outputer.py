# -*- coding: UTF-8 -*-

class outputer(object):

    def __init__(self):
        self.datas = []
        
    def collect_data(self, data):
        self.datas.append(data)
    
        
    def save_data(self):
        fout = open("output.html", "w")
    
        fout.write("<html>")
        fout.write("<body>")
        fout.write(r'<table border="1">')
    
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>Link: %s</td>" %data['url'].encode('utf8'))
            fout.write("<td>%s</td>" %data['title'].encode('utf8'))
            fout.write("<td>%s</td>" %data['score'].encode('utf8'))
            fout.write("<td>%s</td>" %data['summary'].encode('utf8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
    
        fout.close()

        
        