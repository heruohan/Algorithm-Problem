# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 09:40:54 2019

@author: hecongcong
"""

'''
The Problem 376:Wiggle Subsequence
    A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly  alternate
between positive and negative.The first difference(if one exist) may be either positive or nenative.A sequence with fewer
than two elements is trivially a wiggle sequence.
    For example,[1,7,4,9,2,5] is a wiggle sequence because the difference (6,-3,5,-7,3) are alternately positive and negative.
In contract,[1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequence,the first because its first two differences are positive and the
second because its last difference are zero.
    Given a sequence of integers,return the length of the longest subsequence that is a wiggle sequence.A subsequence is obtained
by deleting some numbers of elements(eventually,also zero) from the original sequence,leaving the remaining elements in there 
original order.


Example1:
Input:[1,7,4,9,2,5]
Output:6
Explanation:the entire sequence is a wiggle sequence.
Example2:
Input:[1,17,5,10,13,15,10,5,16,8]
Ouput:7
Explanation:there are several subsequences that achieve this length.one is [1,17,10,13,10,16,8].
Example3:
Input:[1,2,3,4,5,6,7,8,9]
Output:2

Follow up:
Can you do it in O(n) time?
'''


'''
The answer:本题的题意是给定一个序列，找出其最长摇摆子序列的长度，可以采用动态规划和贪心算法两种方法进行求解.

解法1：
此解法本质上是一种动态规划的方法，首先构造两个数组flags和dp,分别表示如下：
flags[i]:从nums[0]到nums[i]形成的最长摇摆子序列，其与前一个元素之差的符号，大于0即为'+'，反之亦然.
dp[i]:表示从nums[0]到nums[i]形成的最长摇摆子序列的长度.
代码如下.


解法2：
本解法本质也是一种动态规划的方法，首先构造两个数组last_p和last_n,分别表示如下：
last_p[i]:从nums[0]到nums[i]，以nums[i]为结尾且nums[i]与其前一个元素之差为正数的最长摇摆子序列的长度.
last_n[i]:表示从nums[0]到nums[i]，以nums[i]为结尾且nums[i]与其前一个元素之差为负数的最长摇摆子序列的长度.
且一个序列的最长摇摆子序列一定可以包含序列的最后一个元素.代码如下.


解法3：O(n)的时间复杂度.
本解法为贪心算法，因为一个序列的最长子序列必定包含其最后一个元素，且其形成的最长子序列可以分为两种情况，第一种情况为
包含其的最长子序列，最后的差为正；第二种情况为包含其的最长子序列，最后的差为负；比如nums=[1,17,5,10,20],最后差为正的
最长子序列为[1,17,5,20],最后差为负的最长子序列为[20];则其最长子序列为[1,17,5,20],长度为4.
因此，可以构建两个整形变量last_p=1和last_n=1,分别表示如下：
last_p:当循环到nums[i]时，如果nums[i]与nums[i-1]之差为正，则代表以nums[i]为尾的最长摇摆子序列长度,否则代表nums[:i]中
最后差值为正的最长子序列(可以不包含nums[i])的长度.
last_n:当循环到nums[i]时，如果nums[i]与nums[i-1]之差为负，则代表以nums[i]为尾的最长摇摆子序列的长度,否则代表nums[:i]中
最后差值为负的最长子序列(可以不包含nums[i])的长度.
因为循环序列,nums[:i]的最长子序列必定包含nums[i]，因此只需要比较nums[i+1]和nums[i]，如果nums[i+1]大于nums[i],则：
if:如果last_n形成的子序列不包含nums[i]，则nums[i]>nums[i-1]，依次前推，即nums[i-1]>nums[i-2]，直至到包含nums[idx]为止，
   因此，由nums[i]>nums[idx],则跟新last_p=last_n+1;
elif:如果last_n包含nums[i]，则last_p=last_n+1,且满足摇摆子序列的长度.

代码r如下.
'''
####解法1
class Solution:
    def wiggleMaxLength(self,nums):
        lens=len(nums)
        if(lens<=1):
            return(lens)
        flags=[0]*lens
        dp=[1]*lens
        for i in range(1,lens):
            for j in range(i):
                if(j==0):
                    if(nums[i]>nums[j]):
                        dp[i]=dp[j]+1
                        flags[i]='+'
                    elif(nums[i]<nums[j]):
                        dp[i]=dp[j]+1
                        flags[i]='-'
                    else:
                        dp[i]=dp[j]
                else:
                    if(nums[i]>nums[j] and flags[j]=='-'):
                        dp[i]=max(dp[i],dp[j]+1)
                        flags[i]='+'
                    elif(nums[i]<nums[j] and flags[j]=='+'):
                        dp[i]=max(dp[i],dp[j]+1)
                        flags[i]='-'
        return(dp[-1])



####解法2
class Solution:
    def wiggleMaxLength(self,nums):
        lens=len(nums)
        if(lens<=1):
            return(lens)
        last_p=[1]*lens
        last_n=[1]*lens
        for i in range(1,lens):
            for j in range(i):
                if(nums[i]>nums[j]):
                    last_p[i]=max(last_p[i],last_n[j]+1)
                elif(nums[i]<nums[j]):
                    last_n[i]=max(last_n[i],last_p[j]+1)
        return(max(last_p[-1],last_n[-1]))




####解法3
class Solution:
    def wiggleMaxLength(self,nums):
        lens=len(nums)
        if(lens<=1):
            return(lens)
        last_p=1
        last_n=1
        for i in range(1,lens):
            if(nums[i]>nums[i-1]):
                last_p=last_n+1
            elif(nums[i]<nums[i-1]):
                last_n=last_p+1
        return(max(last_p,last_n))
        







