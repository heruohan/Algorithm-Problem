# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 23:02:49 2018

@author: hecongcong
"""
'''
The question 345:Reverse Vowels of a String
    Write a function that takes a string as input and reverse only the vowels of a string.

Example1:
Input:'hello'
Output:'holle'

Example2:
Input:'leetcode'
Output:'leotcede'
'''

'''
The answer:本题的题意是给定一个字符串，只反转其中的元音字母,其他则保持不变.
英文26个字母有a,e,i,o,u5个元音字母，包括大写的话共有10个，可以将其都放入vowels集合中，
然后从字符串列表lst前后两端left和right,采用双指针解法处理.共有以下几种情况：
第一种：当lst[left]和lst[right]都在vowels中时，则进行交换，并left后移一位，right前移一位.
第二种：当lst[left]和lst[right]只有一个在vowels中时，则只移动不在vowels中的指针.
第三种：当lst[left]和lst[right]都不在vowels中时，两者都要移动.
代码如下.
'''
def reverseVowels(s):
    vowels={'a','e','i','o','u','A','E','I','O','U'}
    lst=list(s)
    left,right=0,len(lst)-1
    while(left<right):
        if(lst[left] in vowels and lst[right] not in vowels):
            right-=1
        elif(lst[left] not in vowels and lst[right] in vowels):
            left+=1
        elif(lst[left] in vowels and lst[right] in vowels):
            lst[left],lst[right]=lst[right],lst[left]
            left+=1
            right-=1
        else:
            left+=1
            right-=1
    return(''.join(lst))







    
