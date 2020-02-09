'''
Yubo Feng stevens
HW2

Create config.ini file to store configration
Load config.ini
'''


import configparser 


def get_url_from_config(filename='config.ini'):
    '''
    get the url that we are going to crawl from config.ini
    '''
    from urllib.parse import urlunsplit

    config = configparser.ConfigParser()
    config.read('config.ini') # read configration
    domain = config['url'].get('domain')
    protocal = config['url'].get('protocal')
    file_path = config['url'].get('path')

    url = urlunsplit([protocal, domain, file_path,'',''])
    return url

def get_headers_from_config(filename='config.ini'):
    '''
    get headers that are going to be use for crawler
    '''
    config = configparser.ConfigParser()
    config.read('config.ini') # read configration
    headers = {key: config['headers'].get(key) \
                for key in config['headers']}

    return headers

if __name__ == '__main__':
    
    '''
    Create config.ini file to store configration
    '''

    config = configparser.ConfigParser()

    config['url'] = {'protocal':'https', \
                    'domain':'en.m.wikipedia.org', \
                    'path':'wiki/List_of_Internet_top-level_domains'}

    config['headers'] = {'user-agent': 'a normal student'}


    with open('config.ini', 'w') as configfile:
        config.write(configfile)