# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:21:52 2019

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
    def eraseOverlapIntervals(self,intervals):
        if(not intervals):
            return(0)
        a=sorted(intervals,key=lambda x:x.end)
        st=[a[0]]
        idx=0
        count=0
        for i in a[1:]:
            if(i.start>=st[-1].end):
                st.append(i)
                continue
            while(idx<len(st)):
                if(i.end<=st[idx].start):
                    st.insert(idx,i)
                    break
                elif(i.start>=st[idx].end):
                    idx+=1
                elif(i.end>=st[idx].end):
                    count+=1
                    break
            idx=0
        return(count)



#解法2：
class Solution:
    def eraseOverlapIntervals(self,intervals):
        intervals.sort(key=lambda x:x.start)
        count=0
        cur=0
        lens=len(intervals)
        for i in range(1,lens):
            if(intervals[cur].end>intervals[i].start):
                count+=1
                if(intervals[cur].end>intervals[i].end):
                    cur=i
            else:
                cur=i
        return(count)
        
        
        
#解法3：
class Solution:
    def eraseOverlapIntervals(self,intervals):
        if(not intervals):
            return(0)
        intervals.sort(key=lambda x:x.start)
        count=0
        cur=intervals[0].end
        lens=len(intervals)
        for i in range(1,lens):
            tmp=1 if(cur>intervals[i].start) else 0
            cur=min(cur,intervals[i].end) if(tmp) else intervals[i].end
            count+=tmp
        return(count)
            
            
            
            
            
            
            
            
            

    














