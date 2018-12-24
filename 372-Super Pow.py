# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:34:26 2018

@author: hecongcong
"""

class Solution:
    def superPow(self,a,b):
        ret=1
        for i in b:
            ret=(self.pows(ret,10)*self.pows(a,i)) % 1337
        return(ret)
        
    def pows(self,m,n):
        res=1
        k=m % 1337
        while(n):
            if(n & 1==1):
                res=(res*k) % 1337
            k=(k*k) % 1337
            n>>=1
        return(res)
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            