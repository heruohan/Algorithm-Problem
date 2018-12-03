# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:21:38 2018

@author: hecongcong
"""


####解法1
def countNumbersWithUniqueDigits(n):
    if(n==0):
        return(1)
    sums=10
    for i in range(2,n+1):
        end=11-i
        prob=9
        while(end<=9):
            prob*=end
            end+=1
        sums+=prob
    return(sums)



####解法2
def countNumbersWithUniqueDigits(n):
    if(n==0):
        return(1)
    sums=10
    prob=9
    for i in range(2,n+1):
        prob*=11-i
        sums+=prob
    return(sums)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    