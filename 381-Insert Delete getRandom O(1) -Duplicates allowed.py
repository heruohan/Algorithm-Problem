# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 23:21:57 2019

@author: hecongcong
"""


class RandomizedCollection:
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.lst=[]
        self.dic={}
    def insert(self,val):
        '''
        Inserts a value to the collection.Returns true if the
        collection did not already contain the specified element.
        '''
        if(val not in self.dic):
            self.lst.append(val)
            self.dic[val]=[len(self.lst)-1]
            return(True)
        else:
            self.lst.append(val)
            self.dic[val].append(len(self.lst)-1)
            return(False)
            
    def remove(self,val):
        '''
        Removes a value from the collection.Returns true if the
        collection contained the specified element.
        '''
        if(val not in self.dic):
            return(False)
        if(len(self.dic[val])==1):
            tmp=self.lst[-1]
            if(tmp==val):
                self.dic.pop(val)
                self.lst.pop()
            else:
                idx=self.dic[val][0]
                self.lst[idx]=tmp
                self.dic[tmp].append(idx)
                self.dic[tmp].remove(len(self.lst)-1)
                self.dic.pop(val)
                self.lst.pop()
        else:
            tmp=self.lst[-1]
            if(tmp==val):
                self.dic[val].remove(len(self.lst)-1)
                self.lst.pop()
            else:
                idx=self.dic[val][0]
                self.lst[idx]=tmp
                self.dic[tmp].append(idx)
                self.dic[tmp].remove(len(self.lst)-1)
                self.dic[val].remove(idx)
                self.lst.pop()
        return(True)
        
    def getRandom(self):
        '''
        Gets a random element from the collection.
        '''
        import random
        return(self.lst[random.randint(0,len(self.lst)-1)])
        
        
        
        
        
        
        
