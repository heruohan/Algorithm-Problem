# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 00:32:43 2019

@author: hecongcong
"""



#解法1
class Solution:
    def fizzBuzz(self,n):
        res=[]
        for i in range(1,n+1):
            if(i % 15==0):
                res.append('FizzBuzz')
            elif(i % 3==0):
                res.append('Fizz')
            elif(i % 5==0):
                res.append('Buzz')
            else:
                res.append(str(i))
        return(res)
        





