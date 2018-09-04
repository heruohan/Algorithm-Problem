# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 12:29:14 2018

@author: hecongcong
"""
'''
Problem:
 322.Coin Change:
You are given coins of different denominations and a 
total amount of money amount.Write a function to compute 
the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any
combination of the coins, return -1.

Example:
Input:coins=[1,2,5], amount=11
Output:3
Explanation:11=5+5+1
'''
'''
Answer:
动态规划：初始化一个长度为amount+1的dp,dp[i]表示amount为i时的最小数量，
状态转移方程为：dp[i]=min(dp[i-coins[j]])+1,其中j=0,1,2....len(coins).

'''

def coinChange(coins,amount):
    dp=[0]+[-1]*amount
    for i in range(amount):
        if(dp[i]<0):   #
            continue
        for c in coins:
            if(i+c>amount):
                continue
            '''
            dp[i+c]未进行更新，或者dp[i+c]已进行更新，
            且已更新值dp[i+c]大于现有将更新值dp[i]+1;
            '''
            if(dp[i+c]<0 or dp[i+c]>dp[i]+1): 
                dp[i+c]=dp[i]+1
    return(dp[amount])
    
    
    
    
