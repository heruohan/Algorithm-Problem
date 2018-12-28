# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 15:56:58 2018

@author: hecongcong
"""

'''
The problem 374:Guess Number Higher or Lower
We are playing the guess game,the game is as follows:
I pick a number from 1 to n.You have to guess which number i picked.
every time you guess wrong,i will tell you whether the number is higher or lower.
You call a pre-defined API guess(int(num)) which return 3 possible results (-1,1,or 0):
-1: My number is lower.
1: My number is higher.
0: congrats! You got it!

Example:
Input:n=10,pick=6
Output:6
'''

'''
The answer:本题是经典的猜字游戏，给定一个正整数n，从1到n里面猜出我所选择的数，每次如果猜错的话，就会得到猜大或者猜小的提示，
其guess函数的返回值给出.本题用二分查找法解题.

代码如下.
'''


#The guess API is already defined for you.
#@param num,your guess
#@return -1 if my number is lower,1 if my number is higher,otherwise return 0
#def guess(num):



class Solution:
    def guessNumber(self,n):
        left=1
        right=n
        while(left<right):
            mid=(left+right)//2  #如下python2:mid=int((left+right)/2)
            tmp=guess(mid)
            if(tmp==0):
                return(mid)
            elif(tmp==-1):
                right=mid-1
            else:
                left=mid+1
        return(left)
        
        
        
        
        
