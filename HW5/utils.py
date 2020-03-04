# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:24:12 2020

@author: 82091
"""


def get_absolute(url, base_url):
    from urllib.parse import urlsplit
    shceme, netloc = urlsplit(url)[:2]
    if shceme and netloc:
        return url
    else:
        return base_url + url

def save_txt(obj, filepath):
    with open(filepath, 'wb') as f:
        f.write(obj)
        print('save file to {}'.format(filepath))
        

def get_file_path(url):
    filename = url.strip().split('/')[-1]
    return './data/' + filename
    
def open_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    test = 'https://www.gutenberg.org/files/1342/1342-0.txt'
    print(get_file_path(test))