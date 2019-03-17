# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:25:31 2019

@author: hecongcong
"""


'''
The problem 436:Find Right interval
Given a set of intervals,for each of the interval i,check if there exists an interval j whose start point
is bigger than or equal to the end point of the interval i,which can be called that j is on the 'right' of i.
for any ineterval i,you need to store the minimum interval j's index,which means that the interval j has the minimum
start point to build the 'right' relationship for interval i.if the interval j does not exists,store -1 for the interval
i.finally,you need output the stored value of each interval as an array.
Note:
1.you may assume the interval's end point is always bigger than its start point.
2.you may assume none of these intervals have the same start point.
Example1:
input:[ [1,2] ]
output:[-1]
Explantion:there is only one interval in the collection,so it outputs -1.
Example2:
input: [ [3,4], [2,3], [1,2] ]
output:[-1,0,1]
explanation:there is no satisfied 'right' interval for [3,4].
for [2,3],the interval [3,4] has minimum 'right' start point.
for [1,2],the interval [2,3] has minimum 'right' start point.
Example3:
input:[ [1,4], [2,3], [3,4] ]
output:[-1, 2, -1]
explanation:there is no satisfied 'right' interval for [1,4] and [3,4].
for [2,3],the interval [3,4] has minimum 'right' start point.
'''



'''
The answer:本题是给定一个区间的集合intervals，找出各个区间终点，集合种其他区间起点大于等于其终点的最小值区间的索引，如果不存在就为-1，且集合
种每个区间的起点都不一样；

解题思路：因为集合种每个区间的起点不一样，所以将intervals种各个区间的起点与其索引映射存入字典m种，同时将起点放入到start数组种，
然后在对start按升序排序，同时构建一个visited字典，用以存储访问过的区间终点的结果，提高效率；
然后循环intervals,对于每个元素的终点i.end，我们用二分查找法在start里面找第一个大于等于i.end的值，然后从m中取出索引放入结果中；
最后返回结果；
代码如下；
'''

'''
Definition for an interval.
class Interval:
    def __init__(self,s=0,e=0):
        self.start=s
        self.end=e
'''

#解法1：
class Solution:
    def findRightInterval(self,intervals):
        import bisect
        m={}
        visited={}
        start=[]
        res=[]
        lens=len(intervals)
        for i in range(lens):
            m[intervals[i].start]=i
            start.append(intervals[i].start)
        start.sort()
        for i in intervals:
            if(i.end in visited):
                res.append(visited[i.end])
                continue
            if(i.end>start[-1]):   #这种情况就是找不到，则返回-1
                res.append(-1)
                visited[i.end]=-1
                continue
            idx=bisect.bisect_left(start,i.end)  #在start里运用二分查找法找第一个大于等于i.end的索引
            res.append(m[start[idx]])   
            visited[i.end]=m[start[idx]]
        return(res)













