# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:49:06 2019

@author: hecongcong
"""



#解法1
class Solution:
    def canCross(self,stones):
        lens=len(stones)
        if(stones[1]!=1):
            return(False)
        m={1:[1]}
        for i in range(2,lens):
            tmp=[]
            for j in m:
                if(stones[i]-j in m[j] or stones[i]-j-1 in m[j] \
                   stones[i]-j+1 in m[j]):
                    tmp.append(stones[i]-j)
            m[stones[i]]=tmp
        return(True if(m[stones[-1]]) else False)




#解法2:(改进)
class Solution:
    def canCross(self,stones):
        import collections
        m=collections.defaultdict(list)
        m[0].append(0)
        lens=len(stones)
        dp=[0]*lens
        k=0
        for i in range(1,lens):
            while(stones[i]-stones[k]>dp[k]+1):
                k+=1
            for j in range(k,i):
                tmp=stones[i]-stones[j]
                if(tmp in m[j] or tmp+1 in m[j] or tmp-1 in m[j]):
                    m[i].append(tmp)
                    dp[i]=max(dp[i],tmp)
        return(dp[-1]>0)
        
        

#解法3:递归
class Solution:
    def canCross(self,stones):
        return(self.helps(stones,0,0,{}))
    
    def helps(self,stones,pos,jump,dic):
        lens=len(stones)
        if(pos>=lens-1):
            return(True)
        key=(pos,jump)
        if(key in dic):
            return(dic[key])
        for i in range(pos+1,lens):
            dist=stones[i]-stones[pos]
            if(dist<jump-1):
                continue
            elif(dist>jump+1):
                dic[key]=False
                return(False)
            if(self.helps(stones,i,dist,dic)):
                dic[key]=True
                return(True)
        dic[key]=False
        return(False)







