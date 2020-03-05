# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:24:12 2020

@author: 82091
"""


def count_tokens(s):
    return len(s)

def count_verbs(s):
    verb_count = 0
    for word in s:
        if word.pos_ == 'VERB':
            verb_count += 1
    return verb_count


def count_sentences(s):
    sent_count = 0
    sents = s.sents
    for sent in sents:
        sent_count += 1
    return sent_count


def get_vector(s, i=15):
    sents = s.sents
    for i in range(15):
        sent = next(sents)
    token = sent[0]
    return token, token.vector

def get_most_frequent_ent(s):
    '''
    find the most frequent named entity in corpus
    '''
    most_frequent_ent = None
    max_frequency = 0
    ent_dict = {}
    for ent in s.sents:
        if ent not in ent_dict:
            ent_dict[ent] = 0
        ent_dict[ent] += 1
        if ent_dict[ent] > max_frequency:
            max_frequency = ent_dict[ent]
            most_frequent_ent = ent_dict[ent]
    return most_frequent_ent, max_frequency
        

def max_similarity(s):
    '''
    find the most similar pair of sentences
    '''
    from tqdm import tqdm
    max_similarity = 0
    sents = [sent for sent in s.sents 
             if len(sent) >= 10] # get all sents of length greater than 10
    for i in tqdm(range(len(sents))): # Loop through all sents
        sent_1 = sents[i]
        for j in range(i+1, len(sents)):
            sent_2 = sents[j]
            if sent_1 == sent_2: # the sentences shouldn't be identical
                continue
            similarity = sent_1.similarity(sent_2)
            if similarity > max_similarity:
                max_similarity = similarity
                maxpair = [sent_1, sent_2]
    return maxpair, max_similarity




    