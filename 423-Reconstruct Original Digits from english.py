# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:38:21 2019

@author: hecongcong
"""



#解法1
class Solution:
    def originalDigits(self, s):
        mps={}
        tables=['zero','one','two','three','four','five','six','seven','eight','nine']
        res=''
        chs=('z','w','u','x','g','o','h','f','s','i')
        m={'z':'zero','w':'two','u':'four','x':'six','g':'eight',\
             'o':'one','h':'three','f':'five','s':'seven','i':'nine'}
        for i in s:
            if(i not in mps):
                mps[i]=1
            else:
                mps[i]+=1
        for i in chs:
            if(i in mps and mps[i]>0):
                while(mps[i]):
                    for j in m[i]:
                        mps[j]-=1
                    res+=str(tables.index(m[i]))
        return(''.join(sorted(res)))
        
        
                
            
            
            
            
            
            
            