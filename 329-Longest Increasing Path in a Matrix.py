# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 22:11:41 2018

@author: hecongcong
"""
'''
The Problem:329. Longest Increasing Path in a Matrix
Given an integer matrix, find the length of the longest increasing path.
From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example:
Input:nums=[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output:4
Explanation: The longest increasing path is [1, 2, 6, 9].
'''
'''
方法1：直接运用递归进行代码构建，但是重复计算过多，会产生TLE,算法效率太低，需要进行优化.
''''

class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if(len(matrix)==0):
            return(0)
        self.lens=1
        matrix.insert(0,[matrix[0][0]]+matrix[0]+[matrix[0][-1]])
        matrix.append([matrix[-1][0]]+matrix[-1]+[matrix[-1][-1]])
        for i in range(1,len(matrix)-1):
            matrix[i].insert(0,matrix[i][0])
            matrix[i].append(matrix[i][-1])
        for i in range(1,len(matrix)-1):
            for j in range(1,len(matrix[0])-1):
                self.dfs(i,j,matrix,1)
        return(self.lens)
    def dfs(self,x,y,matrix,lens):
        if(matrix[x+1][y]<=matrix[x][y] and matrix[x-1][y]<=matrix[x][y]\
           and matrix[x][y+1]<=matrix[x][y] and matrix[x][y-1]<=matrix[x][y]):
            self.lens=max(self.lens,lens)

        if(matrix[x][y-1]>matrix[x][y]):
            self.dfs(x,y-1,matrix,lens+1)
        if(matrix[x][y+1]>matrix[x][y]):
            self.dfs(x,y+1,matrix,lens+1)
        if(matrix[x-1][y]>matrix[x][y]):
            self.dfs(x-1,y,matrix,lens+1)
        if(matrix[x+1][y]>matrix[x][y]):
            self.dfs(x+1,y,matrix,lens+1)
'''
方法2：运用动态规划的思想，维护一个二维数组dp，dp[i][j]表示以matrix[i][j]为起点的最长路径的长度，
这样做可以避免重复运算，提高算法运行效率.
'''
class Solution:
    def longestIncreasingPath(self,matrix):
        res=1
        m1=len(matrix)
        if(m1==0):
            return(0)
        n1=len(matrix[0])
        dp=[[0]*n1 for _ in range(m1)]
        for i in range(m1):
            for j in range(n1):
                res=max(res,self.dfs(matrix,dp,i,j))
        return(res)
    def dfs(self,matrix,dp,x,y):
        if(dp[x][y]):
            return(dp[x][y])
        lst=[(0,-1),(0,1),(1,0),(-1,0)]
        m_lens=1
        for i in lst:
            m=x+i[0]
            n=y+i[1]
            if(m<0 or m>=len(matrix) or n<0 or n>=len(matrix[0]) \
               or matrix[m][n]<=matrix[x][y]):
                continue
            m_lens=max(m_lens,1+self.dfs(matrix,dp,m,n))
        dp[x][y]=m_lens
        return(m_lens)
        
               
            
            
            
            
            
            
            
            
            
