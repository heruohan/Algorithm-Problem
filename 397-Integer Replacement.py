# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:23:02 2019

@author: hecongcong
"""



#解法1
class Solution:
    def integerReplacement(self,n):
        dp=[0]*(n+2)
        for i in range(2,n+1):
            if(i % 2==0):
                if(dp[i]==0):
                    dp[i]=dp[i//2]+1
            else:
                dp[i+1]=dp[(i+1)//2]+1
                dp[i]=min(dp[i-1],dp[i+1])+1
        return(dp[-2])
        


#解法2
class Solution:
    def integerReplacement(self,n):
        if(n==1):
            return(0)
        if(n % 2==1):
            tmp=n+1
        else:
            tmp=n
        dp=[0]*(n+2)
        dp[2]=1
        for i in range(4,tmp+1,2):
            if((i//2) % 2==0):
                dp[i]=dp[i//2]+1
            else:
                dp[i]=min(dp[i//2-1],dp[i//2+1])+2
        return(min(dp[-1],dp[-3])+1 if(n % 2==1) else dp[-2])
        

#解法3
class Solution:
    def integerReplacement(self,n):
        tmp=n
        res=0
        while(tmp>1):
            res+=1
            if(tmp & 1):
                if((tmp & 2) and tmp!=3):
                    tmp+=1
                else:
                    tmp-=1
            else:
                tmp>>=1
        return(res)
        
        
#解法4
class Solution:
    def integerReplacement(self,n):
        if(n==1):
            return(0)
        if(n % 2==0):
            return(self.integerReplacement(n//2)+1)
        else:
            return(min(self.integerReplacement(n+1),\
                       self.integerReplacement(n-1))+1)


    



