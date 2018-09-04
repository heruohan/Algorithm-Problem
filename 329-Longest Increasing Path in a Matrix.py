# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 22:11:41 2018

@author: hecongcong
"""

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
            
            
            
            
            
            
            
            
            
            
            