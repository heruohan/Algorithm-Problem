# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 01:29:57 2018

@author: hecongcong
"""
'''
The question 343:Integer Break
    Given a positive integer n, break it into the sum of at least two positive integers and 
maximize the product of those integers. Return the maximum product you can get.

Example 1:
Input:2
Output:1
Explanation:2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input:10
Output:36
Explanation:10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note:you may assume that n is not less than 2. 
'''

'''
The answer:本题的题意是给定一个正整数n，把它分解成至少2个正整数之和，并且使他们的乘积最大,返回最大乘积.
本题有两种解法思路，第一种是运用动态规划，第二种是运用数学推倒找出规律.

解法1：动态规划(dynamic programming)
dp[i]:表示当正整数为i时，所能得到的最大乘积.
状态转移方程为：dp[i]=max(j*dp[i-j],max(dp[i],j*(i-j))),其中i>=3,1<=j<=i-1;
边界条件为:dp[0]=0,dp[1]=dp[2]=1;
或状态转移方程为：dp[i]=max(j*dp[i-j],dp[i]),其中i>=7,1<=j<=i-1;
边界条件为：dp[0]=0,dp[1]=dp[2]=1,dp[3]=2,dp[4]=4,dp[5]=5,dp[6]=9

解法2：数学推导
根据均值不等式，算术平均值大于等于几何平均值，

'''
#解法1
def integerBreak1(n):
    dp=[0]*(n+1)
    dp[1]=dp[2]=1
    for i in range(3,n+1):
        for j in range(1,i):
            dp[i]=max(j*dp[i-j],max(dp[i],j*(i-j)))
    return(dp[n])

def integerBreak2(n):
    if(n==2 or n==3):
        return(n-1)
    elif(n % 3==0):
        return(3**(n//3))
    elif(n % 3==1):
        return(2*2*3**((n-4)//3))
    elif(n % 3==2):
        return(2*3**((n-2)//3))
   













