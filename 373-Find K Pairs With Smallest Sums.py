# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 23:00:03 2018

@author: hecongcong
"""

####解法1
class Solution:
    def KSmallestPairs(self,nums1,nums2,k):
        ret=[]
        lens1=len(nums1)
        lens2=len(nums2)
        for i in range(min(k,lens1)):
            for j in range(min(k,lens2)):
                ret.append([nums1[i],nums2[j]])
        sort_ret=sorted(ret,key=lambda x:x[0]+x[1])
        return(sort_ret[:min(k,lens1*lens2)])


####解法2
class Solution:
    def KSmallestPairs(self,nums1,nums2,k):
        import math
        lens1=len(nums1)
        lens2=len(nums2)
        ret=[]
        size=min(k,lens1*lens2)
        idx=[0]*lens1
        for i in range(size):
            cur=0
            sums=math.inf
            for j in range(lens1):
                if(idx[j]<lens2 and sums>nums1[j]+nums2[idx[j]]):
                    cur=j
                    sums=nums1[j]+nums2[idx[j]]
            ret.append([nums1[cur],nums2[idx[cur]]])
            idx[cur]+=1
        return(ret)
        
    
    
    
    
    
    
    
    
    
 