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
    res=count_merge(sums,left,mid,lower,upper)+count_merge(sums,mid+1,right,lower,upper)
    rl,rr=mid+1,mid+1
    for i in range(left,mid+1):
        while(rl<=right and sums[rl]-sums[i]<lower):
            rl+=1
        while(rr<=right and sums[rr]-sums[i]<=upper):
            rr+=1
        res+=(rr-rl)
    tmp=sums[left:right+1]
    m=0
    n=mid+1-left
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
    
            
        
        
            
        
            
            
            
                
    
    