# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:59:21 2019

@author: hecongcong
"""


#解法1
class Solution:
    def lastRemaining(self,n):
        return(self.helpFn(n,True))
        
    def helpFn(self,n,flag):
        if(n==1):
            return(1)
        if(flag):
            return(2*self.helpFn(n//2,False))
        else:
            return(2*self.helpFn(n//2,True)-1+(n % 2))
            


#解法2
class Solution:
    def lastRemaining(self,n):
        low,high=1,n
        gap=1
        flag=True
        while(low<high):
            nums=(high-low)//gap+1
            if(flag):
                low+=gap
                if(nums % 2==1):
                    high-=gap
            else:
                high-=gap
                if(nums % 2==1):
                    low+=gap
            gap*=2
            flag=not flag
        return(low)


#解法3
class Solution:
    def lastRemaining(self,n):
        low=1
        gap=1
        while(2*gap<=n):
            low+=gap
            gap*=2
            if(gap*2>n):
                break
            if((n//gap) % 2==1):
                low+=gap
            gap*=2
        return(low)
        









