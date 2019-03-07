# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:10:49 2019

@author: hecongcong
"""


'''
The problem 416:Partition Equal Subset Sum
Given a non-empty array containing only positive integers,find if the array can be partitioned into two subsets such
that the sum of elements in both subsets is equal.
Note:
1.each of the array element will not exceed 100.
2.the array size will not exceed 200.

Example1:
input:[1, 5, 11, 5]
output:True
Explanation:the array can be partitioned as [1,5,5] and [11].
Example2:
input:[1, 2, 3, 5]
output:False
Explanation:the array can not be partitioned into equal sum subsets.
'''


'''
The answer:本题是给定一个非空的正整数数组nums，问是否能将此数组分割成和相等的两个数组；
思路：nums的和能分为两个非空的数组，则说明其和为偶数，如果为奇数的话则肯定返回False，如果为偶数的话，我们的解题目标就
变为能否在nums中找出元素使得其和为sums//2.同时，可以将大于sums//2的元素不用考虑；

解法1：深度优先搜索+剪枝
思路：本题可以用深度优先搜索的解法，直接在数组中搜索元素的和能否等于mid.比如，不考虑大于mid的元素，在搜索过程中如果累加和
大于mid的话，因为都是正整数，所以也进行剪枝，以及当找到等于mid的组合时，将搜索全部剪枝，即停止搜索；
代码如下.
代码说明：
1.dfs的参数start,使得在搜索过程中，每个元素只能使用一次；
2.dfs的参数flag,其是一个列表，使用列表是因为其在递归搜索过程中使得列表里面的元素带有记忆性，可以传递；
同时列表里面的元素为开关变量，如果为True，则代表已经找到元素组合为target的集合；


解法2：集合枚举法
思路：利用集合将所有可能组合结果枚举出来，进行查表；

解法3：动态规划
１．因为不用考虑负数和大于target的元素，所以构建一个长度为target+1的dp数组，其中dp[i]表示能否以nums中的元素组成和为i；
2.对于nums中的元素num,如果dp[j-num]既j-num能用数组中的元素组成的话，则j必定能用数组中的元素组成，其中num<=j<=target.因为，此时
要保证j-num>=0且不用考虑大于target的元素；因此状态转移方程为:dp[j]=dp[j] or dp[j-num];因为当dp[j]为True的时候，其后续始终为True；
3.在二重循环中j必须从target向num进行，证明如下：
  (1).在二重循环里，dp[j]=dp[j] or dp[j-num],当j从[num,target]时，假设j之前循环过的元素为i，则有:i<j,而j-num也必定小于j，因此dp[i]与
  dp[j-num]可能重复，既j-num==i,如果dp[i]在上一轮外层循环中为False,在当前外层循环中才被更新为True，则说明i被组成的元素中必定包含当前
  元素num,而此时如果j-num==i,则dp[j-num]为True,同时，j-num被组成的元素中也必定包含num，因此j的被组成的元素中num被重复用了两次，不符合题意；
  
  (2).在二重循环里，当j从[target,num]时，假设j之前循环过的元素未x，则有x>j,而j-num必定是小于j的，所以必有x!=j-num;因此在当前num的外层循环中，
  必定排除了num被重复使用的情况；
'''
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
    
    def dfs(self,nums,start,val,target,flag): #flag是一个列表，因此在搜索过程中具有记忆性，里面是开关，一旦搜索到即变为True.
        if(flag[0]):  #剪枝，一旦找到则不在进行搜索
            return
        if(val==target):
            flag[0]=True
            return
        for i in range(start,-1,-1):
            if(val+nums[i]>target):   #剪枝，因为元素都是正整数的，所以一旦大于target,则在这条枝上不在进行搜索
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
            if(dp[target]):  #剪枝，一旦找到则即可结束循环，返回结果
                return(True)
            for j in range(target,num-1,-1):  #此循环必须从高向低循环,此时可以排除重复使用num元素的情况，证明见上述描述
                dp[j]=dp[j] or dp[j-num]
        return(dp[target])
        









