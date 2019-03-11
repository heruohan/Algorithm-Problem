# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:14:58 2019

@author: hecongcong
"""




#解法1
class Solution:
    def findMaximumXOR(self,nums):
        res=0
        mask=0
        for i in range(31,-1,-1):
            mask |=(1<<i)
            st=set()
            for num in nums:
                st.add(num & mask)
            t=res | (1<<i)
            for s in st:
                if(s^t in st):
                    res=t
                    break
        return(res)
            
            
            
            
            
            
            
            
            
            
    