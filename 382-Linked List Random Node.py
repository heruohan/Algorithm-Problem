# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:17:39 2019

@author: hecongcong
"""



#Definition for singly-linked list.
#class ListNode:
#    def __init__(self,x):
#        self.val=x
#        self.next=None

#解法1

class Solution:
    def __init__(self,head):
        '''
        @param head the linked list's head.
        Note that the head is guaranteed to be not null,so it contains
        at least one node.
        :type head:ListNode
        '''
        self.lst=[]
        while(head):
            self.lst.append(head.val)
            head=head.next
    def getRandom(self):
        '''
        returns a random node's values.
        :rtype:int
        '''
        import random
        return(self.lst[random.randint(0,len(self.lst)-1)])



#解法2
class Solution:
    def __init__(self,head):
        '''
        @param head the linked list's head.
        Note that the head is guaranteed to be not null,so it contains
        at least one node.
        :type head:ListNode
        '''
        self.node=head
        self.lens=0
        while(head):
            self.lens+=1
            head=head.next
    def getRandom(self):
        '''
        returns a random node's values.
        :rtype:int
        '''
        import random
        idx=random.randint(0,self.lens-1)
        cur_node=self.node
        while(idx):
            idx-=1
            cur_node=cur_node.next
        return(cur_node.val)


#解法3：蓄水池抽样算法
class Solution:
    def __init__(self,head):
        '''
        @param head the linked list's head.
        Note that the head is guaranteed to be not null,so it contains
        at least one node.
        :type head:ListNode
        '''
        self.node=head
    def getRandom(self):
        '''
        returns a random node's values.
        :rtype:int
        '''
        import random
        res=self.node.val
        i=2
        cur_node=self.node.next
        while(cur_node):
            j=random.randint(0,i-1)
            if(j==0):
                res=cur_node.val
            i+=1
            cur_node=cur_node.next
        return(res)
        






















