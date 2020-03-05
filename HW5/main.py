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


FILE_DOWNLOADED = False
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
    most_frequent_ent, max_frequency = analytics.get_most_frequent_ent(s)
    vec_15_first = analytics.get_vector(s)
    maxpair, max_similarity = analytics.max_similarity(s)
    
    print('then number of tokens is: ', num_tokens)
    print('then number of verbs is: ', num_verbs)
    print('the most frequent entity is: ', most_frequent_ent)
    print('then number of sentences is: ', num_sents)
    print('the most similar pair of sentences are: ', maxpair)
    print('word vector of  the first word in the 15th sentence \
          is \n {}'.format(vec_15_first))
    
    
    
    
    
    