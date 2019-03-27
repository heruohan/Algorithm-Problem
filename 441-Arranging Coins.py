# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:56:10 2019

@author: hecongcong
"""


'''
The problem 441:Arranging Coins
you have a total of n coins that you want to form in a staircase shape,where every k-th row must have exactly k
coins.Given n,find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example1:
n=5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
because the 3rd row is incomplete,we return 2.
Example2:
n=8
the coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
because the 4th row is incomplete,we return 3.
'''

'''
The answer:本题是给定n个硬币，叫排成阶梯状，必须满足第k行放k个硬币，问能放多少行满格的阶梯；


解法1：暴力解法
思路：循环，第i行放置i个硬币，直到剩下的硬币数量小于等于下一行的行数；返回即可；
代码如下；

解法2：二分查找法
思路：利用等差数列的求和公式，然后运用二分查找法；
代码如下；

解法3：数学推倒法
思路：直接利用等差数列的求和公司row*(row+1)//2=n;求出row,然后向下取正整数，既所求；
因为：
第一种情况：当n刚好能排满时，求出来的row即为正整数，为所求；
第二种情况：当n不能排满时，x行算出来的硬币数肯定小于n，而x+1行算出来的硬币数肯定大于n,而用上述公式求出来
的row肯定位于x与x+1之间，因此正确结果为向下取整，即为x；
代码如下；
'''
#解法1
class Solution:
    def arrangeCoins(self,n):
        i=1
        count=0
        while(n-count>=i):
            count+=i
            i+=1
        return(i-1)
        




#解法2：
class Solution:
    def arrangeCoins(self,n):
        if(n<=1):
            return(n)
        left=1
        right=n
        while(left<right):
            mid=(left+right)//2
            if(mid*(mid+1)//2<=n):
                left=mid+1
            else:
                right=mid
        return(left-1)


#解法3：
class Solution:
    def arrangeCoins(self,n):
        return(int(((8*n+1)**0.5-1)//2))





