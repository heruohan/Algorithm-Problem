# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 00:07:29 2019

@author: hecongcong
"""

class RandomizedSet:
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.lst=[]
        self.dic={}
    def insert(self,val):
        '''
        Inserts a value to the set.Returns True if the set did not
        already contain the specified element.
        :type val:int
        :rtype:bool
        '''
        if(val in self.dic):
            return(False)
        self.lst.append(val)
        self.dic[val]=len(self.lst)-1
        return(True)
        
    def remove(self,val):
        '''
        Removes a value from the set.Returns true if the set
        contained the specified element.
        :type val:int
        rtype:bool
        '''
        if(val not in self.dic):
            return(False)
        idx_val=self.dic[val]
        tmp=self.lst[-1]
        self.lst[idx_val],self.lst[-1]=self.lst[-1],self.lst[idx_val]
        self.dic[tmp]=idx_val
        self.dic.pop(val)
        self.lst.pop()
        return(True)
        
    def getRandom(self):
        '''
        Get a random element from the set.
        :rtype:int
        '''
        import random
        if(self.lst):
            return(self.lst[random.randint(0,len(self.lst)-1)])
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        