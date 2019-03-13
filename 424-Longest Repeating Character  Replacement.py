# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:09:19 2019

@author: hecongcong
"""



#解法1：原始解法
class Solution:
    def characterReplacement(self,s,k):
        import copy
        res=0
        max_count=0
        start=0
        lens=len(s)
        count=[0]*26
        for i in range(lens):
            count[ord(s[i])-65]+=1
            tmp=copy.copy(count)
            max_count=max(tmp)
            while(i-start+1-max_count>k):
                tmp[ord(s[start])-65]-=1
                start+=1
                max_count=max(tmp)
            res=max(res,i-start+1)
            start=0
        return(res)
        




#解法2：优化解法
class Solution:
    def characterReplacement(self,s,k):
        res=0
        max_count=0
        start=0
        lens=len(s)
        count=[0]*26
        for i in range(lens):
            count[ord(s[i])-65]+=1
            max_count=max(count)
            while(i-start+1-max_count>k):
                count[ord(s[start])-65]-=1
                start+=1
                max_count=max(count)
            res=max(res,i-start+1)
        return(res)
        







