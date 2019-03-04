# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 00:38:56 2019

@author: hecongcong
"""



#解法1
class Solution:
    def thirdMax(self,nums):
        nums.sort(reverse=True)
        count=1
        lens=len(nums)
        for i in range(1,lens):
            if(nums[i]!=nums[i-1]):
                count+=1
            if(count==3):
                return(nums[i])
        return(nums[0])




#解法2：
class Solution:
    def thirdMax(self,nums):
        s=set(nums)
        lst=list(s)
        lst.sort(reverse=True)
        if(len(lst)<3):
            return(lst[0])
        return(lst[2])
        



#解法3：
class Solution:
    def thirdMax(self,nums):
        import bisect
        s=[]
        visited=set()
        for i in nums:
            if(i not in visited):
                bisect.insort_left(s,i)
                if(len(s)>3):
                    s.pop(0)
        return(s[0] if(len(s)==3) else s[-1])



#解法4：
class Solution:
    def thirdMax(self,nums):
        import math
        first=-math.inf
        second=-math.inf
        third=-math.inf
        for i in nums:
            if(i>first):
                third=second
                second=first
                first=i
            elif(i!=first and i>second):
                third=second
                second=i
            elif(i!=first and i!=second and i>third):
                third=i
        return(third if(third!=-math.inf) else first)
        
        
        
        
        
        
        
        
        
        
