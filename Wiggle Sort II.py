# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:33:15 2018

@author: hecongcong
"""

def wiggleSort(nums):
    lens=len(nums)
    nums1=sorted(nums)
    for i in range(1,lens,2):
        nums[i]=nums1.pop()
    for i in range(0,lens,2):
        nums[i]=nums1.pop()
    return(nums)