# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 23:02:36 2019

@author: hecongcong
"""



#解法1：
class Solution:
    def compress(self,chars):
        lens=len(chars)
        i=0
        j=0
        cur=0
        while(i<lens):
            while(j<lens and chars[i]==chars[j]):
                j+=1
            if(i==j-1):
                chars[cur]=chars[i]
                cur+=1
                i=j
                continue
            chars[cur]=chars[i]
            for num in str(j-i):
                cur+=1
                chars[cur]=num
            i=j
            cur+=1
        for _ in range(lens-cur):
            chars.pop()
        return(cur)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    