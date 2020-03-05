# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:24:12 2020

@author: 82091
"""

import requests
import utils
from lxml import etree


BASE_URL = 'https://www.gutenberg.org/'
HEADERS = {'user-agent':'student'}

class BaseCrawler:
    '''
    a crawler that will check if an url is absolute or not before sending request
    '''
    def __init__(self, base_url=BASE_URL,
                 headers = HEADERS):
        self.base_url = base_url
        self.missing_url = []
        self.headers = headers
        
    def get(self, url):
        url = utils.get_absolute(url, self.base_url)
        try:
            page = requests.get(url, headers=self.headers).content
        except Exception:
            self.missing_url.append(url)
            print('{} error'.format(url))
            return None
        return page
            
    def __repr__(self):
        return 'craw {}'.format(self.base_url)
    
    def parse_url(self, page, i=0, max_depth=3):
        if page and i <= max_depth:
            html = etree.HTML(page)
            hrefs = html.xpath('//@href')
            return hrefs
                    
                    
class BookCrawler(BaseCrawler):
    '''
    A crawler that will check if an url is absolute or not,\
    and will download the page into local directory if '.txt' is in the url
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def get(self, url):
        print('->'*10, '\n', 'visit: ', url)
        page = super().get(url)
        if '.txt' in url:
            filepath = utils.get_file_path(url)
            utils.save_txt(page, filepath)
            return None
        return page
        