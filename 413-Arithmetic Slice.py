# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:38:38 2019

@author: hecongcong
"""



#解法1
class Solution:
    def numberOfArithmeticSlice(self,A):
        start=0
        lens=len(A)
        res=0
        while(lens-start>=3):
            tmp=start+1
            diff=A[tmp]-A[start]
            end=tmp+1
            while(end<lens and A[end]-A[tmp]==diff):
                end+=1
                tmp+=1
            dist=end-start
            count=2
            while(dist-count>=1):
                res+=(dist-count)
                count+=1
            start=end-1
        return(res)



#解法2
class Solution:
    def numberOfArithmeticSlice(self,A):
        start=0
        lens=len(A)
        res=0
        while(lens-start>=3):
            tmp=start+1
            diff=A[tmp]-A[start]
            end=tmp+1
            while(end<lens and A[end]-A[tmp]==diff):
                end+=1
                tmp+=1
            dist=end-start
            res+=(0.5*(dist-1)*(dist-2))
            start=end-1
        return(int(res))
        


#解法3：
class Solution:
    def numberOfArithmeticSlice(self,A):
        lens=len(A)
        res=0
        count=2
        for i in range(2,lens):
            if(A[i]-A[i-1]==A[i-1]-A[i-2]):
                count+=1
            else:
                if(count>2):
                    res+=0.5*(count-1)*(count-2)
                    count=2
        return(int(res) if(count==2) else int(res+0.5*(count-1)*(count-2)))
     
    
    

#解法4：
class Solution:
    def numberOfArithmeticSlice(self,A):
        lens=len(A)
        res=0
        dp=[0]*lens
        for i in range(2,lens):
            if(A[i]-A[i-1]==A[i-1]-A[i-2]):
                dp[i]=dp[i-1]+1
            res+=dp[i]
        return(res)
        
    


#解法5：
class Solution:
    def numberOfArithmeticSlice(self,A):
        lens=len(A)
        res=0
        tmp=0
        for i in range(2,lens):
            if(A[i]-A[i-1]==A[i-1]-A[i-2]):
                tmp+=1
                res+=tmp
            else:
                tmp=0
        return(res)
        











