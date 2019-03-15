# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 00:03:37 2019

@author: hecongcong
"""

'''
The Problem 429:N-ary Tree Level Order Traversal
Given an N-ary Tree,return the level order traversal of its node's values.(ie,from left to right,level by level).
For Example,give a 3-ary tree:
                       1
                    /  | \
                   3   2  4
                  / \
                 5   6
 we should return its level order traversal:
 [
     [1],
     [3,2,4],
     [5,6]
]
Note:
1.the depth of the tree is at most 1000.
2.the total number of nodes is at most 5000.
'''



'''
The answer:本题是给定一个N元的树，返回它的水平顺序遍历.
本题可以用递归和迭代辅助栈的解法进行解法，如下：

解法1：递归
1.首先构建一个辅助函数helps(node,level,res),其中参数level表示当前节点node的深度，即其在第几层，res用于存储每层结果；
2.在辅助函数里面，首先判断res的长度是否小于等于当前深度，如果为空的话，则需要加一个空列表进去，用以存储当面深度的结果；
3.然后循环当前节点node的子节点数组，进行递归，深度则加1；
4.在主函数里调用辅助函数，并返回结果；
代码如下；


解法2：迭代+栈
思路：解法2的思路和解法1基本一样，只是用栈st存储节点和其对应的深度的元组；
代码如下；


解法3：迭代+栈
思路：解法3的栈st里面只需要存储节点，并且每层循环过程中，都新建一个空列表t，存储当前层的结果，而控制当前层则用一个for循环，
因此当前st的长度即为当前层节点数的个数，同时，在python中即使st在变化，如果用for _ in range(len(st)),进行循环的话，其也是按顺序调用，
即len(st)只会调用一次st的初始状态；所以能保证t里面只存储当前层的节点值；
'''

'''
#Definition for a Node.
class Node:
    def __init__(self,val,children):
        self.val=val
        self.children=children
'''


#解法1：
class Solution:
    def levelOrder(self,root):
        res=[]
        self.helps(root,0,res)
        return(res)
        
    def helps(self,node,level,res):
        if(not node):
            return
        if(len(res)<=level):
            res.append([])
        res[level].append(node.val)
        for i in node.children:
            self.helps(i,level+1,res)




#解法2：
class Solution:
    def levelOrder(self,root):
        res=[]
        st=[(root,0)]
        while(st):
            tmp=st.pop()
            if(tmp[0]):
                if(len(res)<=tmp[1]):
                    res.append([])
                res[tmp[1]].append(tmp[0].val)
                for i in tmp[0].children:
                    st.insert(0,(i,tmp[1]+1))
        return(res)
        


#解法3：
class Solution:
    def levelOrder(self,root):
        if(not root):
            return([])
        res=[]
        st=[root]
        while(st):
            t=[]
            for _ in range(len(st)):   #调用len()函数后，其状态就不会随着st的变化而变，不会在循环过程中在调用
                tmp=st.pop()
                t.append(tmp.val)
                for i in tmp.children:
                    st.insert(0,i)
            res.append(t)
        return(res)
        




