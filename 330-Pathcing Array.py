# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 02:15:41 2018

@author: hecongcong
"""

class Solution:
    def minPatches(self,nums,n):
        res=1
        count=0
        lens=len(nums)
        i=0
        while(True):
            if(res>n):
                return(count)
            if(i<lens):
                if(res<nums[i]):
                    res+=res
                    count+=1
                else:
                    res+=nums[i]
                    i+=1
            else:
                res+=res
                count+=1
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                    