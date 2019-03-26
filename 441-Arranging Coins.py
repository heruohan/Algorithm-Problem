# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:56:10 2019

@author: hecongcong
"""



#解法1
class Solution:
    def arrangeCoins(self,n):
        i=1
        count=0
        while(n-count>=i):
            count+=i
            i+=1
        return(i-1)
        




#解法2：
class Solution:
    def arrangeCoins(self,n):
        if(n<=1):
            return(n)
        left=1
        right=n
        while(left<right):
            mid=(left+right)//2
            if(mid*(mid+1)//2<=n):
                left=mid+1
            else:
                right=mid
        return(left-1)


#解法3：
class Solution:
    def arrangeCoins(self,n):
        return(int(((8*n+1)**0.5-1)//2))





