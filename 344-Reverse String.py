# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:27:38 2018

@author: hecongcong
"""
'''
The question 344:Reverse String
Write a function that takes a string as input and returns the string reversed.

Example1:
Input:'hello'
Output:'olleh'

Exaple2:
Input:'A man, a plan, a canal: Panama'
Output:'amanaP :lanac a ,nalp a ,nam A'
'''

'''
The answer:本题是给定一个字符串，写一个函数翻转字符串并输出.
本题采用双指针的解法，并且在相应位置互换字符,直至循环结束.代码如下.

代码技巧：因为在字符串中不可以直接互换两个元素，所以先将其转换为列表，
各个位置互换后，再把字符串列表转换为字符串.
'''
def reverseString(s):
    lst=list(s)
    left,right=0,len(lst)-1
    while(left<right):
        lst[left],lst[right]=lst[right],lst[left] #相应位置互换元素
        left+=1  #左边加指针
        right-=1  #右边减指针
    return(''.join(lst)) #将字符串列表转换为字符串
  
    
    
    
    
