# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:27:38 2018

@author: hecongcong
"""

def reverseString(s):
    lst=list(s)
    left,right=0,len(lst)-1
    while(left<right):
        lst[left],lst[right]=lst[right],lst[left]
        left+=1
        right-=1
    return(''.join(lst))
    