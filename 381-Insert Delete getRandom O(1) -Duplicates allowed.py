# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 23:21:57 2019

@author: hecongcong
"""

'''
The problem 381:Insert Delete getRandom O(1)--Duplicates allowed
Design a data structrue that supports all following operations in average O(1) time.
Note:Duplicates element are allowed.
1.insert(val):inserts an item val to the collection.
2.remove(val):removes an item val from the collection if present.
3.getrandom():returns a random element from current collection of elements.The probability of each element
being returned is linearly related to the number of same value the collection contains.

Example:
//init an empty collection.
randomizedcollection collection=new randomizedcollection()

//inserts 1 to the collection.returns true as the collection did not contain 1.
collection.insert(1)

//insert another 1 to the collection.returns false as the collection contained 1.
collection now contains [1,1].
collection.insert(1)

//inserts 2 to the collection,returns true.collection now contains [1,1,2].
collection.insert(2)

//getrandom should return 1 with the probability 2/3,and return 2 with the probability.
collection.getRandom()

//removes 1 from the collection,returns true.collection now contains [1,2]
collection.remove(1)

//getrandom should return 1 and 2 both equally likely.
collection.getRandom().
'''

'''
The answer:本题是叫涉及一个数据结构，满足插入、删除及随即返回元素操作，并且允许重复.
因为允许重复，所以一个相同的元素可能对应多个位置的映射，因此构造一个字典，key是元素，value是位置的列表集合，
当要删除一个元素时，也是用在数组中把val和数组最后一个元素交换，但是需要考虑以下两种情况：
第一种：所删除的元素只有唯一一个时，既在字典中需要把整个列表都删除掉.
第二种：当所要删除的元素和最后一个元素相同时，就不用互换位置，直接将其删除掉.
'''
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
        
        
        
        
        
        
        
