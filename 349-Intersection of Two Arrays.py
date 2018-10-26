# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:59:48 2018

@author: hecongcong
"""

def intersection(nums1,nums2):
    nums1_set=set(nums1)
    nums2_set=set(nums2)
    if(nums1_set & nums2_set):
        return(list(nums1_set & nums2_set))
    else:
        return([])
    