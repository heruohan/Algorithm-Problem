# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 23:00:03 2018

@author: hecongcong
"""

'''
The problem 373:Find K Pairs With Smallest Sums
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u,v) which consists of one element from the first array and one element from the second array.
Find the k Pairs (u1,v1),(u2,v2)....(uk,vk) with the smallest sums.

Example1:
Input:nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation:The first 3 pairs are returned from the sequence:[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6].
Example2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output:[1,1],[1,1]
Explanation:The first 2 pairs are returned from the sequence:[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3].
Example3:
Input:nums1 = [1,2], nums2 = [3], k = 3
Output:[1,3],[2,3]
Explanation:All possible pairs are returned from the sequence:[1,3],[2,3].
'''


'''
The answer:本题是给定两个排好序的数组和一个正整数k，在定义一对(u,v),其中一个元素是从第一个数组选出，另一个元素是从第二个数组选出，
然后找出k对这样的二元组，使得其和最小；本题我想出了两种解法，分别如下：

解法1：
1.分别对两个数组的长度和k的最小值进行循环，并将其组合放进ret列表中；
2.然后自定义以和排序的排序器，我们这里用lambda 函数，对ret进行排序，得到sort_ret；
3.从sort_ret中选出k和lens1*lens2中的较少个.

解法2：
解法2的核心：是定义一个长度为lens1,且初始化为0的idx数组，idx[i]的含义是：nums1中的元素nums1[i]在nums2中对应的元素索引可与nums1[i]组成对
放入ret结果.例如，nums1=[1,5,9],nums2=[20,30,50],当循环到nums1中的第一个元素1时，idx[0]指向nums2中的20,即idx[0]=0，当[nums1[0],nums2[0]]
被选出放到ret中后，idx[0]则等于1；可以这样做是因为两个数组都是排序了的，所以只需要判断没有取出过的，最前面的一个元素，因为后的元素的和肯定比前面
元素的和大，比如当nums1[1]=5时，如果nums2中没有任何元素取出过，那么idx[1]则等于0；如果nums2中的第一个元素20被取出过，那么idx[1]则等于1，因为
nums2后面的数肯定越来越大，不用考虑；
'''
####解法1
class Solution:
    def KSmallestPairs(self,nums1,nums2,k):
        ret=[]
        lens1=len(nums1)
        lens2=len(nums2)
        for i in range(min(k,lens1)):
            for j in range(min(k,lens2)):
                ret.append([nums1[i],nums2[j]])
        sort_ret=sorted(ret,key=lambda x:x[0]+x[1])
        return(sort_ret[:min(k,lens1*lens2)])


####解法2
class Solution:
    def KSmallestPairs(self,nums1,nums2,k):
        import math
        lens1=len(nums1)
        lens2=len(nums2)
        ret=[]
        size=min(k,lens1*lens2)
        idx=[0]*lens1
        for i in range(size):
            cur=0
            sums=math.inf
            for j in range(lens1):
                if(idx[j]<lens2 and sums>nums1[j]+nums2[idx[j]]):
                    cur=j
                    sums=nums1[j]+nums2[idx[j]]
            ret.append([nums1[cur],nums2[idx[cur]]])
            idx[cur]+=1
        return(ret)
        
    
    
    
    
    
    
    
    
    
 
