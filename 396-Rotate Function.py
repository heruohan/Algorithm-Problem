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
推到如下：
不失一般性，可令A移动i位后为Bi=[a,b,c,...,x,y,z],则B(i+1)=[z,a,b,c,...x,y],因此可写出其F函数如下：
(1)  sums=a+b+c+...+x+y+z
(2)  F(i)=0*a+1*b+2*c+...+(n-3)*x+(n-2)*y+(n-1)*z
(3)  F(i+1)=0*z+1*a+2*b+3*c+...+(n-2)*x+(n-1)*y
用(1)+(2)可得：
F(i)+sums=1*a+2*b+3*c+...+(n-2)*x+(n-1)*y+n*z,两边同时减去n*z,得
F(i)+sums-n*z=0*z+1*a+2*b+3*c+...+(n-2)*x+(n-1)*y=F(i+1)
即：F(i+1)=F(i)+sums-n*z,其中z是原始A移动i位后到Bi的最后一位元素，设其在原始A中的索引为idx,则有：
idx+i=n-1,可得，idx=n-i-1,因此：F(i+1)=F(i)+sums-n*A[idx]=F(i)+sums-n*A[n-i-1];
令q=i+1,则F(q)=F(q-1)+sums-n*A[n-(q-1)-1]=F(q-1)+sums-n*A[n-q],

因此，可写出一般性的状态转移方程为：F(i)=F(i-1)+sums-n*A[n-i],其中n为A的长度.


解法1：迭代
1.循环A，求出sums和F(0);
2.循环A，根据状态转移方程，求出F(j)以及最大值res.

解法2：
1.构建辅助函数helpFn,当参数i大于等于A的长度时,就退出递归.
2.不断更新最大值res,函数值tmp,以及移动位数i；
代码如下.
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






