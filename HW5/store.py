# -*- coding: utf-8 -*-

from queue import Queue


class BaseQueue(Queue):
    '''
    A queue that will not put the object that has been stored before
    
    >>> q_test = BaseQueue()
    >>> q_test.put(1); q_test.put(1); q_test.put(2)
    >>> print(q_test.get(), q_test.get())
    >>> (1, 0) (2, 0)
    '''
    def __init__(self):
        super().__init__()
        self.visited_ = {}
        
    def put(self, item, i=0):
        if item not in self.visited_:
            super().put(item)
            self.visited_[item] = i
    
    def get(self):
        item = super().get()
        depth = self.visited_[item]
        return item, depth
            

class KeyWordQueue(BaseQueue):
    '''
    A queue that only store an object once, \
    and only put object into queue when there are certain key words in the object
    
    >>> q_test = KeyWordQueue('book', 'txt')
    >>> q_test.put('I'); q_test.put('book1'); q_test.put('.txt')
    >>> print(q_test.get(), q_test.get())
    >>> ('I', 0) ('book1', 0)
    '''
    def __init__(self, *key_words):
        super().__init__()
        self.key_words = [keyword for keyword in key_words]
    
    def put_after_filter(self, item, depth=0):
        for key_word in self.key_words:
            if key_word in item:
                super().put(item, depth)
                print('+'*20, '\n', 'put: ', item)
                return None
            
class BaseStack(list):
     '''
    A stack that will not put the object that has been stored before
    '''
    def __init__(self):
        super().__init__()
        self.visited_ = {}
        
    def put(self, item, i=0):
        if item not in self.visited_:
            super().append(item)
            self.visited_[item] = i
    
    def get(self):
        item = super().pop()
        depth = self.visited_[item]
        return item, depth

class KeyWordStack(BaseStack):
    '''
    A stack that only store an object once, \
    and only put object into queue when there are certain key words in the object
    '''
    def __init__(self, *key_words):
        super().__init__()
        self.key_words = [keyword for keyword in key_words]
    
    def put_after_filter(self, item, depth=0):
        for key_word in self.key_words:
            if key_word in item:
                super().put(item, depth)
                print('+'*20, '\n', 'put: ', item)
                return None

    
if __name__ == "__main__":
    q_test = BaseStack()
    q_test.put('a')
    q_test.put('a')
    q_test.put('b')
    print(q_test.get())
    print(q_test.get())