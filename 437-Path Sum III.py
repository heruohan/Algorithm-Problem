# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:07:13 2019

@author: hecongcong
"""



'''
Definition for a binary tree node.
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
'''

#解法1：
class Solution:
    def pathSum(self,root,sum):
        if(not root):
            return(0)
        return(self.helps(root,0,sum)+\
               self.pathSum(root.left,sum)+\
               self.pathSum(root.right,sum))
    
    def helps(self,node,value,target):
        res=[0]
        self.dfs(node,value,target,res)
        return(res[0])
    
    def dfs(self,node,value,target,res):
        if(not node):
            return
        if(node.val+value==target):
            res[0]+=1
        self.dfs(node.left,value+node.val,target,res)
        self.dfs(node.right,value+node.val,target,res)
        


############解法1代码1：
class Solution:
    def pathSum(self,root,sum):
        if(not root):
            return(0)
        return(self.helps(root,0,sum)+\
               self.pathSum(root.left,sum)+\
               self.pathSum(root.right,sum))
    
    def helps(self,node,cursum,target):
        if(not node):
            return(0)
        cursum+=node.val
        return((cursum==target)+\
               self.helps(node.left,cursum,target)+\
               self.helps(node.right,cursum,target))
    
#解法2：
class Solution:
    def pathSum(self,root,sum):
        if(not root):
            return(0)
        res=[0]
        self.helps(root,0,sum,res,False)
        return(res[0])
    
    def helps(self,node,value,target,res,start):
        if(not node):
            return
        if(node.val+value==target):
            res[0]+=1
        if(start):
            self.helps(node.left,value+node.val,target,res,start)
            self.helps(node.right,value+node.val,target,res,start)
        else:
            self.helps(node.left,value+node.val,target,res,not start)
            self.helps(node.right,value+node.val,target,res,not start)
            self.helps(node.left,value,target,res,start)
            self.helps(node.right,value,target,res,start)
            
    
    
#解法3：
class Solution:
    def pathSum(self,root,sum):
        res=[0]
        self.helps(root,0,[],sum,res)
        return(res[0])
    
    def helps(self,node,cursum,lst,target,res):
        if(not node):
            return
        cursum+=node.val
        lst.append(node)
        if(cursum==target):
            res[0]+=1
        t=cursum
        for i in range(len(lst)-1):
            t-=lst[i].val
            if(t==target):
                res[0]+=1
        self.helps(node.left,cursum,lst,target,res)
        self.helps(node.right,cursum,lst,target,res)
        lst.pop()
    
    
    
   
#解法4：
class Solution:
    def pathSum(self,root,sum):
        import collections
        m=collections.defaultdict(int)
        m[0]=1
        return(self.helps(root,0,sum,m))
    
    def helps(self,node,cursum,target,m):
        if(not node):
            return(0)
        cursum+=node.val
        res=m[cursum-target]
        m[cursum]+=1
        res+=self.helps(node.left,cursum,target,m)+\
             self.helps(node.right,cursum,target,m)
        m[cursum]-=1
        return(res)
    
    
    
    
    
    
    
    
    
    




