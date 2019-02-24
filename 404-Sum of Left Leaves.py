# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 23:19:51 2019

@author: hecongcong
"""


'''
The problem 404:Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.
Example:
    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree,with values 9 and 15 respectively.return 24.
'''


'''
The answer:本题是给定一个二叉树，返回所有左子叶节点的和.
本题可以用递归和迭代两种方法做，如下：

解法1：递归
1.当root==None时，返回0，如果root的左子树为None的话，则直接对root的右子树调用递归函数，并返回.
2.否则，当root的左子树的左右子树都为0的话，此时代表root的左子树是叶子节点，因此对右子树调用递归函数，同时加上左子树的
节点值，并返回；
3.否则，直接对左右子树分别调用递归函数，相加并返回；
代码如下；


解法2：迭代
1.当root为None或者其左右子树均为None时返回0；
2.构建一个栈s及res=0,首先将root压入，循环，如果栈顶元素tmp的左子树!=None,同时，如其左子树的左右子树均为None的话，则
说明其是一个左叶子树，将其值累加到res.否则将其左子树压入s中；
3.如果tmp的右子树不为None的话，则将其压入s中；
4.循环完毕后，返回res；
代码如下；
'''


#解法1
class Solution:
    def sumOfLeftLeaves(self,root):
        if(root==None):
            return(0)
        l=root.left
        r=root.right
        if(l==None):
            return(self.sumOfLeftLeaves(r))
        else:
            if(l.left==None and l.right==None):
                return(l.val+self.sumOfLeftLeaves(r))
            else:
                return(self.sumOfLeftLeaves(l)+self.sumOfLeftLeaves(r))




#解法2
class Solution:
    def sumOfLeftLeaves(self,root):
        if(root==None or (root.left==None and root.right==None)):
            return(0)
        s=[]
        s.append(root)
        res=0
        while(s):
            tmp=s.pop()
            if(tmp.left):
                if(tmp.left.left==None and tmp.left.right==None):
                    res+=tmp.left.val
                else:
                    s.append(tmp.left)
            if(tmp.right):
                s.append(tmp.right)
        return(res)
        











