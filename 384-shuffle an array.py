# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:38:53 2019

@author: hecongcong
"""


class Solution:
    def __init__(self,nums):
        '''
        :ype nums:List[int]
        '''
        self.lst=head
    def reset(self):
        '''
        resets the array to its original configuration and return it.
        :rtype:List[int]
        '''
        return(self.lst)
    def shuffle(self):
        '''
        returns a random shuffling of the array.
        :rtype:List[int]
        '''
        import random
        import copy
        cur_lst=copy.copy(self.lst)
        for idx,value in enumerate(cur_lst):
            j=random.randint(0,idx)
            cur_lst[idx],cur_lst[j]=cur_lst[j],value
        return(cur_lst)
        



