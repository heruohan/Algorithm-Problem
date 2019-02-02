# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:07:47 2019

@author: hecongcong
"""


#解法1
class Solution:
    def isrectangleCover(self,rectangles):
        import math
        erea_sum=0
        count=0
        m={}
        a1=math.inf
        a2=math.inf
        a3=-math.inf
        a4=-math.inf
        for rect in rectangles:
            a1=min(a1,rect[0])
            a2=min(a2,rect[1])
            a3=max(a3,rect[2])
            a4=max(a4,rect[3])
            erea_sum+=(rect[2]-rect[0])*(rect[3]-rect[1])
            if(not self.isValid(m,(rect[0],rect[1]),1)):
                return(False)
            if(not self.isValid(m,(rect[2],rect[3]),4)):
                return(False)
            if(not self.isValid(m,(rect[0],rect[3]),2)):
                return(False)
            if(not self.isValid(m,(rect[2],rect[1]),8)):
                return(False)
        for item in m:
            t=m[item]
            if(t==1 or t==2 or t==4 or t==8):
                count+=1
        return(count==4 and area_sum==(a3-a1)*(a4-a2))
        
    def isValid(self,dic,m1,m2):
        if(m1 not in dic):
            dic[m1]=m2
        else:
            tmp=dic[m1]
            if(tmp==m2):
                return(False)
            else:
                dic[m1]+=m2
        return(True)
        
    
    
#解法2
class Solution:
    def isrectangleCover(self,rectangles):
        import math
        st=set()
        area_sum=0
        a1=math.inf
        a2=math.inf
        a3=-math.inf
        a4=-math.inf
        for rect in rectangles:
            a1=min(a1,rect[0])
            a2=min(a2,rect[1])
            a3=max(a3,rect[2])
            a4=max(a4,rect[3])
            area_sum+=(rect[2]-rect[0])*(rect[3]-rect[1])
            if((rect[0],rect[1]) in st):
                st.remove((rect[0],rect[1]))
            else:
                st.add((rect[0],rect[1]))
            if((rect[2],rect[3]) in st):
                st.remove((rect[2],rect[3]))
            else:
                st.add((rect[2],rect[3]))
            if((rect[0],rect[3]) in st):
                st.remove((rect[0],rect[3]))
            else:
                st.add((rect[0],rect[3]))
            if((rect[2],rect[1]) in st):
                st.remove((rect[2],rect[1]))
            else:
                st.add((rect[2],rect[1]))
        s1=(a1,a2)
        s2=(a3,a4)
        s3=(a1,a4)
        s4=(a3,a2)
        if(s1 not in st or s2 not in st or s3 not in st or \
           s4 not in st or len(st)!=4):
            return(False)
        return(area_sum==(a3-a1)*(a4-a2))
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    