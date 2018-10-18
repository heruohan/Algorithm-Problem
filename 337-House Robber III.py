# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:48:18 2018

@author: hecongcong
"""
'''
The answer 337:House Robber III
    The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this 
place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same
night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example:
Input:[3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1
Output:9
Explanation:Maximum amount of money the thief can rob is 4+5=9.
'''

'''
The answer:本题的题意是小偷来到一个所有house可以组成一个二叉树的地方，只能从根节点进入这个地方，并且如果两个直接相连的房间被同时闯入，则会报警，
问小偷能在不报警的情况下偷的的最大金额.
本题可以采用动规划的思想，并结合递归完成,有两种解法，核心思想相似：一个节点能取到的最大金额数为包含当前节点值的最大值与不包含当前节点值最大值中的
较大值.
解法1：
本解法构建一个二元素数组res,其意义如下：
res[0]:表示不包含当前节点值时，在其以下子树范围内所能抢到的最大金额数.
res[1]:表示包含当前节点值时，在其以下子树范围内所能抢到的最大金额数.
设当前节点为roots,其左右节点分别为roots.left和roots.right,对应的所返回的数组为left和right,则根据题意条件，其状态转移方程如下：
res[0]=max(left[0],left[1])+max(right[0],right[1]),因为如不包含roots，则其最大值可为其左右节点最大值之和.
res[1]=left[0]+right[0]+roots.val,因为如包含roots，则不能包含其左右子节点的值，否则会报警.
代码如下.

解法2：
本解法运用递归，直接返回其所能抢到的最大金额数，但是在递归过程中，有较多的重复计算，直接递归效率较低，因此可运用一个字典mps,将当前节点树下与其
所能抢到的最大金额，一一映射保存在字典中,如下次用到则可直接从字典中提取，不必在重复计算,提高计算效率.
代码如下.
'''



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
        res[0]=max(left[0],left[1])+max(right[0],right[1])  #状态转移方程1
        res[1]=left[0]+right[0]+roots.val  #状态转移方程2
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
                       self.dfs(roots.right,mps))  #第一个元素表示包含当前节点值所抢到的最大金额，第二个元素表示不包含当前节点值所抢到的最大金额
        mps[roots]=max_amount
        return(max_amount)
        
    
        
        
        






        
