# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 22:22:31 2018

@author: hecongcong
"""

#解法1:迭代
class Solution:
    def getMoneyAmount(self,n):
        import math
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(i-1,0,-1):
                global_min=math.inf
                for k in range(j,i):
                    local_max=k+max(dp[j][k-1],dp[k+1][i])
                    global_min=min(global_min,local_max)
                dp[j][i]=global_min
        return(dp[1][n])




##解法2：递归
class Solution:
    def getMoneyAmount(self,n):
        dp=[[0]*(n+1) for _ in range(n+1)]
        return(self.fn(1,n,dp))
        
    def fn(self,x,y,hlst):
        import math
        if(x>=y):
            return(0)
        if(hlst[x][y]>0):
            return(hlst[x][y])
        global_min=math.inf
        for i in range(x,y+1):
            local_max=i+max(self.fn(x,i-1,hlst),self.fn(i+1,y,hlst))
            global_min=min(global_min,local_max)
        hlst[x][y]=global_min
        print(hlst)
        return(global_min)
        















