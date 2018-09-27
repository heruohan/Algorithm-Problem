# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 23:51:53 2018

@author: hecongcong
"""
'''
The problem 332:Reconstruct Itinerary
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.

Note:
1.If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order
 when read as a single string. 
2.All airports are represented by three capital letters.
3.You may assume all tickets form at least one valid itinerary.

Example:
Input:[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output:["JFK","ATL","JFK","SFO","ATL","SFO"]
'''

'''
The answer:本题是要找出一条最小字母顺序的行程路径，并且需要把所给全部城市走完，而且一定会有一条可行路径。
因此，采用深度优先搜索算法，沿着出发城市及到达城市进行搜索，然后进行回溯。当一个城市不在mps中或者其所能到达的城市
都遍历过时，则按顺利将其加入结果中，然后进行回溯.
解题思路：
第一步：把tickets转化为字典形式的数据结构mps，其中key是出发的城市，value是其能达到的城市，并且把value按字母序
进行排序.
第二步：利用deep-first-search算法进行遍历，当走到一个城市时，将其从mps中删除.当一个城市满足不在mps或其达到城市都遍历过
时，将其加入到res中，然后进行回溯.
'''
'''
代码技巧：下面运用两种方式进行代码实现，第一种结合栈s进行回溯，第二种运用递归进行回溯.

'''
####解法一：
def findItinerary(tickets):
    mps={}
    res=[]
    s=['JFK']
    for i in tickets:
        if(i[0] not in mps):
            mps[i[0]]=[i[1]]
        else:
            mps[i[0]].append(i[1])
    while(s):
        tmp=s[-1]
        if((tmp not in mps) or (not mps[tmp])):  ##两个条件的顺序不能变
            res.insert(0,tmp)    ##过程中不满足上述条件的加入到res最后.
            s.pop()
        elif(mps[tmp]):
            t=sorted(mps[tmp])[0]
            s.append(t)
            mps[tmp].remove(t)
    return(res)


    
####解法二：         
def findItinerary1(tickets):
    mps={}
    for i in tickets:
        if(i[0] not in mps):
            mps[i[0]]=[i[1]]
        else:
            mps[i[0]].append(i[1])
    res=[]  ####将其传入dfs函数中，通过迭代可更新.
    dfs(mps,'JFK',res)
    return(res)

def dfs(mps,word,res):   ##其中mps和res在迭代过程中都类似属于全局变量
    while((word in mps) and mps[word]):   ##条件顺序不能变
        t=sorted(mps[word])[0]
        mps[word].remove(t)
        dfs(mps,t,res)
        print('inner:',res)  ##查看res的变化情况
    res.insert(0,word)    ##过程中首先不满足上述条件的，首先加入到res最后.
    print('outer:',res)  ##查看res的变化情况

'''
例如：tickets:[['JFK','KUI'],['JFK','LHR'],['LHR','JFK']]
打印：
outer: ['KUI']
inner: ['KUI']
outer: ['JFK', 'KUI']
inner: ['JFK', 'KUI']
outer: ['LHR', 'JFK', 'KUI']
inner: ['LHR', 'JFK', 'KUI']
outer: ['JFK', 'LHR', 'JFK', 'KUI']
'''
    
            
            
            
            
            
            
            
            
            
            
            
            
            
    
