# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 12:29:14 2018

@author: hecongcong
"""

def coinChange(coins,amount):
    dp=[0]+[-1]*amount
    for i in range(amount):
        if(dp[i]<0):
            continue
        for c in coins:
            if(i+c>amount):
                continue
            if(dp[i+c]<0 or dp[i+c]>dp[i]+1):
                dp[i+c]=dp[i]+1
    return(dp[amount])
    