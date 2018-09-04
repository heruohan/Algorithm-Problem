# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 23:18:27 2018

@author: hecongcong
"""

'''
The Problem:328.Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Input:1->2->3->4->5->NULL
Output:1->3->5->2->4->NULL

Note:
1.The relative order inside both the even and odd groups should remain as it was in the input.
2.The first node is considered odd, the second node even and so on ...
'''

'''
The answer:本题是给一个单向链表，在相对顺序不变下，把偶数部分放到奇数部分后面.
My思路：运用两个指针，pre指向奇数节点位置，cur指向偶数节点位置，然后把cur后面的节点提到
pre后面，pre和cur依次前进一位.

代码实现技巧及难点：
1.对于复杂数据结构link，list等，其copy的副本，在不赋值的情况下，内部内容的改变具有传递性及同步性.
例如：a=[1,2,[3,4]],令b=a,则：
command1:b[0]=100,则b=[100,2,[3,4]],a=[100,2,[3,4]].
command2:b=b[2]、b[0]=100,则b=[100,4],a=[100,2,[100,4]].
2.代码中的奇数组根据pre的变化，在head里同步跟新;
偶数组根据cur的变化，在t中同步跟新.
'''
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
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
