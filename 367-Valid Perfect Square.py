# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:57:19 2018

@author: hecongcong
"""
'''
The problem 367:Valid Perfect Square
Given a positive integer num,write a function which returns True if num is a perfect square else False.

Note:Do not use any build-in library function such as sqrt.

Example1:
Input:16
Output:True
Example2:
Input:14
Output:False
'''

'''
The answer:本题的题意是给定一个正整数num，写一个函数确定num是否是一个完全平方数.且不准用内置库函数.
本题可以用两种思路进行解答，分别如下：
解法1：二分查找法
设置左右两个端点left和right，利用二分查找法进行查找；

解法2：等差数列法
1.等差数列的通项公式为：an=a1+(n-1)*d,其中d为公差，首项为a1，末项为an，n为项数；
2.求和公式为：sn=n*a1+(n*(n-1)*d)/2,其中sn为前n项和;
3.设d=2,a1=1,则化简可得sn=n**2;
4.则可得出结论，完全平方数是由首项为1,公差为2的等差数列加和而来，既num=1+3+5+....+(2*n-1).
'''

#解法1：二分查找法
def isPerfectSquare(num):
    left,right=1,num
    while(left<=right):
        mid=left+((right-left)>>2)  #加和减的运算优先级高于右移运算符
        '''
        mid=left+(right-left)//2  #除法的运算优先级高于加减运算符
        '''
        t=mid*mid
        print(t)
        if(t==num):
            return(True)
        elif(t<num):
            left=mid+1
        else:
            right=mid-1
    return(False)


#等差数列法
def isPerfectSquare1(num):
    tmp=1
    while(num>0):
        num-=tmp
        tmp+=2
    return(num==0)
    






















