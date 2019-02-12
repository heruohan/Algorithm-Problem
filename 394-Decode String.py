# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:06:11 2019

@author: hecongcong
"""




#解法1:迭代+栈
class Solution:
    def decodeString(self,s):
        ret=''
        st=[]
        for i in s:
            if(i==']'):
                tmp=st.pop()
                res=tmp
                while(tmp!='['):
                    tmp=st.pop()
                    if(tmp!='['):
                        res=tmp+res
                num=''
                while(st and ('0'<=st[-1]<='9')):
                    num=st.pop()+num
                res=res*int(num)
                st.append(res)
            else:
                st.append(i)
        for j in st:
            ret+=j
        return(ret)
        
                
    
#解法2:递归(重点，难点)
class Solution:
    def decodeString(self,s):
        lst=[0]
        return(self.helps(s,lst))
        
    def helps(self,s,lst):
        res=''
        lens=len(s)
        while(lst[0]<lens and s[lst[0]]!=']'):
            if(s[lst[0]]<'0' or s[lst[0]]>'9'):
                res+=s[lst[0]]
                lst[0]+=1
            else:
                count=0
                while(s[lst[0]]>='0' and s[lst[0]]<='9'):
                    count=10*count+int(s[lst[0]])
                    lst[0]+=1
                lst[0]+=1
                t=self.helps(s,lst)
                lst[0]+=1
                res=res+t*count
        return(res)
        












