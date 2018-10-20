# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:42:17 2018

@author: hecongcong
"""

def countBits(num):
    res=[0,1,1,2]
    if(num<=3):
        return(res[:num+1])
    count=2
    for i in range(4,num+1):
        if(i==2*count):
            count=i
        res.append(1+res[i-count])
    return(res)




def contBits1(num):
    res=[0]
    for i in range(1,num+1):
        if(i%2==0):
            res.append(res[i>>1])
        else:
            res.append(res[i>>1]+1)
    return(res)
    
    
    
    
    
    
    
    
    
    
    
    
    