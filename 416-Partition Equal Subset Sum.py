# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:10:49 2019

@author: hecongcong
"""



#解法1
class Solution:
    def canPartition(self,nums):
        import bisect
        sums=sum(nums)
        if(sums % 2==1):
            return(False)
        mid=sums//2
        if(mid in nums):
            return(True)
        res=[False]
        nums.sort()
        idx=bisect.bisect_left(nums,mid)
        if(sum(nums[:idx])<mid):
            return(False)
        self.dfs(nums,len(nums)-1,0,mid,res)
        return(res[0])
    
    def dfs(self,nums,start,val,target,flag):
        if(flag[0]):
            return
        if(val==target):
            flag[0]=True
            return
        for i in range(start,-1,-1):
            if(val+nums[i]>target):
                continue
            self.dfs(nums,i-1,val+nums[i],target,flag)
            




#解法2
class Solution:
    def canPartition(self,nums):
        s=set([0])
        sums=sum(nums)
        target,val=divmod(sums,2)
        if(val):
            return(False)
        for num in nums:
            new_s=set()
            for i in s:
                new_s.add(i+num)
            s |=new_s
            if(target in s):
                return(True)
        return(False)
        


        
#解法3
class Solution:
    def canPartition(self,nums):
        sums=sum(nums)
        target,val=divmod(sums,2)
        if(val):
            return(False)
        dp=[False]*(target+1)
        dp[0]=True
        for num in nums:
            if(dp[target]):
                return(True)
            for j in range(target,num-1,-1):
                dp[j]=dp[j] or dp[j-num]
        return(False)
        









