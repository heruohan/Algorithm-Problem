# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 00:00:52 2019

@author: hecongcong
"""



#解法1
class Solution:
    def readBinaryWatch(self,num):
        res=[]
        for h in range(12):
            for m in range(60):
                if(bin(h).count('1')+bin(m).count('1')==num):
                    if(m>=10):
                        res.append(str(h)+':'+str(m))
                    else:
                        res.append(str(h)+':'+'0'+str(m))
        return(res)




#解法2
class Solution:
    def readBinaryWatch(self,num):
        hour=[1,2,4,8]
        minutes=[1,2,4,8,16,32]
        res=[]
        for h in range(num+1):
            h_res=self.generate(hour,h)
            m_res=self.generate(minutes,num-h)
            for i in h_res:
                if(0<=i<=11):
                    for j in m_res:
                        if(0<=j<=9):
                            res.append(str(i)+':'+'0'+str(j))
                        elif(10<=j<=59):
                            res.append(str(i)+':'+str(j))
        return(res)
    
    def generate(self,lst,count):
        res=[]
        self.helpFn(lst,count,0,0,res)
        return(res)
    
    def helpFn(self,lst,count,start,val,res):
        if(count==0):
            res.append(val)
            return
        for i in range(start,len(lst)):
            self.helpFn(lst,count,i+1,val+lst[i],res)
            










