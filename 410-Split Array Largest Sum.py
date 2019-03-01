# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:08:11 2019

@author: hecongcong
"""


'''
The problem 410:Split Array Largest sum
Given an array which consists of non-negative integers and an integer m.you can split the array into m non-empty
continuous subarrays.write an algorithm to minimize the largest sum among these m subarrays.
Note:
if n is the length of array,assume the following constraints are satisfied:
1.1 ≤ n ≤ 1000
2.1 ≤ m ≤ min(50, n)
Examples:
input:nums= [7,2,5,10,8],m=2
output:18
Exlanation:there are four ways to split nums into two subarrays.
the best way is to split it into [7,2,5] and [10,8],where the largest sum
among the two subarrays is only 18.
'''



'''
The answer:本题是给定一个数组nums,和一个整数m，把nums分成连续的m个非空子数组，求出所有分法中m个子数组中和的最大值中的最小值；
本题比较难，有以下两种解法，如下：

解法1：动态规划
思路：首先构建一个二维数组dp,初始化为最大值，dp[i][j]表示nums的前j个元素，被分成i份，满足题目条件的最优解,其中i的取值可为1<=i<=j;
其中dp[i][j]可以分解为求max(dp[i-1][k],sums[j]-sums[k]),i-1<=k<j,sums[j]表示前j个元素的累积和，其中所有值得最小值；
令Q=sums[j]-sums[k],则前k个元素分为i-1份假设有count中分法，为A,*,*,*...,*,Q;*,B,*,*..
'''


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
        






