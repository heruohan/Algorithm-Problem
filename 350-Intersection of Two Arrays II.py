# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:10:29 2018

@author: hecongcong
"""

class Solution:
    def intersect(self,nums1,nums2):
        order_nums1=sorted(nums1)
        order_nums2=sorted(nums2)
        idx1=idx2=0
        res=[]
        while(idx1<len(nums1) and idx2<len(nums2)):
            if(order_nums1[idx1]==order_nums2[idx2]):
                res.append(order_nums1[idx1])
                idx1+=1
                idx2+=1
            elif(order_nums1[idx1]<order_nums2[idx2]):
                idx1+=1
            else:
                idx2+=1
        return(res)
        
        
        
        
        
        
        
        
        
        