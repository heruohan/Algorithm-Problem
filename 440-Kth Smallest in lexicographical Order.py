# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 23:58:46 2019

@author: hecongcong
"""



#解法1：
class Solution:
    def findKthNumber(self,n,k):
        cur=1
        while(k>1):
            count=0
            start=cur
            end=cur+1
            while(start<=n):
                count+=min(end,n+1)-start
                start*=10
                end*=10
            if(k>count):
                cur+=1
                k-=count
            else:
                cur*=10
                k-=1
        return(cur)














