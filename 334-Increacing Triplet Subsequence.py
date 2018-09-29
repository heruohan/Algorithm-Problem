# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 23:22:26 2018

@author: hecongcong
"""
'''
The problem 334:Increasing Triple Subsequence
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Note:Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example:
Input:[1,2,3,4,5]
Output:True

Example2:
Input:[5,4,3,2,1]
Output:False
'''

'''
The answer:本题是按数组顺序是否能找出三个递增的元素，并且要求了时间和空间复杂度,因此暂不考虑暴力解法.
解题思路：
第一步：初始化两个变量m1,m2分别为无穷大.
第二步：遍历数组元素i，当i<=m1时,则m1=i;当m1<i<=m2时，m2=i;否则当i>m2时返回True.

The Prove:
当i>m2时，如果m1被更新到m2之后，则m2之前必存在小于m2的数m，满足m<m2<i;
如果m1在m2之前，则必有m1<m2<i;
同时，数组之后的数如满足更新条件则不断更新，可以以更大的概率满足题意.

'''
def increasingTriplet(nums):
    import math
    m1=m2=math.inf
    for i in nums:
        if(i<=m1):
            m1=i
        elif(i<=m2):
            m2=i
        else:
            return(True)
    return(False)
    
