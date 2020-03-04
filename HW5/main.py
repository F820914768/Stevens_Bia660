# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:24:12 2020

@author: 82091
"""
import time
import os
import random

import utils
import analytics
from crawler import BookCrawler
from pipeline import Pipeline
from store import KeyWordStack

import spacy
from tqdm import tqdm


FILE_DOWNLOADED = True
INIT_URL = 'https://www.gutenberg.org/browse/scores/top/'

if __name__ == '__main__':
    
    
    stack = KeyWordStack('book', 'txt')
    crawler = BookCrawler()
    pipeline = Pipeline(INIT_URL, 10, stack, crawler, 2)
    
    if not FILE_DOWNLOADED:
        for i in tqdm(range(100)):
            pipeline.run()
            time.sleep(0.5)
    
    bookpaths = os.listdir('./data')
    bookpath = './data/' + random.choice(bookpaths)
    book = utils.open_txt(bookpath)
    book = book.replace('\n', '')
    
    nlp = spacy.load('en_core_web_lg')
    s = nlp(book)
    
    num_tokens = analytics.count_tokens(s)
    num_verbs = analytics.count_verbs(s)
    num_sents = analytics.count_sentences(s)
    vec_15_first = analytics.get_vector(s)
    maxpair, max_similarity = analytics.max_similarity(s)
    