# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:23:02 2019

@author: hecongcong
"""


'''
The problem 397:Integer Replacement
Given a positive integer n and you can do operations as follow:
1.if n is even,replace n with n/2.
2.if n is odd,you can repalce n with either n-1 or n+1.
what is the minimum number of replacements needed for n to become 1?

Example1:
Input:8
return:3
Explanation:8 -> 4 -> 2 -> 1.

Example2:
Input:7
return:4
Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
'''


'''
The answer:本题是给定一个正整数n,当n为偶数时,用n/2代替它，当n为奇数时，用n-1或者n+1代替，求当n变到1时,所需要的最小替换步数.
本题有多种解法，分别如下：

解法1：动态规划
核心思想：
1.构建一个dp数组，dp[i]表示i到达1的最小步数，则dp[1]=0
2.状态转移方程，当i为偶数时，dp[i]=dp[i//2]+1;当i为奇数时，dp[i]=min(dp[i+1],dp[i-1])+1
代码如下；
解法2与解法1同思路，也是动态规划思想；


解法3：迭代
1.当n为偶数时，直接将n除以2就可以了，步数res加1；
2.当n为奇数时，需要判断什么时候加1，什么时候减1，通过观察，除过3,7以外，其他奇数如果加1，是4的倍数的话，则此奇数加1，求出的步数更小；
对与7，加1和减1所得的结果一样，可不用考虑；
更进一步，怎么判断一个奇数加1后是4的倍数呢，可以用位运算进行判断，因为如果n位奇数的话，其二进制的最后一位是1，如果倒数第二位也是1的话，
加1后，则其二进制位的后两位就都会变成0，即n+1=...x*(2**4)+y*(2**3)+z*(2**2),因此必定能被4整数;
代码如下；


解法4：递归
代码如下；


'''
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


    



