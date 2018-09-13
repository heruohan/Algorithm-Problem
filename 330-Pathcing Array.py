# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 02:15:41 2018

@author: hecongcong
"""
'''
The Problem 330:Patchinig Array
Given a sorted positive integer array nums and an integer n,
add/patch elements to the array such that any number in range [1, n] inclusive
can be formed by the sum of some elements in the array.
Return the minimum number of patches required.

Example:
Input:nums = [1,5,10],n=20
Output:2
Explanation:The two patches can be[2,4].
'''
'''
The answer: 可以初始化res=1,其表示第一个不能被表示的数，比如res=5,表示能表示[0,5)，
既0,1,2,3,4,从5开始不能表示，然后不断更新res,直至满足res>n为止.
第一步：初始化res=1,计数器count=0.

第二步：当数组元素循环完，或者res<nums[i]时，加入元素res，更新res和count；否则
用nums[i]更新res,指针前移一位；直至res>n.
'''

class Solution:
    def minPatches(self,nums,n):
        res=1
        count=0
        lens=len(nums)
        i=0
        while(True):
            if(res>n):
                return(count)
            if(i>=lens or res<nums[i]):    ##i>=lens必须在res<nums[i]前，否则程序会报错.
                res+=res
                count+=1
            else:
                res+=nums[i]
                i+=1
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                    
