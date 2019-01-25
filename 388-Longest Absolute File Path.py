# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 23:45:22 2019

@author: hecongcong
"""

#解法1
class Solution:
    def lengthLongestPath(self,input):
        res=0
        m={0:0}
        start=0
        level=0
        lens=len(input)
        for i in range(lens+1):
            if(i==lens or input[i]=='\n'):
                tmp=input[start:i]
                if('.' in tmp):
                    res=max(res,m[level]+len(tmp))
                else:
                    m[level+1]=m[level]+len(tmp)+1
                level=0
                start=i+1
            elif(input[i]=='\t'):
                level+=1
                start+=1
        return(res)
        

#解法2
class Solution:
    def lengthLongestPath(self,input):
        res=0
        m={0:0}
        for dirs in input.splitlines():
            name=dirs.lstrip('\t')
            depth=len(dirs)-len(name)
            if('.' in name):
                res=max(res,m[depth]+len(name))
            else:
                m[depth+1]=m[depth]+len(name)+1
        return(res)
        

#解法3
class Solution:
    def lengthLongestPath(self,input):
        lens_sum=0
        res=0
        st=[(-1,0)]
        for dirs in input.splitlines():
            depth=dirs.count('\t')
            name=dirs.lstrip('\t')
            top_depth,top_lens=st[-1]
            while(top_depth>=depth):
                st.pop()
                top_depth,top_lens=st[-1]
            lens=len(name)+(depth>0)
            lens_sum=top_lens+lens
            if('.' in name):
                res=max(res,lens_sum)
            else:
                st.append((depth,lens_sum))
        return(res)
        













           