# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 14:55:12 2019

@author: hecongcong
"""


class Solution:
    def lexicalOrder(self,n):
        res=[0]*n
        cur=1
        for i in range(n):
            res[i]=cur
            if(cur*10<=n):
                cur*=10
            else:
                if(cur>=n):
                    cur//=10
                cur+=1
                while(cur % 10==0):
                    cur//=10
        return(res)
        
        
        
        
        
        
        