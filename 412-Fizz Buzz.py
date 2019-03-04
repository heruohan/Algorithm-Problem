# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 00:32:43 2019

@author: hecongcong
"""


'''
The problem 412:Fizz Buzz
write a program that outputs the string representation of numbers from 1 to n.
but for multiples of three it should output 'Fizz' instead of the number and for the multiples of five output 'Buzz'.
For numbers which are multiples of both three and five output 'FizzBuzz'.

Example:
n=15,
return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


'''
The answer:本题是给定一个整数n,返回1到n的字符串列表，如果是3的倍数则用'Fizz'替代，如果是5的倍数则用'Buzz'替代，如果即是3的倍数，
又是5的倍数，则用'FizzBuzz'替代；

解法1：
1.从1循环到n，如果元素i是15的倍数，则表示其即是3的倍数又是5的倍数，则用'FizzBuzz'将其替代.
2.如果i是3的倍数，因为其的判断语句在15的之下，会自动排除是5的倍数，则将'Fizz'加入到结果中.
3.如果i是5的倍数，同上.
'''
#解法1
class Solution:
    def fizzBuzz(self,n):
        res=[]
        for i in range(1,n+1):
            if(i % 15==0):      #既是5的倍数又是3的倍数
                res.append('FizzBuzz')
            elif(i % 3==0):     #自动排除是5的倍数，只是3的倍数
                res.append('Fizz')
            elif(i % 5==0):     #自动排除是3的倍数，只是5的倍数
                res.append('Buzz')
            else:
                res.append(str(i))
        return(res)
        





