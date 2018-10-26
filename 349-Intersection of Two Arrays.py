# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:59:48 2018

@author: hecongcong
"""
'''
The question 349:Intersection of Two Array
    Given two arrays, write a function to compute their intersection.

Example1:
Input:nums1 = [1,2,2,1], nums2 = [2,2]
Output:[2]

Example2:
Input:nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output:[4,9]

Note:
1.Each element in the result must be unique.
2.The result can be in any order.
'''

'''
The answer:本题的题意是给定两个数组，找出他们的交集部分，并且不能重复，不限制顺序.
本题可把两个数组nums1和nums2转换为集合nums1_set和nums2_set，然后在运用集合的交集运算，
如两者的交集非空，则用list()将集合转换为数组，并返回.否则，返回空集.
代码如下.
'''

def intersection(nums1,nums2):
    nums1_set=set(nums1)
    nums2_set=set(nums2)
    if(nums1_set & nums2_set):
        return(list(nums1_set & nums2_set))
    else:
        return([])
 




