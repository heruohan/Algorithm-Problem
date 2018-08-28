# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:33:15 2018

@author: hecongcong
"""
'''
324:Wiggle Sort II.
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
Example1:
Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example2:
Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
'''

'''
Answer:时间复杂度为O(n).
解题思路：
第一步：对nums进行排序.
第二步：在原数组的奇数位(既1,3,5....)依次存放排序后数组的后半部分，直至放满，
偶数位(既0，2，4.....)依次存放排序后数组的剩下部分，直至放满.
第三步：放满后，原数组既符合题目中nums[0] < nums[1] > nums[2] < nums[3]....的要求.
'''
def wiggleSort(nums):
    lens=len(nums)
    nums1=sorted(nums)      ##排序
    for i in range(1,lens,2):   ##奇数位填充
        nums[i]=nums1.pop()
    for i in range(0,lens,2):   ##偶数位填充
        nums[i]=nums1.pop()
    return(nums)
