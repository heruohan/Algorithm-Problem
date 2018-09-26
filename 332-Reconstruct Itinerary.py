# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 23:51:53 2018

@author: hecongcong
"""

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
        if((tmp not in mps) or (not mps[tmp])):
            res.insert(0,tmp)
            s.pop()
        elif(mps[tmp]):
            t=sorted(mps[tmp])[0]
            s.append(t)
            mps[tmp].remove(t)
    return(res)


    
####         
def findItinerary1(tickets):
    mps={}
    for i in tickets:
        if(i[0] not in mps):
            mps[i[0]]=[i[1]]
        else:
            mps[i[0]].append(i[1])
    res=[]
    dfs(mps,'JFK',res)
    return(res)

def dfs(mps,word,res):
    while((word in mps) and mps[word]):
        t=sorted(mps[word])[0]
        mps[word].remove(t)
        dfs(mps,t,res)
    res.insert(0,word)
    
            
            
            
            
            
            
            
            
            
            
            
            
            
    