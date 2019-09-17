# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 22:13:31 2019

@author: hecongcong
"""

'''
Question 445:Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers.the most significant digit comes first
and each of their node contain a single digit.Add the two numbers and return it as a linked list.

you may assume the two numners do not contain any leading zero,except the number 0 itself.
Follow up:
what if you can not modified the input lists? In other words,reversing the lists is not allowed.

Example:
Input:(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output:7 -> 8 -> 0 -> 7
'''


'''
Answer:本题是给定两个单链表，分别代表两个非负的整数，然后相加，并将其结果用链表表示；因为链表只能从前往后循环，而加法是从
后往前进行的，所以有以下两种解法。
解法1：栈数据结构辅助
1.构建两个栈s1和s2,分别将链表l1和l2各个节点的值存入；
2.然后，根据栈的先进后出的原则，循环对两个栈的顶部元素进行操作，并且考虑进位的情况；

解法2：递归
1.递归的思想就是层层将大问题，分解为相关联的小问题，因此，本题可以用递归来解答；
2.构建递归函数helper(l1,l2,diff),其中l1,l2表示两个要相加的链表，并且l1的长度肯定大于l2，diff是两个链表长度的差值，
此函数的返回值为两个链表的相加值，但是没有考虑最高一位的进位情况；
3.在主函数中，将递归函数返回值的最高位进位情况考虑进去，并返回结果；
'''

#definition for singly-linked list.
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
'''

####解法1：栈数据结构辅助

class Solution:
    def addTwoNumbers(self,l1,l2):
        s1=[]
        s2=[]
        
        while(l1):
            s1.append(l1.val)
            l1=l1.next
        while(l2):
            s2.append(l2.val)
            l2=l2.next
        
        jinwei=0
        cur=None
        
        while(s1!=[] or s2!=[]):
            if(s1!=[]):
                val1=s1.pop()
            else:
                val1=0
            
            if(s2!=[]):
                val2=s2.pop()
            else:
                val2=0
            
            sums=val1+val2+jinwei
            jinwei=sums//10
            
            res=ListNode(sums%10)
            res.next=cur
            
            cur=res
        if(jinwei==0):
            return res
        else:
            res=ListNode(jinwei)
            res.next=cur
            return res
        
        
###精简
class Solution:
    def addTwoNumbers(self,l1,l2):
        s1=[]
        s2=[]
        while(l1):
            s1.append(l1.val)
            l1=l1.next
        
        while(l2):
            s2.append(l2.val)
            l2=l2.next
        
        sums=0
        cur=ListNode(0)
        while(s1!=[] or s2!=[]):
            if(s1!=[]):
                sums+=s1.pop()
            if(s2!=[]):
                sums+=s2.pop()
            
            cur.val=sums % 10
            res=ListNode(sums//10)
            res.next=cur
            cur=res
            sums//=10
        return(cur.next if(cur.val==0) else cur)
        


 #解法2：递归
class Solution:
    def addTwoNumbers(self,l1,l2):
        len_1=self.getLength(l1)
        len_2=self.getLength(l2)
        head=ListNode(1)
        child=self.helper(l1,l2,len_1-len_2) if(len_1>len_2) else self.helper(l2,l1,len_2-len_1)
        
        if(child.val>9):
            child.val %=10
            head.next=child
            return head
        return child
      
    
    def getLength(self,node):
        count=0
        while(node):
            count+=1
            node=node.next
        return count
    
    def helper(self,l1,l2,diff):
        if(not l1):
            return None
        res=ListNode(l1.val+l2.val) if(diff==0) else ListNode(l1.val)
        child=self.helper(l1.next,l2.next,0) if(diff==0) else self.helper(l1.next,l2,diff-1)
        
        if(child and child.val>9):
            child.val %=10
            res.val+=1
        res.next=child
        return res

        
JAVA：
/**
*Definition for singly-linked list.
*public class ListNode
{
    int val;
    ListNode next;
    ListNode(int x)
    {
        val=x;
    }
}
*/

//解法1：栈数据结构辅助
class Solution{
    public ListNode addTwoNumbers(ListNode l1,ListNode l2)
    {
        Stack<Integer> s1=new Stack<>();
        Stack<Integer> s2=new Stack<>();
        
        while(l1!=null)
        {
            s1.push(l1.val);
            l1=l1.next;
        }
        
        while(l2!=null)
        {
            s2.push(l2.val);
            l2=l2.next;
        }
        
        int sum=0;
        ListNode cur=new ListNode(0);
        while(!s1.empty() || !s2.empty())
        {
            if(!s1.empty())
            {
                sum+=s1.pop();
            }
            
            if(!s2.empty())
            {
                sum+=s2.pop();
            }
            
            cur.val=sum % 10;
            ListNode res=new ListNode(sum/10);
            res.next=cur;
            cur=res;
            
            sum/=10;
        }
        
        return cur.val==0 ? cur.next : cur;
    }
}



//解法2：递归
class Solution{
    public ListNode addTwoNumbers(ListNode l1,ListNode l2)
    {
        int len_1=getLength(l1);
        int len_2=getLength(l2);
        
        ListNode head=new ListNode(1);
        ListNode child=len_1>len_2 ? helper(l1,l2,len_1-len_2) : helper(l2,l1,len_2-len_1);
        
        if(child.val>9)
        {
            child.val %=10;
            head.next=child;
            return head;
        }
        
        return child;
    }
    
    public int getLength(ListNode node)
    {
        int count=0;
        while(node!=null)
        {
            count++;
            node=node.next;
        }
        return count;
    }
    
    public ListNode helper(ListNode l1,ListNode l2,int diff)
    {
        if(l1==null)
        {
            return null;
        }
        
        ListNode res=diff==0 ? new ListNode(l1.val+l2.val) : new ListNode(l1.val);
        ListNode child=diff==0 ? helper(l1.next,l2.next,0) : helper(l1.next,l2,diff-1);
        
        if(child!=null && child.val>9)
        {
            child.val %=10;
            ++res.val;
        }
        
        res.next=child;
        return res;
        
    }
}


        
        
