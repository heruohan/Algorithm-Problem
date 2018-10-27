# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:10:29 2018

@author: hecongcong
"""
'''
The question 350:Intersection of Two Arrays II
    Given two arrays, write a function to compute their intersection.

Example1:
Input:nums1 = [1,2,2,1], nums2 = [2,2]
Output:[2,2]

Example2:
Input:nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output:[4,9]

Note:
1.Each element in the result should appear as many times as it shows in both arrays.
2.The result can be in any order.
'''

'''
The answer:本题是给定两个数组，找出其交集部分，但是要找出存在于两个数组中全部的元素.
解题思路：
给两个数组分别以升序进行排序,产生有序数组order_nums1和order_nums2,然后设置两个指针idx1和idx2，分别表示排序后两个数组的开头位置.
然后在两个数组内循环，其有三种情况，分别如下：
1.当order_nums1[idx1]==order_nums2[idx2]时,将元素放入结果中,然后指针分别向前移动一位.
2.当order_nums1[idx1]<order_nums2[idx2]时，将元素值有的指针向前移动一位，即idx1=idx1+1;
3.idx2同理.
代码如下.
'''


class Solution:
    def intersect(self,nums1,nums2):
        order_nums1=sorted(nums1)
        order_nums2=sorted(nums2)
        idx1=idx2=0
        res=[]
        while(idx1<len(nums1) and idx2<len(nums2)):
            if(order_nums1[idx1]==order_nums2[idx2]):
                res.append(order_nums1[idx1])
                idx1+=1
                idx2+=1
            elif(order_nums1[idx1]<order_nums2[idx2]):
                idx1+=1
            else:
                idx2+=1
        return(res)
        
        
        
        
        
        
        
        
        
        
