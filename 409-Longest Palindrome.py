# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 22:45:36 2019

@author: hecongcong
"""



#解法1
class Solution:
    def longestPalindrome(s):
        m={}
        for i in s:
            if(i not in m):
                m[i]=1
            else:
                m[i]+=1
        res=0
        count=0
        for i in m:
            if(m[i] % 2==0):
                res+=m[i]
            else:
                res+=(m[i]-1)
                count+=1
        return(res if(count==0) else res+1)



#解法2
class Solution:
    def longestPalindrome(s):
        a=set()
        for i in s:
            if(i not in a):
                a.add(i)
            else:
                a.remove(i)
        return(len(s)-max(0,len(a)-1))









