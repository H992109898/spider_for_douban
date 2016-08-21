# -*- coding: UTF-8 -*-

from douban import url_manager, download, parser, outputer
import urllib2

class spider(object):
    def __init__(self):
        self.url_manager = url_manager.url_manager()
        self.download = download.download()
        self.parser = parser.parser()
        self.outputer = outputer.outputer()
        
    def craw(self, root_url):
        count = 1
        self.url_manager.add_new_url(root_url)
        while self.url_manager.has_new_url(): 
            try:
                new_url = self.url_manager.get_new_url()
                html = self.download.download_html(new_url)
                urls, data = self.parser.parser_html(new_url, html)
                self.url_manager.add_new_urls(urls)
                if data != None:
                    self.outputer.collect_data(data)
                    print "save No.%d movie." %count
                    if count == 50:
                        break
                    count += 1
            except urllib2.URLError, e:
                print e.reason
                
        self.outputer.save_data()
        
if __name__ == '__main__':
    obj = spider()
    obj.craw("https://movie.douban.com/subject/3592854/")
    
    