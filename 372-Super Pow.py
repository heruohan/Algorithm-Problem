# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:34:26 2018

@author: hecongcong
"""
'''
The problem 372:Super Pow
Your task is to calculate a**b mod 1337 where a is a positive integer and b is an extremely large positive integer given 
in the form of an array.

Example1:
Input:a=2,b=[3]
Output:8
Example2:
Input:a=2,b=[1,0]
Output:1024
'''

'''
The answer:本题题意是求一个数的幂，然后求模，既a**b mod 1337;同时由于b过大，所以用数组表示，本题用快速幂算法进行解法，且用到以下公式：
(a**b)%c=((a%c)**b)%c,(a*b)%c=((a%c)*(b%c))%c,既两个数相乘取模等于各因子分别取模相乘然后对结果在取模；这样可以减小a的大小；

同时，多个数相乘取模，可以分别对各因子多次取模，且可以取模后相结合在取模，既可以在任何位置，任何时候对中间结果进行取模，均不影响最终结果，同时
可以起到降低运算数字大小的效果，从而减少运算量；

代码如下.
'''
class Solution:
    ###计算a**b mod 1337
    def superPow(self,a,b):
        ret=1
        for i in b:
            ret=(self.pows(ret,10)*self.pows(a,i)) % 1337
        return(ret)
    
    ###运用快速幂算法计算m**n mod 1337
    def pows(self,m,n):
        res=1
        k=m % 1337
        while(n):
            if(n & 1==1):
                res=(res*k) % 1337
            k=(k*k) % 1337
            n>>=1
        return(res)
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
