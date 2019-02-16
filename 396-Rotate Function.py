# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:19:38 2019

@author: hecongcong
"""


'''
The problem 396:Rotate Function
Given an array of integers A and let n to be its length.
Assume Bk to be an array obtained by rotating the array A k positions clock-wise,we define a
'rotate function' F on A as follow:
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
Calculate the maximum value of F(0),F(1),F(2)......F(n-1).
Note:
n is guaranteed to be less than 10**5.

Example:
A = [4, 3, 2, 6]
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

so the maximum value of F(0),F(1),F(2),F(3) is F(3)=26.
'''


'''
The answer:本题是给定一个长度为n的整数数组A，Bk是A顺时针移动k个位置所得到的数组，然后在定义一个旋转函数F如题目所示，
求出F(0),F(1)...F(n-1)的最大值；
仔细观察，可以看出，F(0)和F(1),F(1)和F(2)有一定联系，可以推出一个一般性递推式表示F(i-1)和F(i)关系的状态转移方程;
'''

#解法1：迭代
class Solution:
    def maxRotateFunction(self,A):
        lens=len(A)
        sums=0
        tmp=0
        for i in range(lens):
            sums+=A[i]
            tmp+=i*A[i]
        res=tmp
        for j in range(1,lens):
            tmp+=(sums-lens*A[lens-j])
            res=max(res,tmp)
        return(res)
        


#解法2：递归
class Solution:
    def maxRotateFunction(self,A):
        self.lens=len(A)
        t=0
        sums=0
        for i in range(self.lens):
            sums+=A[i]
            t+=i*A[i]
        return(self.helpFn(A,t,t,sums,1))
        
    def helpFn(self,A,res,tmp,sums,i):
        if(i>=self.lens):
            return(res)
        tmp+=(sums-self.lens*A[self.lens-i])
        res=max(res,tmp)
        return(self.helpFn(A,res,tmp,sums,i+1))






