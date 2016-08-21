# -*- coding: UTF-8 -*-

import urllib2

class download(object):
    def __init__(self):
        self.header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'}
        
    
    def download_html(self, url):
        request = urllib2.Request(url, None, self.header)
        response = urllib2.urlopen(request)
        return response.read()
    