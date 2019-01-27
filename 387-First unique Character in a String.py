# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:49:31 2019

@author: hecongcong
"""


#解法1
class Solution:
    def firstUniqChar(self,s):
        sts=set()
        lens=len(s)
        for i in range(lens):
            if(s[i] not in sts and s[i] not in s[i+1:]):
                return(i)
            else:
                if(s[i] not in sts):
                    sts.add(s[i])
        return(-1)
        
            

#解法2
class Solution:
    def firstUniqChar(self,s):
        dic={}
        for i in s:
            if(i not in dic):
                dic[i]=1
            else:
                dic[i]+=1
        for i in range(len(s)):
            if(dic[s[i]]==1):
                return(i)
        return(-1)
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            