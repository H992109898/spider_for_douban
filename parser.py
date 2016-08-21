# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import re

class parser(object):
        
    def parser_html(self, url, html):
        soup = BeautifulSoup(html, "html.parser", from_encoding='utf8')
        
        data = {}
        urls = self.get_urls(url, soup)
        data['score'] = self.get_score(url, soup)
        if float(data['score']) < 8.5:
            return urls, None
        data['url'] = url
        data['title'] = self.get_title(url, soup)
        data['summary'] = self.get_summary(url, soup)
        
        return urls, data
    
    def get_score(self, url, soup):
        #<strong class="ll rating_num" property="v:average">9.1</strong>
        score = soup.find('strong',  class_ = "ll rating_num")
        return score.get_text()
    
    def get_title(self, url, soup):
        #<div id="content">
        title = soup.find('div', id = "content").find('h1')
        return title.get_text()
    
    def get_summary(self, url, soup):
        #<span property="v:summary" class="">
        summary = soup.find('span', property="v:summary")
        return summary.get_text()
    
    def get_urls(self, url, soup):
        #<a href="https://movie.douban.com/subject/25786060/?from=subject-page" class="">
        links = soup.find_all('a', href = re.compile(r"https://movie.douban.com/subject/\d+/\?from=subject-page"))
        urls = set()
        for link in links:
            L = link['href'].split('/')
            tot = len(link['href'])
            cutted = len(L[-1])
            urls.add(link['href'][0:tot-cutted])
        
        return urls
        