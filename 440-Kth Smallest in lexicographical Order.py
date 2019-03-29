# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 23:58:46 2019

@author: hecongcong
"""


'''
The problem 440:K-th Smallest in Lexicographical Order
Given integers n and k,find the lexicographically k-th smallest integer in the range from 1 to n.
Note:1<=k<=n<=10**9.

Example:
input:n=13,k=2
output:10
Explanation:the lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],so the second smallest
number is 10.
'''


'''
The answer:本题是给定两个整数n和k，在1到n之间找出按字典序排列的第k个大小的数字；
如果用暴力解法，排列出1到n之间所有数字的字典序，然后在取出第k个数字的话，这样会超时；
因此，我们需要换一种思路，快速的定位到第k个数字的位置；

核心思路：仔细观察1到n之间按字典序排列的结果，会发现结果可以组成一个类似于十叉树的树形结构，比如1到21的字典序排序，
1的子节点为10到19,2的子节点为20，21；3到9没有子节点；并且树形结构遵循以下规则：
1、父节点按字典序肯定比子节点小；
2、同一父节点的所有子节点按字典序从左到右依次增大；
3、同一水平的节点，从左到右依次增大；

因此，解题步骤如下：
1.首先将当前节点设置为1，进入循环while(k>1),这样就可以排除当前节点cur,找出1到2之间按字典序排列的所有数字的个数count.
因为每层的节点数可以用end-start表示；且因为是十叉树，所以在满足start<=n的情况下，start和end分别扩大10倍，即可包含一
层的所有节点数，如果end大于最大范围n的话，则用n代替end计算当前层的节点数量；
2.找出cur与其同层的下一个节点即cur+1，之间包含的所有节点数的个数count后，如果k大于count说明需要找的数位于cur+1树里面，
因此，更新cur和k；
如果k<=count,则需要找的数字必定位于cur的子节点中，也更新cur和k;
代码如下；


'''
#解法1：
class Solution:
    def findKthNumber(self,n,k):
        cur=1
        while(k>1):
            count=0
            start=cur
            end=cur+1
            while(start<=n):
                count+=min(end,n+1)-start
                start*=10
                end*=10
            if(k>count):
                cur+=1
                k-=count
            else:
                cur*=10
                k-=1
        return(cur)














