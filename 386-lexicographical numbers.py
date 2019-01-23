# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 14:55:12 2019

@author: hecongcong
"""

'''
The problem 386:lexicographical numbers
Given an integer n,return 1--n in lexicographical order.
for example,given 13:return:[1,10,11,12,13,2,3,4,5,6,7,8,9].
please optimize your algorithm to use less time and space.the input size may be as large as 5000000.
'''


'''
The answer:本题是给定一个正整数n，返回用字典序排列的1到n的数组.如果用原始方法，定义一个用字典序排序的函数，
会超时.因此，找寻规律，可以采用另一种方法.
字典序的定义：给定两个对象，按位进行比较，如果相应的位较小，则相应的对象就小；如果相应的位相同，则继续向后移动
一位进行比较；a=100,b=21,因为第一位2大，所以按字典序b>a.如果两者所有位都相同，则短的较小；

解法：
1.构建一个长度位n的数组res,及cur=1,然后在小于n的范围内，不断用cur乘以10，更新cur,达到最高位，比如1,10,100....
2.然后，从最后一位不断加1进行更新，如果更新进位后后面为0,则需要将0去掉，比如cur=109,加1后为110,但是按字典序排序的
话11比110小；
3.如果更新到cur>=n,则需要将cur退一位，加1.比如，n=123,cur=123,则更新cur=cur//10+1=13,一直到最前一位为9；

这道题有规律可循，仔细思考.
代码如下.
'''
class Solution:
    def lexicalOrder(self,n):
        res=[0]*n
        cur=1
        for i in range(n):
            res[i]=cur
            if(cur*10<=n):
                cur*=10
            else:
                if(cur>=n):
                    cur//=10
                cur+=1
                while(cur % 10==0):
                    cur//=10
        return(res)
        
        
        
        
        
        
        
