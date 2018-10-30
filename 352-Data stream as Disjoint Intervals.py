# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:04:37 2018

@author: hecongcong
"""
'''
The question 352:Data stream as Disjoint Intervals
    Given a data stream input of non-negative integers a1, a2, ..., an, ..., 
summarize the numbers seen so far as a list of disjoint intervals.

For example,suppose the integers from the data stream are 1,3,7,2,6...,then the summary will be:
[1,1]
[1,1],[3,3]
[1,1],[3,3],[7,7]
[1,3],[7,7]
[1,3],[6,7]
'''

'''
The answer:本题的题意是，给定一个数据流，概括出不相交的间隔.
比如当data=1时，则为[1,1]，只包含1；data=3时，因为1和3不连续，则为[1,1],[3,3].分别包含数字1和3;
当data=2时，则为[1,3]，包含1，2，3.因为1，2，3连续，即构成区间[1,3]；

解题思路：
第一：首先通过构造函数__init__()，初始化一个SummaryRanges对象的属性ret,既内部全局变量self.ret.
第二：在执行obj.addNum(val)方法时，首先构造new_interval对象和临时存储结果的tmp_ret，以及指针idx.
     然后遍历self.ret，分以下三种情况处理：
     1.当new_interval和interval不overlap且在interval之后时,将interval对象加入到tmp_ret中，并且指针加1.
     2.当new_interval和interval不overlap且在interval之前时,将interval加入tmp_ret即可.
     3.否则，则可合并，既不断更新new_interval.
第三：在遍历完后，将new_interval插入到tmp_ret合适的位置,并且将self.ret赋值为tmp_ret,既更新self.ret；
'''
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
            if(new_interval.start>interval.end+1): #no overlap且在后
                tmp_ret.append(interval)
                idx+=1
            elif(new_interval.end<interval.start-1): #no overlap且在前
                tmp_ret.append(interval)
            else:  ##满足合并条件，更新new_interval
                new_interval.start=min(new_interval.start,interval.start)
                new_interval.end=max(new_interval.end,interval.end)
        tmp_ret.insert(idx,new_interval)   #将更新后的new_interval插入到合适位置
        self.ret=tmp_ret  #更新self.ret
    
    def getIntervals(self):
        return(self.ret)
    
    
#You SummaryRanges object will be instantiated and called as such:
#obj=SummaryRanges()
#obj.addNum(val)
#ret=obj.getIntervals()

    
    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
