# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:54:27 2019

@author: hecongcong
"""



#解法1:迭代
class Solution:
    def reconstructQueue(self,people):
        import copy
        mps=copy.deepcopy(people)
        ret=[]
        while(people):
            idx=self.helps(people)
            tmp=people[idx]
            ret.append(mps[idx])
            del(people[idx])
            del(mps[idx])
            for p in people:
                if(p[0]<=tmp[0]):
                    p[0]-=tmp[0]
                    p[1]-=1
                else:
                    p[0]-=tmp[0]
        return(ret)
    
    def helps(self,lst):
        import math
        res=0
        h=math.inf
        for i in range(len(lst)):
            if(lst[i][1]==0 and lst[i][0]<=h):
                h=lst[i][0]
                res=i
        return(res)
        


#解法2：递归
class Solution:
    def reconstructQueue(self,people):
        import copy
        mps=copy.deepcopy(people)
        ret=[]
        self.helps(people,mps,ret)
        return(ret)
    
    def helps(self,lst,mps,ret):
        import math
        res=0
        h=math.inf
        if(not lst):
            return
        for i in range(len(lst)):
            if(lst[i][1]==0 and lst[i][0]<=h):
                h=lst[i][0]
                res=i
        ret.append(mps[res])
        tmp=lst[res]
        del(lst[res])
        del(mps[res])
        for p in lst:
            if(p[0]<=tmp[0]):
                p[0]-=tmp[0]
                p[1]-=1
            else:
                p[0]-=tmp[0]
        self.helps(lst,mps,ret)



#解法3：
class Soluiton:
    def reconstructQueue(self,people):
        ret=[]
        people.sort(key=lambda x:(-x[0],x[1]))
        for p in people:
            ret.insert(p[1],p)
        return(ret)
        


#解法4：
class Solution:
    def reconstructQueue(self,people):
        people.sort(key=lambda x:(-x[0],x[1]))
        for i in range(len(people)):
            count=i
            tmp=people[i][1]
            while(count!=tmp):
                people[count],people[count-1]=people[count-1],people[count]
                count-=1
        return(people)
        
#解法5：
class Solution:
    def reconstructQueue(self,people):
        people.sort(key=lambda x:(-x[0],x[1]))
        for i in range(len(people)):
            p=people[i]
            if(p[1]!=i):
                people.pop(i)
                people.insert(p[1],p)
        return(people)
        

