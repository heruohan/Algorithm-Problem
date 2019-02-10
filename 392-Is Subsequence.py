# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 23:19:08 2019

@author: hecongcong
"""


#代码1
class Solution:
    def isSubsequence(self,s,t):
        i,j=0,0
        len_s=len(s)
        len_t=len(t)
        if(len_s==0):
            return(True)
        while(j<len_t):
            if(s[i]==t[j]):
                i+=1
                j+=1
            else:
                j+=1
            if(i>=len_s):
                return(True)
        return(False)
    

#代码2
class Solution:
    def isSubsequence(self,s,t):
        i,j=0,0
        len_s=len(s)
        len_t=len(t)
        if(len_s==0):
            return(True)
        while(i<len_s and j<len_t):
            if(s[i]==t[j]):
                i+=1
            j+=1
        return(i==len_s)







