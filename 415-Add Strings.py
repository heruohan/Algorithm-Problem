# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:54:59 2019

@author: hecongcong
"""


'''
The problem 415:Add Strings
Given two non-negative integers num1 and num2 repsresented as string,return the sum of num2 and num1.
Note:
1.the length of both num1 and num2 is less than 5100.
2.both num1 and num2 contains only digits 0-9.
3.both num1 and num2 does not contain any leading zero.
4.you must not use any built_in BigInteger Library or convert the inputs to integer directly.
'''


'''
The answer:本题是给定两个字符串数字num1,num2.返回这两个数字相加的和，并以字符串表示；不能用内建库和函数，也不能直接将字符串转化为
数字进行运算；
思路：
将两个字符串的每个对应位相加，并用变量count表示进位，同时，短的字符串高位以0表示就可以；
代码如下；

'''
#解法1： 
class Solution:
    def addStrings(self,num1,num2):
        res=''
        count=0
        lens1=len(num1)
        lens2=len(num2)
        t1=lens1-1
        t2=lens2-1
        while(t1>=0 or t2>=0):
            if(t1>=0):
                i1=ord(num1[t1])-48  #用ord()将数字字符串转化为相应的ASCII码，并且因为'0'的ASCII码为48，所以减去即可转换
            else:
                i1=0   #对于短字符串的高位以0表示
            if(t2>=0):
                i2=ord(num2[t2])-48
            else:
                i2=0
            sums=i1+i2+count  #count表示前一位是否进位
            res=str(sums % 10)+res
            count=sums//10   #求当前位的进位值
            t1-=1
            t2-=1
        return('1'+res if(count) else res)



#代码2：将短的字符串高位以0填充，使得两者长度相等
class Solution:
    def addStrings(self,num1,num2):
        res=''
        lens1=len(num1)
        lens2=len(num2)
        '''
        将短的字符串填充0
        '''
        if(lens1>lens2):
            num2='0'*(lens1-lens2)+num2
        elif(lens1<lens2):
            num1='0'*(lens2-lens1)+num1
        t=max(lens1,lens2)-1
        count=0
        while(t>=0):
            i1=ord(num1[t])-48
            i2=ord(num2[t])-48
            sums=i1+i2+count
            res=str(sums % 10)+res
            count=sums//10
            t-=1
        return('1'+res if(count) else res)
        







