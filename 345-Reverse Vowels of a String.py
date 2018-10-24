# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 23:02:49 2018

@author: hecongcong
"""

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







    