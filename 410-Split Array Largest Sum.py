# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:08:11 2019

@author: hecongcong
"""



#解法1：
class Solution:
    def splitArray(self,nums,m):
        import math
        lens=len(nums)
        sums=[0]*(lens+1)
        dp=[[math.inf]*(lens+1) for _ in range(m+1)]
        dp[0][0]=0
        for i in range(1,lens+1):
            sums[i]=sums[i-1]+nums[i-1]
        for i in range(1,m+1):
            for j in range(1,lens+1):
                for k in range(i-1,j):
                    val=max(dp[i-1][k],sums[j]-sums[k])
                    dp[i][j]=min(dp[i][j],val)
        return(dp[m][lens])




#解法2
class Solution:
    def splitArray(self,nums,m):
        left,right=0,0
        for i in range(len(nums)):
            left=max(left,nums[i])
            right+=nums[i]
        while(left<right):
            mid=(left+right)//2
            if(self.can_split(nums,m,mid)):
                right=mid
            else:
                left=mid+1
        return(left)
    
    def can_split(self,lst,m,mid):
        cursum=0
        count=1
        for i in range(len(lst)):
            cursum+=lst[i]
            if(cutrsum>mid):
                cursum=lst[i]
                count+=1
                if(count>m):
                    return(False)
        return(True)
        






