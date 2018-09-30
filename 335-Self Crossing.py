# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 23:47:21 2018

@author: hecongcong
"""
'''
The problem 335:Self Crossing
    You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north,
then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words,
after each move your direction changes counter-clockwise.
Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.
'''


'''
The answer:本题的题意是从零点开始按照本文的题目条件移动，是否会与其轨迹相交,并且限制为常熟空间的复杂度.
本题难度比较大，通过找规律发现只有三种情况会产生自交.以下di代表第i条边的长度.
第一种情况：第4条边与第1条边相交，及推广到第5条边与第2条边、第6条边与第3条边等等......
以第4与第1条边相交为例，其需满足的condition:
 d1>=d3 and d4>=d2.
 
第二种情况：第5条边与第1条边重合相交，可推广至第6与第2、第7与第3条边等等......
以第5与第1条边重合相交为例，其需满足的condition:
d2==d4 and d5>=d3-d1.

第三种情况：第6与第1条边相交，可推广至第7与第2、第8与第3条边等等......
以第6与第1条边相交为例，其需满足的condition:
d4>=d2 and d3>=d5 and d5>=d3-d1 and d6>=d4-d2.
'''
####代码如下：
def isSelfCrossing(x):
    for i in range(3,len(x)):
        if(x[i-3]>=x[i-1] and x[i]>=x[i-2]):
            return(True)
        if(i>=4 and x[i-3]==x[i-1] and x[i]>=x[i-2]-x[i-4]):
            return(True)
        if(i>=5 and x[i-2]>=x[i-4] and x[i-3]>=x[i-1] and \
           x[i-1]>=x[i-3]-x[i-5] and x[i]>=x[i-2]-x[i-4]):
            return(True)
    return(False)
    
