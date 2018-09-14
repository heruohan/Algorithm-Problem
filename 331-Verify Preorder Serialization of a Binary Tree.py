# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:55:54 2018

@author: hecongcong
"""
'''
The Problem 331:Verify Preorder Serialization of a binary tree.
    One way to serialize a binary tree is to use pre-order traversal. 
When we encounter a non-null node, we record the node's value.
If it is a null node, we record using a sentinel value such as #.
For example, the above binary tree can be serialized to the  string
"9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
    Given a string of comma separated values, verify whether it is a correct
preorder traversal serialization of a binary tree. Find an algorithm without
reconstructing the tree.
'''

'''
The answer:本题是确认一个二叉树前序字符串是否正确，依据题意，当字符串中连续出现两个#号时，
表示这个node为叶节点，可以将此叶节点转换为#号，例如'4##'可以转换为'#'，当字符串循环完后，如果只
剩下'#'，则为正确.
思路：
第一步：将preorder转换为字符形式的list.
第二步：创建一个栈s，依次进入preorder中的元素，当遇到连续两个#时，比如'4##'变为'#'，直至最终
栈中的元素只剩下为'#'.
'''

class Solution:
    def isValidSerialization(self,preorder):
        preorder=preorder.split(',')
        if(preorder==['#']):
            return(True)
        if(preorder[0]=='#'):
            return(False)
        s=[preorder[0]]
        for i in range(1,len(preorder)):
            if(s[0]=='#'):
                return(False)
            if(preorder[i]=='#'):
                while(s and s[-1]=='#'):
                    s.pop()
                    s.pop()
            s.append(preorder[i])
        return(True if(s==['#']) else False)
        
                           
                           
        
                          
                          
                   
               
                
           
           
                      
                      

        
             
    
    

                                
