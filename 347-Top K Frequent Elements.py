# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 09:50:15 2018

@author: hecongcong
"""
'''
The question 347:Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example1:
Input:nums = [1,1,1,2,2,3], k = 2
Output:[1,2]

Example2:
Input:nums = [1,1,1,2,2,3], k = 2
Output:[1]

Note:you may assume k is always valid,1<=k<=number of unique elements.
'''

'''
The answer:本题是给定一个整数数组，返回出现最频繁的前k个元素.
本题用dict数据结构，将数组中的元素与其出现的次数一一映射，然后根据次数对其降序排列，
返回前K个元素.代码如下.

代码技巧：
第一：首先产生一个key为元素，value为出现频数的映射字典.
第二：然后运用dict.items()方法，将字典转换为元组列表，然后运用sorted函数,将其key关键字参数设为
operator.itemgetter(1),表示根据元素列表第二个元素进行排序.
'''
def topKFrequent(nums,k):
    import operator
    tabs={}
    res=[]
    for i in nums:
        if(i not in tabs):
            tabs[i]=1
        else:
            tabs[i]+=1
    ordered_lst=sorted(tabs.items(),key=operator.itemgetter(1),\
                       reverse=True)  #降序
    for i in range(k):
        res.append(ordered_lst[i][0])
    return(res)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
