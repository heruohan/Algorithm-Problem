# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:04:37 2018

@author: hecongcong
"""

#Definition for an interval.
class Interval:
    def __init__(self,s=0,e=0):
        self.start=s
        self.end=e


class SummaryRanges:
    def __init__(self):
        self.ret=[]
    
    def addNum(self,val):
        new_interval=Interval(val,val)
        tmp_ret=[]
        idx=0
        for interval in self.ret:
            if(new_interval.start>interval.end+1):
                tmp_ret.append(interval)
                idx+=1
            elif(new_interval.end<interval.start-1):
                tmp_ret.append(interval)
            else:
                new_interval.start=min(new_interval.start,interval.start)
                new_interval.end=max(new_interval.end,interval.end)
        tmp_ret.insert(idx,new_interval)
        self.ret=tmp_ret
    
    def getIntervals(self):
        return(self.ret)
    
    
                
                
                
                
                
                
                
                
                
                
                
                
                
                