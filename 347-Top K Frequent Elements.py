# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 09:50:15 2018

@author: hecongcong
"""

def topKFrequent(nums,k):
    import operator
    tabs={}
    res=[]
    for i in nums:
        if(i not in tabs):
            tabs[i]=1
        else:
            tabs[i]+=1
    ordered_lst=sorted(tabs.items(),key=operator.itemgetter(1),\
                       reverse=True)
    for i in range(k):
        res.append(ordered_lst[i][0])
    return(res)
    
    
    
    
    
    
    
    
    
    
    
    
    
    