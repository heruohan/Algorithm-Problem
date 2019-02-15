# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:50:43 2019

@author: hecongcong
"""



#解法1：
class Solution:
    def longestSubstring(self,s,k):
        res=0
        lens=len(s)
        i=0
        while(i+k<=lens):
            m={}
            mask=0
            idx=i
            for j in range(i,lens):
                diff=ord(s[j])-ord('a')
                m[diff]=m.get(diff,0)+1
                if(m[diff]<k):
                    mask|=(1<<diff)
                else:
                    mask&=~(1<<diff)
                if(mask==0):
                    res=max(res,j-i+1)
                    idx=j
            i=j+1
        return(res)
        
        
        
#解法2：代码1
class Solution:
    def longestSubstring(self,s,k):
        res=0
        lens=len(s)
        m={}
        flag=True
        idx=0
        for i in s:
            if(i not in s):
                m[i]=1
            else:
                m[i]+=1
        for j in range(lens):
            if(m[s[j]]<k):
                res=max(res,self.longestSubstring(s[idx:j],k))
                flag=False
                idx=j+1
        return(lens if(flag) else max(res,\
               self.longestSubstring(s[idx:lens],k)))
        
        
#解法2：代码2
class Solution:
    def longestSubstring(self,s,k):
        lens=len(s)
        if(lens<k):
            return(0)
        for i in set(s):
            if(s.count(i)<k):
                return(max(self.longestSubstring(t,k) \
                           for t in s.split(i)))
        return(lens)









