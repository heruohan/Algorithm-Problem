# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:25:31 2019

@author: hecongcong
"""



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
            if(i.end>start[-1]):
                res.append(-1)
                visited[i.end]=-1
                continue
            idx=bisect.bisect_left(start,i.end)
            res.append(m[start[idx]])
            visited[i.end]=m[start[idx]]
        return(res)













