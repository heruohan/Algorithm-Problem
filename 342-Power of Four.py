# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:29:37 2018

@author: hecongcong
"""

def isPowerOfFour(num):
    return(num>0 and (not num-1 & num) and (num-1)%3==0)
    