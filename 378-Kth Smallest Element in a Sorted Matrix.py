# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 22:54:08 2019

@author: hecongcong
"""

'''
The problem 378:Kth Smallest Element in a sorted matrix
   Given a n*n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order,not the kth distinct element.

Example:
matrix=[
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k=8
return 13.

Note:
You may assume k is always valid,1<=k<=n**2.
'''


'''
The answer:本题是给定一个行、列都按升序排列的矩阵和正整数k，在这个矩阵中找出第k小的元素.
本题有四种解法，分别如下：
解法1：
构建一个列表res,然后循环分别把matrix的每行都放入到res里面，然后对res按升序排序，找出第k个元素
即为所求.

解法2：
维护一个长度为k的res数组，将矩阵中的每个元素运用二分查找算法按升序插入进去，将矩阵
中的元素遍历完毕后，res数组中最后一个元素几位所求.

解法3：
运用变异的二分查找算法，因为矩阵matrix中的最小元素为matrix[0][0],最大元素为matrix[-1][-1],
所以我们在这个范围内用二分查找算法进行查找:
第一步：设置left=matrix[0][0],right=matrix[-1][-1],算出mid.
第二步：遍历matrix的每行，然后再运用二分查找算法找出小于等于mid的元素个数count.
第三步：如果count<k,则所求元素必定大于mid,既令left=mid+1,否则必定小于等于mid,既令right=mid.
第四步：循环，直到left==right为止，返回即可.


解法4：
在解法3中我们查找matrix中小于等于mid的所有元素个数时，是运用二分算法遍历了矩阵的所有行，没有
只用到矩阵中每行是增序的这个条件，没有用到每列也是按增序排列的这个条件.在此解法中我们运用到这个
条件，如下：
第一步：重写一个search_less函数进行个数的查找，从矩阵的最后一行的第一个元素开始循环.
第二步：如果此元素小于等于mid,则其和其以上的这列元素均小于mid，将其个数加入res中，并且列向前移动一位.
如果此元素大于mid，则需要将行向上移动一位，继续查找.
第三步：循环完毕后，res即为矩阵中小于等于mid的所有元素个数.其余操作和解法3一样.

代码如下.
'''

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



##解法4:python3
class Solution:
    def kthSmallest(self,matrix,k):
        left=matrix[0][0]
        right=matrix[-1][-1]
        while(left<right):
            mid=(left+right)//2
            count=self.search_less(matrix,mid)
            if(count<k):
                left=mid+1
            else:
                right=mid
        return(left)
    
    def search_less(self,matrix,target):
        m=len(matrix)
        i,j=m-1,0
        res=0
        while(i>=0 and j<m):
            if(matrix[i][j]<=target):
                res+=i+1
                j+=1
            else:
                i-=1
        return(res)
    
        


















