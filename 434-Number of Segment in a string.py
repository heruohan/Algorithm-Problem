# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 13:33:04 2019

@author: hecongcong
"""



#解法1:
class Solution:
    def countSegments(self,s):
        lst=s.split()
        return(len(lst))



#解法2：
class Solution:
    def countSegment(self,s):
        s_diff=s.strip()
        res=0
        flag=False
        for i in s_diff:
            if(not flag and i==' '):
                res+=1
                flag=True
            elif(flag and i!=' '):
                flag=False
        return(res+1 if(s_diff) else res)



#解法3：
class Solution:
    def countSegment(self,s):
        res=0
        lens=len(s)
        i=0
        while(i<lens):
            if(s[i]==' '):
                i+=1
                continue
            res+=1
            while(i<lens and s[i]!=' '):
                i+=1
        return(res)
        



#解法4:
class Solution:
    def countSegment(self,s):
        res=0
        lens=len(s)
        for i in range(lens):
            if(s[i]!=' ' and (i==0 or s[i-1]==' ')):
                res+=1
        return(res)
        





