# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 13:07:47 2019

@author: hecongcong
"""



'''
Definition for a QuadTree node.
class Node:
    def __init__(self,val,isLeaf,topLeft,topRight,bottomLeft,bottomRight):
        self.val=val
        self.isLeaf=isLeaf
        self.topLeft=topLeft
        self.topRight=topRight
        self.bottomLeft=bottomLeft
        self.bottomRight=bottomRight
'''



#解法1：
class Solution:
    def construct(self,grid):
        return(self.helps(grid,0,0,len(grid)))
    
    def helps(self,grid,x,y,dist):
        if(dist<=0):
            return
        for i in range(x,x+dist):
            for j in range(y,y+dist):
                if(grid[x][y]!=grid[i][j]):
                    return(Node(True,False,\
                                self.helps(grid,x,y,dist//2),\
                                self.helps(grid,x,y+dist//2,dist//2),\
                                self.helps(grid,x+dist//2,y,dist//2),\
                                self.helps(grid,x+dist//2,y+dist//2,dist//2)))
        return(Node(grid[x][y]==1,True,None,None,None,None))
        



