# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 22:54:08 2019

@author: hecongcong
"""


#解法1
def kthSmallest(matrix,k):
    res=[]
    m=len(matrix)
    for i in range(m):
        res+=matrix[i]
    sort_res=sorted(res)
    return(sort_res[k-1])



##解法2
def kthSmallest1(matrix,k):
    import bisect
    res=[]
    m=len(matrix)
    for i in range(m):
        for j in range(m):
            bisect.insort_left(res,matrix[i][j])
            if(len(res)>k):
                res.pop()
    return(res[-1])


##解法3
def kthSmallest2(matrix,k):
    import bisect
    m=len(matrix)
    left=matrix[0][0]
    right=matrix[-1][-1]
    while(left<right):
        mid=(left+right)//2
        count=0
        for i in range(m):
            count+=bisect.bisect_right(matrix[i],mid)
        if(count<k):
            left=mid+1
        else:
            right=mid
    return(left)



##解法4
class Solution:
    
        


















