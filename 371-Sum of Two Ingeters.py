# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 13:41:13 2018

@author: hecongcong
"""

def getSum(a,b):
    while(b):
        tmp=a&b
        a=(a^b) % 0x100000000
        b=(tmp<<1) % 0x100000000
    return(a if a <= 0x7FFFFFFF else a | (~0x100000000+1))
    


