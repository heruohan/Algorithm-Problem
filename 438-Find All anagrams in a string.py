# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:59:47 2019

@author: hecongcong
"""



#解法1：
class Solution:
    def findAnagram(self,s,p):
        m={}
        m1={}
        res=[]
        len_s=len(s)
        len_p=len(p)
        if(len_s<len_p):
            return([])
        for i in range(len_p):
            m[p[i]]=m.get(p[i],0)+1
            m1[s[i]]=m1.get(s[i],0)+1
        if(m1==m):
            res.append(0)
        for i in range(1,len_s-len_p+1):
            if(s[i-1]==s[i+len_p-1]):
                if(m1==m):
                    res.append(i)
                    continue
            else:
                m1[s[i-1]]-=1
                if(m1[s[i-1]]==0):
                    m1.pop(s[i-1])
                m1[s[i+len_p-1]]=m1.get(s[i+len_p-1],0)+1
                if(m1==m):
                    res.append(i)
        return(res)
        
        



#解法2：滑动窗口法
class Solution:
    def findAnagram(self,s,p):
        import collections
        len_s=len(s)
        len_p=len(p)
        res=[]
        m=collections.defaultdict(int)
        count=len_p
        for i in p:
            m[i]+=1
        left,right=0,0
        while(right<len_s):
            if(m[s[right]]>=1):
                count-=1
            m[s[right]]-=1
            right+=1
            if(count==0):
                res.append(left)
            if(right-left==len_p):
                if(m[s[left]]>=0):
                    count+=1
                m[s[left]]+=1
                left+=1
        return(res)
        





