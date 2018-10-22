# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 01:29:57 2018

@author: hecongcong
"""

def integerBreak(n):
    if(n==2 or n==3):
        return(n-1)
    elif(n % 3==0):
        return(3**(n//3))
    elif(n % 3==1):
        return(2*2*3**((n-4)//3))
    elif(n % 3==2):
        return(2*3**((n-2)//3))
        