# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:18:30 2019

@author: hecongcong
"""



#解法1
class Solution:
    def toHex(self,num):
        if(num<0):
            num=num & 4294967295
        res=''
        m={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        while(num>0):
            num,y=divmod(num,16)
            if(10<=y<=15):
                res=m[y]+res
            else:
                res=str(y)+res
        return(res if(res) else '0')



#解法2
class Solution:
    def toHex(self,num):
        res=''
        count=0
        while(num!=0 and count<8):
            t=num & 0xf
            if(t>=10):
                res=chr(97+t-10)+res
            else:
                res=str(t)+res
            num>>=4
            count+=1
        return(res if(res) else '0')









