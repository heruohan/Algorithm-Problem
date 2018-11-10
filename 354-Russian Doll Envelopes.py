# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 13:05:54 2018

@author: hecongcong
"""

def maxEnvelopes(envelopes):
    sort_envelopes=sorted(envelopes,key=lambda x:(x[0],-x[1]))
    res=[]
    for i in sort_envelopes:
        left=0
        right=len(res)
        num=i[1]
        while(left<right):
            mid=left+(right-left)//2
            if(res[mid]<num):
                left=mid+1
            else:
                right=mid
        
        if(right>=len(res)):
            res.append(num)
        else:
            res[right]=num
    return(len(res))
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        