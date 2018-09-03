# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 23:18:27 2018

@author: hecongcong
"""

#Definition for singly-linked list.
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
'''
class Solution:
     def oddEvenList(self, head):
         """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None or head.next==None):
            return(head)
        pre=head
        cur=head.next
        t=cur
        while(cur and cur.next):
            pre.next=cur.next
            pre=pre.next
            cur.next=pre.next
            cur=cur.next
        pre.next=t
        return(head)
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            