# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 23:22:26 2018

@author: hecongcong
"""

def increasingTriplet(nums):
    import math
    m1=m2=math.inf
    for i in nums:
        if(i<=m1):
            m1=i
        elif(i<=m2):
            m2=i
        else:
            return(True)
    return(False)
    