# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:17:39 2019

@author: hecongcong
"""

'''
The problem 382:Linked List Random Node
Given a singly linked list,return a random node's value from the linked list.each node must have the same 
probability of being chosen.

Follow up:
what if the linked list is extremely large and its length is unknown to you?could you solve this efficiently
without using extra space?

Example:
//Init a singly linked list [1,2,3].
Listnode head=new Listnode(1)
head.next= new Listnode(2)
head.next.next=new Listnode(3)
Solution solution=new Solution(head)

//getrandom() should return either 1,2 or 3 randomly.each element should have equel probability of returning.
solution.getrandom();
'''

'''
The answer:本题是给定一个单链表，随机返回链表中一个节点的值，进一步，如果链表非常大，大到不知道他的长度时，怎么样不用
额外的空间来求解.以下给出三种解法：

解法1：
1.构造一个列表self.lst,将链表中的元素都放入到列表中，然后随机选取一个并返回.

解法2：
1.求出链表的长度，然后随机返回一个指针idx，并循环找出idx指针所对应的节点值.

解法3：蓄水池抽样算法
针对链表很大，大到不知道它的长度的时候，可以采用蓄水池抽样算法.这里的蓄水池容量k=1.
1.首先将链表的第一个元素放入蓄水池中，既res指向链表的第一个元素.
2.循环链表，然后第二个元素取1/2的概率，第三个元素取1/3得概率，以此类推....
3.循环完毕后，链表中的每个元素被取到的概率都相同.
详细证明见我学习笔记.
代码如下.
'''

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
        






















