# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:48:47 2019

@author: hecongcong
"""


#解法1
class Solution:
    def deserialize(self,s):
        if(len(s)==0):
            return(NestedInteger())
        if(s[0]!='['):
            return(NestedInteger(int(s)))
        st=[]
        start=1
        for i in range(len(s)):
            if(s[i]=='['):
                st.append(NestedInteger())
                start=i+1
            elif(s[i]==',' or s[i]==']'):
                if(i>start):
                    st[-1].add(NestedInteger(int(s[start:i])))
                start=i+1
                if(s[i]==']'):
                    if(len(st)>1):
                        tmp=st.pop()
                        st[-1].add(tmp)
        return(st[-1])
        
        
#解法2
class Solution:
    def deserialize(self,s):
        if(len(s)==0):
            return(NestedInteger())
        if(s[0]!='['):
            return(NestedInteger(int(s)))
        if(len(s)<=2):
            return(NestedInteger())
        res=NestedIneger()
        start=1
        tmp=0
        for i in range(1,len(s)):
            if(tmp==0 and (s[i]==',' or i==len(s)-1)):
                res.add(self.deserialize(s[start:i]))
                start=i+1
            elif(s[i]=='['):
                tmp+=1
            elif(s[i]=']'):
                tmp-=1
        return(res)
        
        
        
        
        
        
        
                    
                
                