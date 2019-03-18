# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:07:13 2019

@author: hecongcong
"""


'''
The problem 437:Path Sum III
you are given a binary tree in which each node contains an integer value.
find the number of paths that sum to a given value.
the path does not need to start or end at the root or a leaf,but it must go downwards(traveling only from parent nodes to
children nodes).
The tree has no more than 1000 nodes and the values are in the range  -1,000,000 to 1,000,000.

Example:
root=[10,5,-3,3,2,null,11,3,-2,null,1],sum=8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
return 3.the paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''


'''
The answer:本题给定一个二叉树以及一个给定的正整数sum,求出有多少条路径使得其上面的元素相加等于sum.
思路：求一条路径有以下原则：1、从上到下，一个节点可以为起始点，也可以不为起始点；
                         2、如果已经成为起始点后，其后必然都要连续；
                         3、因为节点值有正有负，所以当一条路径的和为sum,则也要向下继续搜索验证；

解法1：递归
思路：递归有三个部分，第一部分是必包含root的节点的路径的数量，所以需要写一个辅助函数helps;其余两部分是不包含root节点的路径数量，
即分别是左右子节点所包含的路径和为sum的数量；三部分的和则为整个root数所有路径和为sum的数量；
代码如下；

解法1的代码1：
其思路和解法1相同，只是辅助函数helps(node,cursum,target)的写法更加简洁，参数node为当前节点，cursum表示截止到其父节点的路径累积和；函数
的含义为必包含当前节点node,其路径累积和为target的所有路径数量；
代码如下；


解法2：
思路：首先构建一个辅助函数helps(node,value,target,res,start),参数value是截止到当前节点node的父节点的累积和，res是一个存储路径数量的数组，
start是一个开关变量，为True表示在当前节点时，路径的起始位置已经存在了；为False表示在当前节点时路径的起始点还不存在；
因此，当start为True时，其路径和里肯定包含当前节点的值；当start为False时，当前节点可以为起始点，也可以不为起始点，即继续向下寻找起始点；
代码如下；


解法3：
思路：首先构建一个辅助函数helps(node,cursum,target,lst,res),参数node表示当前节点，cursum表示根节点到截止到当前节点的父节点的路径的累计和，
lst用以存储根节点到当前节点路径上的所有节点；
然后每到一个节点，算出根节点到当前节点，所有子路径的累积和，然后看是否等于sum;
需要注意的是当当前节点加入lst中，其后面的子节点用完后，当递归到其父节点的另一个子节点后，需要将其从lst中删除(对于所有的节点同样适用);


解法4：
思路：

'''

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
        lst.pop()   #用完后，需要将node从lst中删除
    
    
    
   
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
    
    
    
    
    
    
    
    
    
    




