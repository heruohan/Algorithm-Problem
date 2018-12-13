# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:57:19 2018

@author: hecongcong
"""

def isPerfectSquare(num):
    left,right=1,num
    while(left<=right):
        mid=left+((right-left)>>2)
        '''
        mid=left+(right-left)//2
        '''
        t=mid*mid
        print(t)
        if(t==num):
            return(True)
        elif(t<num):
            left=mid+1
        else:
            right=mid-1
    return(False)



def isPerfectSquare1(num):
    tmp=1
    while(num>0):
        num-=tmp
        tmp+=2
    return(num==0)
    






















