# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 00:42:20 2019

@author: hecongcong
"""


#解法1
class Solution:
    def validUtf8(self,data):
        i=0
        lens=len(data)
        while(i<lens):
            if(data[i]>255):
                return(False)
            count=0
            if((data[i] & 0b10000000)==0):
                count=0
            elif((data[i] & 0b11100000)==0b11000000):
                count=1
            elif((data[i] & 0b11110000)==0b11100000):
                count=2
            elif((data[i] & 0b11111000)==0b11110000):
                count=3
            else:
                return(False)
            for j in range(i+1,i+count+1):
                if(j>=lens or (data[j] & 0b11000000)!=0b10000000):
                    return(False)
            i+=count+1
        return(True)
        















