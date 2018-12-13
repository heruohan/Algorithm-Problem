# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 23:28:36 2018

@author: hecongcong
"""
'''
The problem 365:Water and Jug Problem
You are given two jugs with capacities x and y liters.there is an infinite amount of water supply available.
you need to determine whether it is possible to measure exactly z liters using these two jugs.

If z liters of water is measurable,you must have z liters of water contained within one or both buckets by the end.

Operations allowed:
1.Fill any of the jugs completely with water.
2.Empty any of the jugs.
3.Pour water from one jug into another till the other jug is completely full or the jug itself is empty.

Example1:
Input:x=3,y=5,z=4
Output:True
Example2:
Input:x=2,y=6,z=5
Output:False
'''

'''
The answer:本题是给两个x和y升的罐子，问是否可以精确的度量出z升水，既是否满足z=m*x+n*y,其中x+y>=z，m与n是倒水和舀水的次数；
根据裴蜀定理，若对于任何整数x,y以及其最大公约数(x,y)=d,则对任意的整数m,n满足m*x+n*y必定是d的倍数，特别的存在整数，使得
m*x+n*y=d;所以只要z是d的倍数，且x+y>=z，则满足题意要求，为True.

#解法1
用辗转相除法和循环算出两个数的最大公约数.代码如下.

#解法2
用辗转相除法和递归算法两个数的最大公约数.代码如下.
'''
#解法1 迭代
class Solution:
    def canMeasureWater(self,x,y,z):
        def GreatestCommonDivisor(m,n):
            a=max(m,n)
            b=min(m,n)
            while(a%b):
                tmp=a%b
                a=b
                b=tmp
            return(b)
        if(x==0 or y==0):
            return(z in (x,y))
        gcd=GreatestCommonDivisor(x,y)
        return((x+y>=z) and (not z%gcd))


#解法2 递归
class Solution:
    def canMeasureWater(self,x,y,z):
        def Gcd(m,n):
            if(m%n==0):    #初始条件
                return(n)
            return(Gcd(n,m%n))
        if(x==0 or y==0):
            return(z in (x,y))
        gcd=Gcd(x,y)
        return((x+y>=z) and (not z%gcd))






















