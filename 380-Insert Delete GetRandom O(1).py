# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 00:07:29 2019

@author: hecongcong
"""

'''
The problem 380:Insert Delete GetRandom O(1)
Design a data structrue that supports all following operations in average O(1) time.
1.insert(val):Inserts an item val to the set if not already present.
2.remove(val):Removes an item val from the set if present.
3.getrandom():returns a random element from current set of elements.each element must
have the same probability of being returned.

Example:
//init an empty set.
Randomizedset randomset=new RandomizedSet()

//inserts 1 to the set.returns true as 1 was inserted successfully.
randomset.insert(1)

//returns False as 2 dose not exits in the set.
randomset.remove(2)

//inserts 2 to the set,return true.set now contains [1,2].
randomset.insert(2)

//getRandom should return either 1 or 2 randomly.
randomset.getRandom()

//remove 1 from the set,return true.set now contains [2].
randomset.remove(1)

//2 was already in the set,so return false.
randomset.insert(2)

//since 2 is the only number in the set,getRandom always return 2.
randomset.getRandom()
'''


'''
The answer:本题是叫设计一个数据结构并支持插入，删除，和随机返回其中的元素操作,并且要在O(1)时间内完成.
由于在数组中删除元素并不是常数时间，而字典可以实现常数时间.因此，我们构建一个数组和一个字典，字典是数组
中的元素与其索引的映射，在删除操作中，我们将需要删除的元素与列表中最后一个元素互换位置，并同步修改字典中
的相关内容，这样就可以实现列表元素的常数时间删除了，相应也删除字典中的项.
代码如下.
'''

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
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
