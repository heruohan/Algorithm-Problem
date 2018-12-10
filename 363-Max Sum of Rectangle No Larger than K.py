# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 22:10:38 2018

@author: hecongcong
"""

'''
The problem 363:Max Sum of Rectangle No larger Than K.
Given a non-empty 2D matrix matrix and an integer k,find the max sum of a rectangle in the matrix such that its sum is
no larger than k.

Example:
Input:matrix=[[1,0,1],[0,-2,3]],k=2
Output:2
Explanation:Because the sum of rectangle [[0,1],[-2,3]] is 2,and 2 is the max number no larger than k(k=2).

Note:
1.The rectangle inside the matrix must have an area>0;
2.what if the number of rows is much larger than the number of columns?
'''

'''
The answer:本题的题意是给定一个二维矩阵matrix和一个正整数k，找到一个子矩阵使得其和最大且不大于k.本题特别难,可拆分为几个小题.
首先，想到的是暴力解法，把所有的子矩阵找出来，然后进行比较，但是会TLE，我们在此基础上进行优化，有以下两种解法.
解法1：
1.构造一个二维sums数组，其中sums[i][j]表示从矩阵matrix[0][0]到matrix[i][j]构成的子矩阵所有元素的和；
2.然后进行循环，以[0,0]到[i,j]为子矩阵A，然后遍历子矩阵A的所有子矩阵，求出其和，找出满足条件的最大值；
3.此种方法时间复杂度为O(m*m*n*n),也会TLE,通不过测试;

解法2：
1.此种方法将矩阵以列或者行进行划分，然后构建一个一维数组sums，求其累计和；
2.然后再对一维数组sums用累积和的方法查找其任意子数组的和；
2.用bisect.bisect_left对sums进行二分查找，找出排序后的数组lst，第一个大于等于cursum-k的值得索引，
设找出的值为Q，则Q>=cursum-k,则cursum-Q<=k,同时cursum-Q是sums子数组的和，既其满足条件且是最接近K值的；
3.然后将累计和cursum，按顺序插入数组lst中；
4.此种方法的时间复杂度为O(n*n*mlog(m)).
'''

##解法1
def maxSumSubmatrix(matrix,k):
    import math
    m=len(matrix)
    n=len(matrix[0])
    res=-math.inf
    sums=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            tmp=matrix[i][j]
            if(i>0):
                tmp+=sums[i-1][j]
            if(j>0):
                tmp+=sums[i][j-1]
            if(i>0 and j>0):
                tmp-=sums[i-1][j-1]
            sums[i][j]=tmp
            for a in range(i+1):
                for b in range(j+1):
                    tmp=sums[i][j]
                    if(a>0):
                        tmp-=sums[a-1][j]
                    if(b>0):
                        tmp-=sums[i][b-1]
                    if(a>0 and b>0):
                        tmp+=sums[a-1][b-1]
                    if(tmp<=k):
                        res=max(res,tmp)
    return(res)



##解法2
def maxSumSubmatrix(matrix,k):
    import math
    import bisect
    m=len(matrix)
    n=len(matrix[0]) if(m) else 0
    M=max(m,n)
    N=min(m,n)
    res=-math.inf
    for i in range(N):  #对较小的进行循环，较大的进行二分查找；
        sums=[0]*M
        for j in range(i,N): #求多维数组的累计和
            lst=[]
            cursum=0
            for a in range(M):
                sums[a]+=matrix[a][j] if(m>n) else matrix[j][a]
                cursum+=sums[a]  ##一维数组的累计和方法
                if(cursum<=k):
                    res=max(res,cursum)
                idx=bisect.bisect_left(lst,cursum-k)
                if(idx!=len(lst)):
                    res=max(res,cursum-lst[idx])
                bisect.insort(lst,cursum)
    return(res)
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
