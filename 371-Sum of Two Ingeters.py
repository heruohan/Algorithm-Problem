# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 13:41:13 2018

@author: hecongcong
"""
'''
The problem 371:Sum of Two Ingeters
Calculate the sum of two ingeters a and b,but you are not allowed to use the operator + and -.

Example1:
Input:a=1,b=2
Output:3
Eaxmple2:
Input:a=-2,b=3
Output:1
'''

'''
The answer:本题是给定两个整数a,b，计算其和，但是不能用+和-.
本题用位运算模拟加法的运算，因为两个数相加，可以分解为其对应二进制位上不考虑进位和只考虑进位两者结果之和，而其分别对应于位运算中的
异或(^)运算和与(&)运算及左移运算，比如：2+3=5，2^3=1、(2&3)<<1=4,因此1+4=5；但是由于python中整形不是固定的32位，当其左移操作的结果超过最大整数范围时，
会自动将int类型转化为long类型，因此需做特殊处理；
1.因为python3支持无限大的整形数字，所以需要模拟32位整数，首先定义MAX_INT=0x7FFFFFFF,既2**31-1；
2.定义TMP=0x100000000，既2**32，来模拟32为整数，对其取模相当于左移后可以去掉32位以上的；
3.最终当a是0<a<TMP,同时，当a位于32位之间时则返回a，如MAX_INT<a<TMP,则运用(~0<<31) | a将其转换；

代码如下.
'''
def getSum(a,b):
    MAX_INT=0x7FFFFFFF
    TMP=0x100000000
    while(b):
        tmp=a&b
        a=(a^b) % TMP
        b=(tmp<<1) % TMP
    return(a if(a <= MAX_INT) else (~0<<31) | a)
    


