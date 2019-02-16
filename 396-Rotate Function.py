# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:19:38 2019

@author: hecongcong
"""



class Solution:
    def maxRotateFunction(self,A):
        lens=len(A)
        sums=0
        tmp=0
        for i in range(lens):
            sums+=A[i]
            tmp+=i*A[i]
        res=tmp
        for j in range(1,lens):
            tmp+=(sums-lens*A[lens-j])
            res=max(res,tmp)
        return(res)
        









