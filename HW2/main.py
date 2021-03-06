'''
Yubo Feng stevens
HW2

extract information from html file which is downloaded by domain_crawler.py
'''
import re
import pandas as pd

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup as BSoup


def open_html(filename):
    '''
    open html file which is stored locally
    '''
    from os.path import exists

    if exists(filename):
        f = open(filename, 'rb')
        return f
    else:
        raise NameError('html file not exist')


if __name__ == '__main__':
    df_top_domain = {} # initiate a final output file
    
    html = open_html('top-level-domain.html')
    content = html.read().decode('utf-8')
    
    '''
    Using Regular Expression
    '''
    expression = re.compile('>(\.\S+?)</')
    df_top_domain['By_regular_expression'] = list(set(expression.findall(content)))
    
    
    
    '''
    Using beautiful soup to extract
    '''    
    soup = BSoup(content, 'lxml')
    
    top_domain_list = []
    tables = soup.select('table')
    for table in tables:
        for tr in table.select('tr')[1:]:
            for td in tr.select('td'):
                if td.a is None:
                    contents = td.contents
                    titles = [content for content in contents if '.' in content and len(content)<=25]
                    top_domain_list.extend(titles)
                else:
                    try:
                        title = td.a.attrs['title']
                    except KeyError:
                        pass
                    if title[0] == '.':
                        top_domain_list.append(title)
                
    df_top_domain['By_beautiful_soup'] = list(set(top_domain_list))
    
    '''
    Visit second level domain
    '''

    By_re = pd.DataFrame(df_top_domain['By_regular_expression'])
    By_bs = pd.DataFrame(df_top_domain['By_beautiful_soup'])
    
    availability = []
    for i in range(len(By_re)):
        domain = By_re[0][i]
        url = 'http://www.example' + domain
        try:
            response = requests.get(url)
            availability.append(response.status_code)
        except Exception:
            availability.append('404')
    By_re['status'] = availability
    

    By_bs[0] = By_bs[0].str.extract('(\.\S+)')
    availability = []
    for i in range(len(By_re)):
        domain = By_bs[0][i]
        
        try:
            url = 'http://www.example' + domain
            response = requests.get(url)
            availability.append(response.status_code)
        except Exception:
            availability.append('404')
    By_bs['status'] = availability

    




    '''
    Save file into csv file
    '''
    
    By_re.to_csv('top_level_domain_by_regular_expression.csv')
    By_bs.to_csv('top_level_domain_by_beautifulsoup.csv')
    
    
    
    
    
    
    
    
    
