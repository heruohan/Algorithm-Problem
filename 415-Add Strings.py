# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:54:59 2019

@author: hecongcong
"""



#解法1：
class Solution:
    def addStrings(self,num1,num2):
        res=''
        count=0
        lens1=len(num1)
        lens2=len(num2)
        t1=lens1-1
        t2=lens2-1
        while(t1>=0 or t2>=0):
            if(t1>=0):
                i1=ord(num1[t1])-48
            else:
                i1=0
            if(t2>=0):
                i2=ord(num2[t2])-48
            else:
                i2=0
            sums=i1+i2+count
            res=str(sums % 10)+res
            count=sums//10
            t1-=1
            t2-=1
        return('1'+res if(count) else res)



#代码2：
class Solution:
    def addStrings(self,num1,num2):
        res=''
        lens1=len(num1)
        lens2=len(num2)
        if(lens1>lens2):
            num2='0'*(lens1-lens2)+num2
        elif(lens1<lens2):
            num1='0'*(lens2-lens1)+num1
        t=max(lens1,lens2)-1
        count=0
        while(t>=0):
            i1=ord(num1[t])-48
            i2=ord(num2[t])-48
            sums=i1+i2+count
            res=str(sums % 10)+res
            count=sums//10
            t-=1
        return('1'+res if(count) else res)
        







