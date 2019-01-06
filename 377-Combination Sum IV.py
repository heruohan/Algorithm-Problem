# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:26:45 2019

@author: hecongcong
"""

'''
The problem 377：Combination Sum IV
    Given an integer array with all positive numbers and no duplicates,find the number of possible combinations that add up to
a positive integer target.

Example:
Input:nums=[1,2,3],target=4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3,1)

Note that different sequences are counted as different combinations.
Therefore the output is 7.
'''


'''
The answer:本题是给定一个无重复的正整数数组nums，找出其中的元素相加等于给定的一个正整数target的所有组合数，其中要考虑组合顺序的不同情况.
本题可以采用动态规划的思想进行求解，具体如下：
1.构建一个长度为target+1的一维数组dp,其中含义如下，
dp[i]:表示target为i时，满足题意给定数组nums及其他条件的所有解的个数.
2.对于每个i，依次在nums中循环，然后进行累加，这样同时也考虑了序列的顺序，循环完毕后，即为满足题意条件，target=i时的所有不同顺序的组合数.
代码如下.
'''


class Solution:
    def combinationSum4(self,nums,target):
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for j in nums:
                if(i>=j):  #因为都是正数，所以不考虑负数的情况
                    dp[i]+=dp[i-j]
        return(dp[-1])
    
    
    
    
    
