# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:59:21 2019

@author: hecongcong
"""

'''
The problem 390:Elimination Game
there is a list of sorted integers from 1 to n.starting from left to right,remove the first number and
every other number afterword until you reach the end of the list.
repeating the previous step again,but this time from right to left,remove the right most number and every
other number from the remaining numbers.
we keep repeating the steps again,alternating left to right and right to left,until a single number remains.
Find the last number that remains starting with a list of length n.

Example:
Input:n=9
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6
Output:6
'''


'''
The answer:本题是给定一个从1到n的列表，先从左到右间隔一个元素进行删除，然后从右到左继续上述的过程，直到只剩下一个元素.
本题可以采用三种解法，如下：

解法1：递归
1.递归的退出条件是当n=1时，返回1.然后一个指示变量flag,当flag=True时，从左到右，当flag=False时，从右到左.
2.当从左到右时，不管n的奇偶性，他的结果就是等于2倍的n//2从右到左；因为比如：
  当n=2k时，只删除奇数，所以剩下2，4，....2k,既2倍的1,2,....k从右到左的结果;
  当n=2k+1时，只删除奇数，所以剩下2,4,....2k,既2倍的1,2...k从右到左的结果；
3.当从右到左时，需要考虑n的奇偶性，如下：
  当n=2k时，只删除偶数，所以剩下1,3,5...2k-1,既2倍的1,2,...k从左到右的结果减1.
  当n=2k+1时，只删除奇数，所以剩下2,4,...2k,既2倍的1,2...k从左到右的结果.
代码如下.

解法2：等差数列法
1.1到n以及此后每轮保留下来的数组，可以看作是一个等差数列，可以用可以用左右两个端点low,high和公差gap进行描述；
2.然后以flag=True表示从左到右，flag=False表示从右到左.当low等于high时，既剩下一个元素，返回即可；
3.每轮数列的个数用nums计算出来，当从左到右删除时，结果数列，low肯定会向前移动一个公差，同时，当nums是奇数时，high向后移动一个公差，
否则，high不变；
4.当从右到左删除是，结果数列，high肯定会向后移动一个公差，同时，当nums是奇数时，low会向前移动一个公差，否则，low不变；
5.每完成一轮后，公差gap扩大一倍，flag方向变；
代码如下.


解法3：变异解法
1.本解法可以看作是等差数列解法的延伸，只需要维护左端点low,和公差gap;同时剩下的最后一个元素必定是low.
2.可用gap*2是否小于等于n，来判断是否只剩下一个元素，同时，用n//gap判断剩下的数组元素的个数；
3.然后把不同方向两个过程写道同一个循环里面，最后只剩下一元素时，返回low即可；
代码如下；

'''
#解法1
class Solution:
    def lastRemaining(self,n):
        return(self.helpFn(n,True))
        
    def helpFn(self,n,flag):
        if(n==1):
            return(1)
        if(flag):
            return(2*self.helpFn(n//2,False))
        else:
            return(2*self.helpFn(n//2,True)-1+(n % 2))
            


#解法2
class Solution:
    def lastRemaining(self,n):
        low,high=1,n
        gap=1
        flag=True
        while(low<high):
            nums=(high-low)//gap+1
            if(flag):
                low+=gap
                if(nums % 2==1):
                    high-=gap
            else:
                high-=gap
                if(nums % 2==1):
                    low+=gap
            gap*=2
            flag=not flag
        return(low)


#解法3
class Solution:
    def lastRemaining(self,n):
        low=1
        gap=1
        while(2*gap<=n):   #判断剩下的数组是否还剩下一个元素
            low+=gap       #从左到右过程，更新low.
            gap*=2         #从左到右过程，更新gap,既扩大2倍
            if(gap*2>n):   #判断剩下的数组是否还剩下一个元素
                break
            if((n//gap) % 2==1):      #从右到左过程，判断数列个数是否为奇数，如为奇数，则更新low,否则不变.
                low+=gap
            gap*=2             #从右到左过程，更新gap，既扩大2倍
        return(low)
        









