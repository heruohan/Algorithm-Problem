# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:23:37 2019

@author: hecongcong
"""



#解法1
class Solution:
    def removeKdigits(self,num,k):
        st=[]
        lens=len(num)
        diff=lens-k
        for i in num:
            while(st and k>0 and st[-1]>i):
                st.pop()
                k-=1
            st.append(i)
        while(st and st[0]=='0'):
            st.pop(0)
        while(len(st)>diff):
            st.pop()
        return(''.join(st) if(len(st)>0) else '0')



#解法2
class Solution:
    def removeKdigits(self,num,k):
        lens=len(num)
        diff=lens-k
        res=self.helps(num,k)
        while(len(res)>0 and res[0]=='0'):
            res=res.replace(res[0],'',1)
        while(len(res)>diff):
            res=res.replace(res[-1],'',1)
        return(res if(len(res)>0) else '0')
    
    def helps(self,nums,k):
        if(k==0):
            return(nums)
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                return(self.helps(nums[:i]+nums[i+1:],k-1))
        return(nums)











