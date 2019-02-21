# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 23:19:51 2019

@author: hecongcong
"""



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
        











