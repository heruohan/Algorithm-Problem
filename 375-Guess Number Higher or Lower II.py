# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 22:22:31 2018

@author: hecongcong
"""
'''
The problem 375:Guess Number Higher or Lower
We are playing the guess game.The game is as follows:
I pick a number from 1 to n,you have to guess which number i picked.
Every time you guess wrong,i will tell you whether the number i picked is higher or lower.
However,when you guess a particular number x,and you guess wrong,you pay $x.you win the game when you guess the number i picked.

Example:
n=10,i picked is 8.
First round:you guess 5,i tell you that it is higher.you pay $5.
Second round:you guess 7,i tell you that it is higher.you pay $7.
Third round:you guess 9,i tell you that it is lower.you pay $9.
Game over.8 is the number i picked.
You end up paying $5+$7+$9=$21.
Given a particular n>=1,find out how much money you need to have to guarantee a win.
'''

'''
The anwer:本题是猜字游戏，给定一个数字n，找出能保证你赢的钱数.本题可以用全局极小和局部极大值的方法.
构造一个二维数组dp,其中dp[i][j]表示在[i,j]内能满足题意的钱数，i<=j.依次循环，当k属于[i,j]时，
local_max=k+max(dp[i][k-1],dp[i+1][j],循环完毕后，找出最小的local_max,并赋值dp[i][j]=local_max.
比如，当[1，1]时dp[1][1]=0,当[1，2]时，dp[1][2]=1;当[1,3]时，dp[1][3]=2;当[1,4]时，如下：
(1).当k=1时，左边位空，即dp[1][0]=0,右边为[2,4]，dp[2][4]=3，则local_max=1+3=4
(2).当k=2时，左边为[1,1]，即dp[1][1]=0,右边为[3,4]，dp[3][4]=3,则local_max=2+4=6
(3).当k=3时，左边为[1,2],dp[1][2]=1,右边为[4,4]，dp[4][4]=0,则local_max=3+1=4.
(4).当k=4时，左边为[1,3]，dp[1][3]=2，右边为[5][4]，dp[5][4]=0,则local_max=4+2=6.
因此，dp[1][4]取当中最小的local_max，即dp[1][4]=4.


#解法1：迭代的方法，先构造dp二维数组，然后迭代的求出dp[j][i]，即global_min,并赋值给dp[j][i]=global_min,其中j<i.
#解法2：递归的方法，此时为了减少重复计算，可以使用一个类似的dp二维数组，将global_min存入里面，当下次遇到相同的区间时，
直接从里面取，减少计算量.

代码如下.
'''


#解法1:迭代
class Solution:
    def getMoneyAmount(self,n):
        import math
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(i-1,0,-1):  ####必须依次求出i-1,i-2,...1到i的dp值,即dp[i-1][i],dp[i-2][i]....dp[1][i]
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
        















