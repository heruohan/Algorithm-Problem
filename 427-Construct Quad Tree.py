# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 13:07:47 2019

@author: hecongcong
"""

'''
The problem 427:Construct Quad Tree
we want to use quad trees to store an NxN boolean gird.Each cell in the grid can only be
True or Fasle.the root node represents the whole grid.For each node,it will be subdivided
into four children nodes until the values in the region it represents are all the same.
each node has another two boolean attributes:isLeaf and val.isLeaf is true if and only if the
node is a leaf node.the val attribute for a leaf node contains the value of the region it
represents.
your task is to use a quad tree to represent a given grid.For the non-leaf nodes,val can be
arbitray,so it is reprepsented as *.
Note:
1.N is less than 1000 and guaranteened to be a power of 2.
2.if you want to know more about the quad tree,you can refer to its wiki. 
'''




'''
The answer:本题是给定一个NxN的布尔值网格，每个格子只能是1或者0，叫用一个四元象限树来表示这个网格；比如给定一个8x8的网格grid，如果其里面的元素全部
是1或者0，则grid是一个LeafNode，返回即可;否则，就将grid等分成4快，对每一块重复上述过程；因为需要等分成四块，所以我们可以用一个起始坐标(x,y)和其边长
dist来表示当前的正方形；

解法1：
1.首先构建一个辅助函数helps(grid,x,y,dist),其中x,y是当前起始点的坐标，dist为其边长，这样就可以表示任意一个分块，然后循环当前块中所有的点，一旦有
不相等的点，就表示此块为非叶子节点，并将其划分为四块，然后调用递归函数，返回此节点；如果所有元素都循环完，则表示此块为一个叶子节点，直接返回即可；
2.在主函数construct里面调用并返回辅助函数helps.
代码如下；
'''

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
        



