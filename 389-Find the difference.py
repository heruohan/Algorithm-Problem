# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:59:44 2019

@author: hecongcong
"""


#解法1
class Solution:
    def findTheDifference(self,s,t):
        dic={}
        for i in s:
            if(i not in dic):
                dic[i]=1
            else:
                dic[i]+=1
        for i in t:
            if(i not in dic or dic[i]==0):
                return(i)
            else:
                dic[i]-=1


#解法2
class Solution:
    def findTheDifference(self,s,t):
        lst_s=list(s)
        for i in t:
            if(i not in lst_s):
                return(i)
            else:
                lst_s.remove(i)
                

            
    
    
   