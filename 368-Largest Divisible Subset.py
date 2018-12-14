# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:19:24 2018

@author: hecongcong
"""


def largestDivisibleSubset(nums):
    lens=len(nums)
    if(lens==0):
        return([])
    nums.sort()
    dp=[1]*lens
    pre_idx=[0]*lens
    max_lens,max_idx=0,0
    for i in range(lens):
        for j in range(i):
            if(nums[i]%nums[j]==0 and dp[j]+1>dp[i]):
                dp[i]=dp[j]+1
                pre_idx[i]=j
        if(dp[i]>max_lens):
            max_lens=dp[i]
            max_idx=i
    res=[nums[max_idx]]
    for i in range(max_lens-1):
        max_idx=pre_idx[max_idx]
        res.append(nums[max_idx])
    return(res[::-1])
   
    
    
    
    
    
    
    
    