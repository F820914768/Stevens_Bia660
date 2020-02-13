
import os
import re
import threading
from queue import Queue
from urllib.parse import urlsplit, urlunsplit

from bs4 import BeautifulSoup
import selenium

    

class Crawler:
    '''
    a crawler object to send requests to url
    '''
    def __init__(self, path='./driver/chromedriver.exe'):
        from selenium import webdriver
        self.browse = webdriver.Chrome(path)
        self.cur_url = None

    def __repr__(self):
        return self.browse.page_source

    def get(self, url):
        print('>'*20,'visit->\n',url)
        response = self.browse.get(url)
        self.cur_url = url
        return response

    

    

class UrlQueue(Queue):
    '''
    A FIFO custom-made queue. Before put url into queue, the queue
    will check if input url is standard input, and whether input url 
    has been visited or not.
    
    The input url which is relative url will be made absolute. The url
    that's not in stevens.edu domain will not be put into queue.
    '''
    def __init__(self, protocal='https', domain='www.stevens.edu',
                key_word='www.stevens.edu', *kwargs):
        
        super(UrlQueue, self).__init__(*kwargs)
        self._site_visited = set() # to keep track of site that's visited
        self.domain = domain
        self.protocal = protocal
        self.key_word = key_word

    def put(self, url):
        
        url = url.lower().strip('/') # make url lower case
        scheme, netloc, path, query, fragment = urlsplit(url)
        if not scheme: # check whether the url is absolute url or not
            url = urlunsplit([self.protocal, self.domain, path,
                            query, fragment]) # make url absolute
    
        if self.key_word not in url: # check if the url is within domain
            return None
        
        if url not in self._site_visited: # check if the url is visited
            super(UrlQueue, self).put(url)
            self._site_visited.add(url)
            print('+'*20,'put in queue\n',url)


class Writer:
    '''
    an object to write iterable object into txt file
    '''
    def write(self, filename, iter_obj, type_='w'):
        with open(filename, type_) as f:
            for each in iter_obj:
                f.write(str(each)+'\n')


def write_file(url, content, root='./www.stevens.edu'):
    '''
    Copy the file architecture
    '''
    ini_cwd = os.getcwd() # record the initial work directory
    paths = urlsplit(url).path # get relative path of url
    if paths == '': 
        return None
    paths = paths.strip('/').split('/')
    os.chdir(root)
    print(paths)
    for dir_ in paths:
        if '.' in dir_:
            break
        if not os.path.exists(dir_):
            os.mkdir(dir_)
        os.chdir(dir_)
    try: # file name is too long to save on windows
        with open(dir_+'.html', 'wb') as f:
            f.write(content.encode('utf-8'))
    except FileNotFoundError:
        dir_ = dir_[:5]
        with open(dir_+'.html', 'wb') as f:
            f.write(content.encode('utf-8'))
    os.chdir(ini_cwd)




if __name__ == '__main__':
    q = UrlQueue() # queue isntance to get and put url
    crawler = Crawler() # crawler instance to send request
    writer = Writer()  # write emails into txt file
    emails_dic = set() # record all emails

    q.put('https://www.stevens.edu')
    
    os.mkdir('www.stevens.edu')
    for i in range(1000):
        print(i) # print the number of site visited
        
        url = q.get() # get a url from queue
        try:
            crawler.get(url) # send a request to given url
        except Exception as e:
            print(url,'！！！！！',e)
            continue
        soup = BeautifulSoup(crawler.browse.page_source, 'html.parser')

        write_file(url, crawler.browse.page_source)
        
        # extract email from response page
        rule_email = re.compile(r'[a-zA-Z]+\.?[a-zA-Z]+\.?[a-zA-Z]+@stevens\.edu')
        emails = rule_email.findall(crawler.browse.page_source)
        emails_dic = emails_dic.union(set(emails))
        
        # extract more urls from response page
        links = soup.find_all('a')
        for link in links:
            u = link.get('href')
            if u == None:
                continue
            q.put(u)
        print('#'*20, 'emails:\n', emails_dic) # print the email we have extracted currently
        
    

    
    writer.write('stevens_email_by_YuboFeng_BIA660.txt', emails_dic)

    

