# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 13:49:31 2019

@author: hecongcong
"""

'''
The problem 398:Random Pick Index
Given an array of integers with possible duplicates,randomly output the index of a given target number.you
can assume that the given target number must exist in the array.
Note:
the array size can be very large,Solution that uses too much extra space will not pass the judge.

Example:
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);
//pick(3) should return either index 2,3 or 4 randomly.each index should have equal probability of returning.
Solution.pick(3).
//pick(1) should return 0,since in the array only nums[0] is equal to 1.
Solution.pick(1).
'''

'''
the answer:本题是给定一个可能重复的整数数组，随机的返回所给目标值得索引，假定所给目标值必定存在于数组中；
本题说了数组的长度很大，不能使用额外的空间求解，因此想到蓄水池抽样算法.

核心思想：
1.构建一个计数器count,循环数组，当元素等于target时，将计数器加1，并且随机返回一个[0,count]的整数j；
2.如果j等于0的话，则令res=i;循环结束返回即可；
代码如下.
'''
#代码1
class Solution:
    def __init__(self,nums):
        self.num=nums
    
    def pick(self,target):
        import random
        lens=len(self.num)
        count=0
        flag=True
        for i in range(lens):
            if(flag):
                res=i
                flag=False
            else:
                count+=1
                j=random.randint(0,count)
                if(j==0):
                    res=i
        return(res)
        

#代码2
class Solution:
    def __init__(self,nums):
        self.num=nums
    def pick(self,target):
        import random
        count=-1
        lens=len(self.num)
        for i in range(lens):
            if(self.num[i]==target):
                count+=1
                j=random.randint(0,count)
                if(j==0):
                    res=i
        return(res)






