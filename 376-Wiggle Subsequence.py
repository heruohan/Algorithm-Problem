# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 09:40:54 2019

@author: hecongcong
"""


####解法1
class Solution:
    def wiggleMaxLength(self,nums):
        lens=len(nums)
        if(lens<=1):
            return(lens)
        flags=[0]*lens
        dp=[1]*lens
        for i in range(1,lens):
            for j in range(i):
                if(j==0):
                    if(nums[i]>nums[j]):
                        dp[i]=dp[j]+1
                        flags[i]='+'
                    elif(nums[i]<nums[j]):
                        dp[i]=dp[j]+1
                        flags[i]='-'
                    else:
                        dp[i]=dp[j]
                else:
                    if(nums[i]>nums[j] and flags[j]=='-'):
                        dp[i]=max(dp[i],dp[j]+1)
                        flags[i]='+'
                    elif(nums[i]<nums[j] and flags[j]=='+'):
                        dp[i]=max(dp[i],dp[j]+1)
                        flags[i]='-'
        return(dp[-1])



####解法2
class Solution:
    def wiggleMaxLength(self,nums):
        lens=len(nums)
        if(lens<=1):
            return(lens)
        last_p=[1]*lens
        last_n=[1]*lens
        for i in range(1,lens):
            for j in range(i):
                if(nums[i]>nums[j]):
                    last_p[i]=max(last_p[i],last_n[j]+1)
                elif(nums[i]<nums[j]):
                    last_n[i]=max(last_n[i],last_p[j]+1)
        return(max(last_p[-1],last_n[-1]))




####解法3
class Solution:
    def wiggleMaxLength(self,nums):
        lens=len(nums)
        if(lens<=1):
            return(lens)
        last_p=1
        last_n=1
        for i in range(1,lens):
            if(nums[i]>nums[i-1]):
                last_p=last_n+1
            elif(nums[i]<nums[i-1]):
                last_n=last_p+1
        return(max(last_p,last_n))
        







