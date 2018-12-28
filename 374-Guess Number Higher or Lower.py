# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 15:56:58 2018

@author: hecongcong
"""


#The guess API is already defined for you.
#@param num,your guess
#@return -1 if my number is lower,1 if my number is higher,otherwise return 0
#def guess(num):



class Solution:
    def guessNumber(self,n):
        left=1
        right=n
        while(left<right):
            mid=(left+right)//2
            tmp=guess(mid)
            if(tmp==0):
                return(mid)
            elif(tmp==-1):
                right=mid-1
            else:
                left=mid+1
        return(left)
        
        
        
        
        
