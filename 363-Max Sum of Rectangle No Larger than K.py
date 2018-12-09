# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 22:10:38 2018

@author: hecongcong
"""

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
    for i in range(N):
        sums=[0]*M
        for j in range(i,N):
            lst=[]
            cursum=0
            for a in range(M):
                sums[a]+=matrix[a][j] if(m>n) else matrix[j][a]
                cursum+=sums[a]
                if(cursum<=k):
                    res=max(res,cursum)
                idx=bisect.bisect_left(lst,cursum-k)
                if(idx!=len(lst)):
                    res=max(res,cursum-lst[idx])
                bisect.insort(lst,cursum)
    return(res)
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            