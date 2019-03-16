# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:21:52 2019

@author: hecongcong
"""


'''
The problem 435:Non-overlapping Intervals
given a collection of intervals,find the minimum number of intervals you need to remove
to make the rest of the intervals non-overlapping.
Note:
1.you may assume the intervals's end point is always bigger than its start point.
2.interval like [1,2] and [2,3] have borders 'touching' but they do not overlap each other.

Example1:
input:[ [1,2], [2,3], [3,4], [1,3] ]
output:1
Explanation:[1,3] can be removed and the rest of intervals are non-overlapping.
Example2:
input:[[1,2],[1,2],[1,2]]
output:2
Explanation:you need to remove two [1,2] to make the rest of intervals non-overlapping.
Example3:
input:[[1,2],[2,3]]
output:0
explanation:you do not need to remove any of the intervals since they are already non-overlapping.
'''


'''
The answer:本题是给定一个区间的集合intervals,找出可以删除的最小区间数量，使得剩下的区间之间不重叠；

解法1：
1.首先将intervals按元素的终点进行升序排列，并构建一个栈st，将终点最小的区间放入；并初始化索引idx=0,和统计量count=0.
2.然后从第二个元素开始循环，如果当前元素i的起点大于st中最后一个元素的终点，则直接将其插入到st的最后；如果当前元素的终点小于st中当前元素
的起点，则将其插入当st中的当前位置，循环结束；因为st中的元素是按顺序排列的不重叠区间，且之前已经依次循环判断过当前元素的起点大于等于st中之前元素的终点，
所以插入当当前位置，其必然不会重叠，维持了st中元素的属性；
3.如果当前元素的起点大于等于st中当前元素的终点，则需要向后继续找合适的位置；
4.根据上面两个判断条件不满足，可以得出当前元素i的起点必然小于st中当前元素的终点，且当前元素的终点必然大于st中当前元素的起点，又因为一个区间的终点
必然大于其起点，所以此时两个区间必然重叠，则必然删除一个(最优应删除终点小的区间)，count加1，结束循环；
5.循环完毕后，idx重置为0；外层循环结束后，返回结果；
代码如下；


解法2：
1.将intervals按起点升序排列，然后构建一个cur=0，表示指向判断过的不重叠区间的最后一个；
2.然后从第二个元素开始循环，如果指向的元素intervals[cur]的终点大于当前元素intervals[i]的起点，则必有重叠，需删除一个，这在这种
情况下，需要删除两者中终点较大的区间，因此更新cur为区间终点较小的索引；(实际是不删除的，只更新cur即可)
3.如果没有重叠，也更新cur到当前循环的元素；最后循环完毕，返回结果；
代码如下；


解法3：
解法3和解法2的思路一样，只是换了种写法；
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
                else:         #则两个区间必有重叠，必须删除一个，最优的是删除终点小的那个区间
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
            tmp=1 if(cur>intervals[i].start) else 0    #或直接这样写:tmp=cur>intervals[i].start
            cur=min(cur,intervals[i].end) if(tmp) else intervals[i].end    #tmp为真则为重复的情况，去两者的较小值
            count+=tmp
        return(count)
            
            
            
            
            
            
            
            
            

    














