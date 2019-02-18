# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:09:53 2019

@author: hecongcong
"""



#代码1
class Solution:
    def findNthDigit(self,n):
        start=1
        lens=1
        count=9
        while(n>count*lens):
            n-=count*lens
            start*=10
            lens+=1
            count*=10
        if(n % lens==0):
            tmp=start+n//lens-1
            str_tmp=str(tmp)
            return(int(str_tmp[lens-1]))
        else:
            tmp=start+n//lens
            str_tmp=str(tmp)
            return(int(str_tmp[n%lens-1]))
            
        
        








