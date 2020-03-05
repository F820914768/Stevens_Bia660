# -*- coding: utf-8 -*-


            

class Pipeline:
    '''
    A pipeline to send request, which has a limit depth recursion 
    '''
    def __init__(self, init_url, num_books, queue, 
                 crawler, max_depth):
        self.num_books = num_books
        self.queue = queue
        self.crawler = crawler
        self.queue.put(init_url)
        self.max_depth = max_depth
        
    def run(self):
        url, depth = self.queue.get()
        depth += 1
        page = self.crawler.get(url)
        hrefs = self.crawler.parse_url(page, depth,
                                       self.max_depth)
        if hrefs == None:
            return None
        for href in hrefs:
            self.queue.put_after_filter(href, depth)
        

        




