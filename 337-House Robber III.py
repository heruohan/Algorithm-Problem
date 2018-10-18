# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:48:18 2018

@author: hecongcong
"""

#Definition for a binary tree node.
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None


####解法1
class Solution:
    def rob(self,root):
        ret=self.dfs(root)
        return(max(ret[0],ret[1]))
        
    def dfs(self,roots):
        res=[0,0]
        if(not roots):
            return(res)
        left=self.dfs(roots.left)
        right=self.dfs(roots.right)
        res[0]=max(left[0],left[1])+max(right[0],right[1])
        res[1]=left[0]+right[0]+roots.val
        return(res)
        
        

####解法2
class Solution:
    def rob(self,root):
        mps={}
        return(self.dfs(root,mps))
    
    def dfs(self,roots,mps):
        if(not roots):
            return(0)
        if(roots in mps):
            return(mps[roots])
        max_amount=0
        if(roots.left):
            max_amount+=self.dfs(roots.left.left,mps)+\
                        self.dfs(roots.left.right,mps)
        if(roots.right):
            max_amount+=self.dfs(roots.right.left,mps)+\
                        self.dfs(roots.right.right,mps)
        max_amount=max(max_amount+roots.val,self.dfs(roots.left,mps)+\
                       self.dfs(roots.right,mps))
        mps[roots]=max_amount
        return(max_amount)
        
    
        
        
        






        