# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 00:03:37 2019

@author: hecongcong
"""



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
            for _ in range(len(st)):
                tmp=st.pop()
                t.append(tmp.val)
                for i in tmp.children:
                    st.insert(0,i)
            res.append(t)
        return(res)
        




