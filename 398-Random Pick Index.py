# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 13:49:31 2019

@author: hecongcong
"""




#代码1
class Solution:
    def __init__(self,nums):
        self.num=nums
    
    def pick(self,target):
        import random
        lens=len(self.num)
        count=0
        flag=True
        for i in range(lens):
            if(flag):
                res=i
                flag=False
            else:
                count+=1
                j=random.randint(0,count)
                if(j==0):
                    res=i
        return(res)
        

#代码2
class Solution:
    def __init__(self,nums):
        self.num=nums
    def pick(self,target):
        import random
        count=-1
        lens=len(self.num)
        for i in range(lens):
            if(self.num[i]==target):
                count+=1
                j=random.randint(0,count)
                if(j==0):
                    res=i
        return(res)






