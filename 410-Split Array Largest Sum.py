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
其中dp[i][j]可以分解为求Q=max(dp[i-1][k],sums[j]-sums[k]),i-1<=k<j,sums[j]表示前j个元素的累积和，其中所有Q值得最小值；
令T=sums[j]-sums[k],则前k个元素分为i-1份假设有count种分法，其中A，B，C...为前k个元素每种分割方法中和的最大值：
1、A,*,*,*...,*,T;
2、*,B,*,*..*，T；
3、*，*，*，C，*，T；
证明Q是dp[i-1][k]和T中的较大值，任意设C=dp[i-1][k],如下：
1.如果T<C,因此A>B>C>T,所以各个分组中的最大值为A,B,C,则Q=C，是dp[i-1][k]与T中的较大值；
2.如果T>C，则任意取第2种分法：
    a.如B>T,则第二种分法的最大值为B，第三种分法最大值为T，因为B>T,所以Q=T；
    b.如B<T,则第二种分法的最大值为T，第三种分法的最大值为T，因此，Q=T；
 因此，Q是dp[i-1][k]与T中的较大值；
综上所述，在任意情况下Q是dp[i-1][k]和T钟的较大值，证明完毕;
然后对于不同T的情况，因为Q是count种分法的中的最优解的局部最小值，因此，全局最优解dp[i][j]，是Q中的最小值；

解题步骤：
1.构建累积和数组sums.二维dp数组，dp[i][j]表示nums的前j个元素，被分成i份，满足题目条件的全局最优解；
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
        






