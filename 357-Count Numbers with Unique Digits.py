# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:21:38 2018

@author: hecongcong
"""
'''
The question 357:Count Numbers with Unique Digits
Given a non-negative integer n,count all numbers with unique digits,x,where 0<=x<10**n.

Example:
Input:2
Output:91
Explanation:The answer should be the total numbers in the range of 0<=x<100,
excluding 11,22,33,44,55,66,,77,88,99.
'''

'''
The answer:本题是在一个范围内找每个位置上不相同的数字，比如123则是，121则不是。
本题运用动态规划的思想，其中k代表位数，f(k)指全部的k位数满足条件的数字个数，如下：
初始状态：f(1)=10
状态方程为：f(k)=9*9*8......*(9-k+2)，其中k>=2
然后累加即可得出结果。
代码如下。
'''
####解法1
def countNumbersWithUniqueDigits(n):
    if(n==0):
        return(1)
    sums=10
    for i in range(2,n+1):
        end=11-i
        prob=9
        while(end<=9):
            prob*=end
            end+=1
        sums+=prob
    return(sums)



####解法2
def countNumbersWithUniqueDigits(n):
    if(n==0):
        return(1)
    sums=10
    prob=9
    for i in range(2,n+1):
        prob*=11-i
        sums+=prob
    return(sums)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
