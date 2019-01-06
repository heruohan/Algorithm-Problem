# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:26:45 2019

@author: hecongcong
"""


class Solution:
    def combinationSum4(self,nums,target):
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for j in nums:
                if(i>=j):
                    dp[i]+=dp[i-j]
        return(dp[-1])
        