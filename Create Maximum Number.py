# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:58:25 2018

@author: hecongcong
"""


'''
leetcode题目：
321.Create Maximum Number.
Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Example:
Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
'''

'''
解题思路：
第一步：
(1)choose操作，既从一个数组中能抽取的K个最大数.
(2)例如：nums=[3,4,6,5],k=2;则结果为[6,5].

第二步：
(1)merge操作：对第一步选出的两个最大子数组进行合并.
(2)例如：num1=[6,5],num2=[9,8,3];则合并结果为[9,8,6,5,3].
(3)其中需要创建比较函数greater.greater函数比较两个数组分别在i,j位置的大小.

第三步：
(1)主函数maxNumber,从num1中选i个数，num2中选K-i个数，通过choose操作分别选出
i和k-i个最大子数组；
(2)然后通过merge操作将两个最大子数组合并为长度为k的最大数组.
(3)将k进行所有可能的分割，求出最大的数组.

'''

####第一步：
def choose(num,k):
    s=[]
    lens=len(num)
    for i in range(lens):
        while(s and (lens-i+len(s))>k and num[i]>s[-1]):
            s.pop()
        if(len(s)<k):
            s.append(num[i])
    return(s)


def greater(nums1,i,nums2,j):
    while(i<len(nums1) and j<len(nums2) and nums1[i]==nums2[j]):
        i+=1
        j+=1
    return(j==len(nums2) or (i<len(nums1) and nums1[i]>nums2[j]))

#####第二步：
def merge(num1,num2,k):
    res=[]
    i=0
    j=0
    count=0
    while(count<k):
        if(greater(num1,i,num2,j)):
            res.append(num1[i])
            i+=1
            count+=1
        else:
            res.append(num2[j])
            j+=1
            count+=1
    return(res)
    

#第三步：主函数.
def maxNumber(nums1,nums2,k):
    max_Num=[0]*k
    for i in range(k+1):
        if(i<=len(nums1) and k-i<=len(nums2)):
            tmp1=choose(nums1,i)
            tmp2=choose(nums2,k-i)
            Num=merge(tmp1,tmp2,k)
            if(greater(Num,0,max_Num,0)):
                max_Num=Num
    return(max_Num)
                
            
    
    
    
    
    
    
    
    
    
