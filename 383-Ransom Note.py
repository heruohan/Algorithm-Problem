# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:25:52 2019

@author: hecongcong
"""


#解法1
class Solution:
    def canConstruct(self,ransomNote,magazine):
        magazine_lst=list(magazine)
        for i in ransomNote:
            if(i not in magazine_lst):
                return(False)
            magazine_lst.remove(i)
        return(True)



#解法2
class Solution:
    def canConstruct(self,ransomNote,magazine):
        dic={}
        for i in magazine:
            if(i not in dic):
                dic[i]=1
            else:
                dic[i]+=1
        for i in ransomNote:
            if(i not in dic or dic[i]==0):
                return(False)
            dic[i]-=1
        return(True)
        
        
        
        
        
            