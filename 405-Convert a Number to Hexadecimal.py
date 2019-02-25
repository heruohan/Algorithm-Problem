# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:18:30 2019

@author: hecongcong
"""


'''
The problem 405:Convert a number to hexadecimal
Given an integer,write an algorithm to convert it to hexadecimal.For negative integer,two's complement method is used.
Note:
1.all letters in hexadecimal(a-f) must be in lowercase.
2.the hexadecimal string must not contain extra leading 0's.if the number is zero,it is represented by a single zero 
character '0'.otherwise,the first character in the hexadecimal string will not be the zero character.
3.the given number is gauranteed to fit within the range of a 32-bit singed integer.
4.you must not use any method provided by the libary which converts/formats the number to hex directly.

Example1:
input:26
output:'1a'
Example2:
input:-1
output:"ffffffff"
'''


'''
The answer:本题是给定一个整数num，写一个算法将其转换为十六进制的，并且以字符串输出；

解法1：
1.首先我们将num不管为负数还是正数，统统转化为与其补码值相同的无符号的正整形数；
2.然后构建一个10到15的字典m，然后不断地对16取模取余循环，因为对16取余，相当于余数就是16的0次方，1次方....
直接把余数加入到结果res里就可以了.
3.然后返回res.
代码如下；


解法2：
思路：解法2不需要转化num,因为数字在计算机中都是用补码进行存储和计算，所以直接可以用与运算和右移运算转化，
但是题目中要求是32位；同时在python中整数无位数限制，因为超过计算机本身的数值范围后，会自动转化为长整形数，
所以需要有一个计数器count来限制；

1.构建一个计数器count.然后进行循环，每次用与运算取出num的后四位；
2.如果大于等于10,则直接用chr函数将其转化为对应的字符；
3.将num向右移动4位，count加1；
4.返回结果；
代码如下；
'''
#解法1
class Solution:
    def toHex(self,num):
        if(num<0):
            num=num & 4294967295
        res=''
        m={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        while(num>0):
            num,y=divmod(num,16)
            if(10<=y<=15):
                res=m[y]+res
            else:
                res=str(y)+res
        return(res if(res) else '0')



#解法2
class Solution:
    def toHex(self,num):
        res=''
        count=0
        while(num!=0 and count<8):
            t=num & 0xf
            if(t>=10):
                res=chr(97+t-10)+res  #用chr()函数把ASCII码转化为对应的字符，97对应的字符为'a'
            else:
                res=str(t)+res
            num>>=4
            count+=1
        return(res if(res) else '0')









