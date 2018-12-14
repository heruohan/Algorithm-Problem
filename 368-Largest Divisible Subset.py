# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:19:24 2018

@author: hecongcong
"""

'''
The problem 368:Largest Divisible Subset
Given a set of distinct integers,find the largest subset such that every pair (Si,Sj) of elements in this subset satisfies:
Si%Sj==0 or Sj%Si==0.
If there are multiple solutions,return any subset is fine.

Example1:
Input:[1,2,3]
Output:[1,2](of course,[1,3] will also be ok)
Example2:
Input:[1,2,4,8]
Output:[1,2,3,8]
'''

'''
The answer:本题是给定一个集合，找出满足题意条件的最大子集，其中子集中的元素两两都要满足Si%Sj==0 or Sj%Si==0,本题可以采用动态规划的方法：
1.首先对nums进行排序，然后只需要考虑nums[i]%nums[j]==0,其中nums[i]>nums[j].
2.然后设置四个变量，分别为dp和pre_idx数组、max_lens和max_idx整型变量，其含义如下：
dp数组：其中dp[i]表示从nums[0]到nums[i]中满足条件的最大子集的长度.

pre_idx数组：其中pre_idx[i]是指当前元素nums[i]之前，满足nums[i]%nums[j]==0且dp[j]+1>dp[i]的条件(其中0<=j<i)，并且离nums[i]最近元素的索引,
既当前元素nums[i]最长子集路径，上一个元素的索引；

max_lens:整个数组nums的最大子集的长度；

max_idx:整个数组nums的最大子集终点元素的索引；
3.把上述四个变量求出来以后，在找出nums的最大子集；
代码如下.
'''

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
    return(res[::-1])  #需要对求出来的res进行翻转
   
    
    
    
    
    
    
    
    
