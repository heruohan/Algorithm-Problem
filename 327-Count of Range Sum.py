# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 13:42:15 2018

@author: hecongcong
"""
'''
Problem 327:Count of Range Sum
  Given an integer array nums, return the number of range sums
that lie in [lower, upper] inclusive.Range sum S(i, j) is 
defined as the sum of the elements in nums between
indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial.
You MUST do better than that.

Example:
Input: nums = [-2,5,-1], lower = -2, upper = 2
Output:3
Explanation:The three ranges are : [0,0], [2,2], [0,2] and 
their respective sums are: -2, -1, 2.

'''

'''
Answer:
方法1：O(n2).
用两次循环，但可借鉴动态规划的思想，可创建一个矩阵dp存计算结果，
减少计算量.

方法2:O(nlog(n)),因为nums中有负数，且是无序的，同时区间的统计不能
改变其中元素的位置，则可创建一个sums数组，sums[i]表示nums[i]到nums[0]
所有元素之和，则nums[i:j]元素之和为sums[j]-sums[i],为了后续对sums归并
排序的方便处理sums用了小技巧.同时，此题的代码实现中用了较多的技巧，需要注意.

思路如下：
第一步:生成sums数组.
第二步：对sums数组进行归并排序,同时统计符合的区间和个数.
在归并排序过程中，如生成排序好的左半部分sums[left:mid]和排序好的
右半部分sums[mid+1,right],因为是求区间和的个数，且左右sums数组的
相对位置没有改变，所以不影响结果.针对左数组中的任何一个元素sums[i],
设rl=rr=mid+1:
1.求首个sums[rl]-sums[i]大于等于的lower的位置rl.
2.求首个sums[rr]-sums[i]大于upper的位置rr.
则对于sums[i]元素及右半部分的元素来说，区间和满足条件的个数为rr-rl.
依次循环左数组中的元素.且因为左部分的元素是增大的，所以rl和rr不需要
回溯.


第三步：合并左右数组，使其有序.

代码实现技巧：
1.构造sums数组的时候，前面加0,比如nums=[-2,5,-1],可理解为
nums=[0,-2,5,-1],因为相对位置没有改变且是0,则不影响求个数的结果.
则sums=[0,-2,3,2],nums[0]到nums[2]的区间和,相当于sums[3]-sums[0].
2.sums数组在递归过程中是不断改变的，因为改变的是数组内的元素，则sums
数组相当于全局变量,其各个长度的左右数组不断的排序，合并.
3.count_merge(sums,left,right,lower,upper)函数返回的是sums数组中
left到right段上元素,符合条件的区间和的个数.返回结果后,此段元素已经进行了
归并且排序了.
'''


def countRangeSum(nums,lower,upper):
    if(len(nums)==0):
        return(0)
    sums=[0]
    for i in range(len(nums)):
        sums.append(sums[i]+nums[i])
    return(count_merge(sums,0,len(nums),lower,upper))


def count_merge(sums,left,right,lower,upper):
    if(left==right):
        return(0)
    mid=(left+right)//2
    '''
    ##1编号的代码表示sums数组上,左部分和右部分分别各自符合条件的区间和
    个数的和，且左右两部分对应sums数组上的元素已经分别排好序了.
    '''
    res=count_merge(sums,left,mid,lower,upper)+\
    count_merge(sums,mid+1,right,lower,upper) ##1
    rl,rr=mid+1,mid+1
    '''
    下面循环部分的代码表示针对右数组和左数组之间符合条件的区间和的
    个数.其最终循环完累加结果res表示左部分,右部分各自独立的符合条件
    区间和的个数，及左右两部分符合条件个数，三者之和，即sums数组上
    left到right元素全部符合条件区间和的个数.
    '''
    for i in range(left,mid+1):
        while(rl<=right and sums[rl]-sums[i]<lower):
            rl+=1
        while(rr<=right and sums[rr]-sums[i]<=upper):
            rr+=1
        res+=(rr-rl)
    '''
    以下代码表示在sums数组上相应位置上的合并排序.
    '''
    tmp=sums[left:right+1]
    m=0  ##m表示在tmp数组上左部分的开始位置.
    n=mid+1-left  ##n表示在tmp数组右部分的开始位置.
    for i in range(left,right+1):
        if(m<mid+1-left and n<right+1-left):
            if(tmp[m]<tmp[n]):
                sums[i]=tmp[m]
                m+=1
            else:
                sums[i]=tmp[n]
                n+=1
        elif(m<mid+1-left):
            sums[i]=tmp[m]
            m+=1
        elif(n<right+1-left):
            sums[i]=tmp[n]
            n+=1
    return(res)
    
            
        
        
            
        
            
            
            
                
    
    