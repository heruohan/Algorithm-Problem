# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 13:05:54 2018

@author: hecongcong
"""
'''
The question 354:Russian Roll Envelopes
    You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit
into another if and only if both the width and height of one envelope is greater than the width and height of the
other envelope.
    what is the maximum number of envelopes can you Russian doll?(put one inside other)
Note:Rotation is not allowed.

Example:
Input:[[5,4],[6,4],[6,7],[2,3]]
Output:3
Explanation:The maximum number of envelopes you can Russian doll is 3.([2,3]=>[5,4]=>[6,7]).
'''

'''
The answer:本题题意是给一堆信封，类似俄罗斯套娃一样，看最多能套多少个.
本题有两种解法，第一种是用动态规划的思想，第二种是把题目转换为寻找最长递增子序列的思想.
解法1：动态规划
先对envelopes进行排序，先按第一个元素进行升序排序，当第一个元素相等时，按第二个元素进行升序排序，
然后初始化一个元素为1的dp数组，dp[i]代表的含义为：以第i个envelope为尾，最多能叠多少个envelopes；其
状态转移方程为:dp[i]=max(dp[i],dp[j]+1),其中j<i,同时，envelopes[i][0]>envelopes[j][0] and 
envelopes[i][1]>envelopes[j][1];
代码如下.

解法2：longest increasing subsequence(二分法查找算法)
先对envelopes进行排序，先按第一个元素进行升序排序，当第一个元素相等时，按第二个元素进行降序排序，
这样排序的好处是当把二维的envelopes转化为一维的只对高度求最长递增子序列时，可以自动将宽度相等，
不能重叠的情况包含在内.现在的问题就变成了求高度的最长递增子序列.可以采用二分法查找算法求解.这样求解出来
的res数组，不一定是正确的最长递增子序列，但是其最长递增子序列的长度必定正确.
代码如下.
'''

#解法1
def maxEnvelopes1(envelopes):
    sort_envelopes=sorted(envelopes)
    lens=len(envelopes)
    if(lens==0):
        return(0)
    dp=[1]*lens
    for i in range(lens):
        for j in range(i):
            if(sort_envelopes[i][0]>sort_envelopes[j][0] and \
               sort_envelopes[i][1]>sort_envelopes[j][1]):
                dp[i]=max(dp[i],dp[j]+1)
    return(max(dp))

#解法2
def maxEnvelopes(envelopes):
    sort_envelopes=sorted(envelopes,key=lambda x:(x[0],-x[1]))
    res=[]
    for i in sort_envelopes:
        left=0
        right=len(res)
        num=i[1]
        while(left<right):
            mid=left+(right-left)//2
            if(res[mid]<num):
                left=mid+1
            else:
                right=mid
        
        if(right>=len(res)):
            res.append(num)
        else:
            res[right]=num
    return(len(res))
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
