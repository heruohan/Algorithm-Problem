# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:09:53 2019

@author: hecongcong
"""

'''
The problem 400:Nth digit
Find the nth digit of the infinite integer sequence:1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
Note:
n is positive and will fit within the range of a 32-bit signed integer(n<2**31).

Example1:
input:3
output:3

Example2:
input:11
output:0
Explanation:the 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...is a 0,which is part of the
number 10.
'''


'''
The answer:本题是给定一个正整数，从一个无限的序列中找到第n个数字；
核心思路：
1到9中有9个一位数，10到99中有90个两位数，100到999中有900个三位数，以此类推；因此，可以构建变量lens表示在几位数区间，start表示
在某个区间的开始位置，count表示此区间有多少数字；通过这几个变量可以确定第n个位置，是区间中的哪个数字；
确定以后，在用字符串的方式将其选出，然后直接转化为数字；
代码如下；
'''

#代码1
class Solution:
    def findNthDigit(self,n):
        start=1
        lens=1
        count=9
        while(n>count*lens):
            n-=count*lens
            start*=10
            lens+=1
            count*=10
        if(n % lens==0):
            tmp=start+n//lens-1
            str_tmp=str(tmp)
            return(int(str_tmp[lens-1]))
        else:
            tmp=start+n//lens
            str_tmp=str(tmp)
            return(int(str_tmp[n%lens-1]))
            
        
        








