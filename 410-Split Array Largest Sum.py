# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:08:11 2019

@author: hecongcong
"""


'''
The problem 410:Split Array Largest sum
Given an array which consists of non-negative integers and an integer m.you can split the array into m non-empty
continuous subarrays.write an algorithm to minimize the largest sum among these m subarrays.
Note:
if n is the length of array,assume the following constraints are satisfied:
1.1 ≤ n ≤ 1000
2.1 ≤ m ≤ min(50, n)
Examples:
input:nums= [7,2,5,10,8],m=2
output:18
Exlanation:there are four ways to split nums into two subarrays.
the best way is to split it into [7,2,5] and [10,8],where the largest sum
among the two subarrays is only 18.
'''



'''
The answer:本题是给定一个数组nums,和一个整数m，把nums分成连续的m个非空子数组，求出所有分法中m个子数组中和的最大值中的最小值；
本题比较难，有以下两种解法，如下：

解法1：动态规划
思路：首先构建一个二维数组dp,初始化为最大值，dp[i][j]表示nums的前j个元素，被分成i份，满足题目条件的最优解,其中i的取值可为1<=i<=j;
其中dp[i][j]可以分解为求Q=max(dp[i-1][k],sums[j]-sums[k]),i-1<=k<j,sums[j]表示前j个元素的累积和，dp[i][j]是所有Q值得最小值；
令T=sums[j]-sums[k],则前k个元素分为i-1份假设有count种分法，其中A，B，C...为前k个元素每种分割方法中和的最大值：
1、A,*,*,*...,*,T;
2、*,B,*,*..*，T；
3、*，*，*，C，*，T；
证明Q表示:在T时刻count种分法中的最优解，且它是dp[i-1][k]和T中的较大值，任意设C=dp[i-1][k],如下：
1.如果T<C,因此A>B>C>T,所以各个分组中的最大值为A,B,C,且因为C最小，则Q=C，因为count中分法中的最优解Q是dp[i-1][k]与T中的较大值；
2.如果T>C，则任意取第2种分法：
    a.如B>T,则第二种分法的最大值为B，第三种分法最大值为T，因为B>T,所以Q=T；
    b.如B<T,则第二种分法的最大值为T，第三种分法的最大值为T，因此，Q=T；
    因此，count种分法中的最优解Q是dp[i-1][k]与T中的较大值；
综上所述，在任意情况下，T时刻，即count种分法中的最优解Q是dp[i-1][k]和T中的较大值，证明完毕;
然后对于不同T的情况，因为Q是count种分法的中的最优解的局部最小值，因此，全局最优解dp[i][j]，是Q中的最小值；

解题步骤：
1.构建累积和数组sums.二维dp数组，dp[i][j]表示nums的前j个元素，被分成i份，满足题目条件的全局最优解，初始化为最大值；令dp[0][0]=0;
2.进入循环，然后更新dp数组，最后返回结果；
代码如下；



解法2：二分查找法
思路：一个数组nums被分成m分，当被分成1份时，其最优解为nums所有元素的和sums；当分成len(nums)份时，其最优解为nums中的最大值max，因此，被分成m份所对应
的最优解肯定位于sums和max之间；因此可以采用二分查找法；现在的难点就是每次的中位数mid对应的份数count怎么与m联系上，进行比较；
     同时，我们发现，份数m与其对应的最优解Y的函数是Y=fn(m)是减函数；
     我们需要构造一个辅助函数can_split()来表示一个最优解和其可分的份数的映射关系，以此来比较中位数mid对应的分数count与m的大小关系，由此根据减函数的
     性质再推出mid与m所对应的最优值的大小情况，从而进行二分查找；
     因此辅助函数can_split(lst,m,mid)可以这样构造，首先其是一个减函数，其次，参数mid在这里的含义是划分lst后的最优值，所以其将lst划分过程中，其是份数
     中的最大值，因此各个份的和是小于等于mid的；所以在构造过程中循环lst,如果累计和cursum>mid时，则将份数统计值count加1，并重新计算cursum.一旦count
     大于m时，就返回False，表示mid所对应的分数count是大于m的，由于是减函数所以m对应的最优值是大于mid的；如果循环完毕后，则返回True，表示mid所对应的
     份数是小于等于m,由于是减函数所以m对应的最优值是小于等于mid；从而可以进行二分查找；
'''


#解法1：动态规划
class Solution:
    def splitArray(self,nums,m):
        import math
        lens=len(nums)
        sums=[0]*(lens+1)
        dp=[[math.inf]*(lens+1) for _ in range(m+1)]
        dp[0][0]=0
        for i in range(1,lens+1):
            sums[i]=sums[i-1]+nums[i-1]   #求累积和数组
        for i in range(1,m+1):
            for j in range(i,lens+1):  #使得数组长度大于等于被分份数
                for k in range(i-1,j):
                    val=max(dp[i-1][k],sums[j]-sums[k])   #更新dp[i][j]的局部最优解val
                    dp[i][j]=min(dp[i][j],val)    #更新dp[i][j]，即全局最优解
        return(dp[m][lens])




#解法2：二分查找法
class Solution:
    def splitArray(self,nums,m):
        left,right=0,0
        for i in range(len(nums)):
            left=max(left,nums[i])
            right+=nums[i]
        while(left<right):
            mid=(left+right)//2
            if(self.can_split(nums,m,mid)):    #表示m对应的最优值是小于等于mid的
                right=mid
            else:
                left=mid+1   #表示m对于的最优值是大于mid的
        return(left)
    
    def can_split(self,lst,m,mid):  #mid其实是表示划分后的最优值
        cursum=0  #累计和
        count=1
        for i in range(len(lst)):
            cursum+=lst[i]
            if(cutrsum>mid):  #保证累计和小于等于mid，使得mid是其最优值
                cursum=lst[i]
                count+=1
                if(count>m):
                    return(False)
        return(True)
        






