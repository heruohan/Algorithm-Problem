# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 23:28:36 2018

@author: hecongcong
"""

class Solution:
    def canMeasureWater(self,x,y,z):
        def GreatestCommonDivisor(m,n):
            a=max(m,n)
            b=min(m,n)
            while(a%b):
                tmp=a%b
                a=b
                b=tmp
            return(b)
        if(x==0 or y==0):
            return(z in (x,y))
        gcd=GreatestCommonDivisor(x,y)
        return((x+y>=z) and (not z%gcd))
            






















