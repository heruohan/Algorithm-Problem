# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:58:25 2018

@author: hecongcong
"""


'''
leetcode题目：
321.Create Maximum Number.
'''
'''
解题思路：
'''

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
    

#
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
                
            
    
    
    
    
    
    
    
    
    
