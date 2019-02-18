# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:41:26 2019

@author: hecongcong
"""



#解法1：递归
class Solution:
    def calcEquation(self,equations,values,queries):
        import collections
        m=collections.defaultdict(dic)
        for (a,b),val in zip(equations,values):
            m[a][b]=val
            m[b][a]=1.0/val
        '''
        以下为列表推导式，且set()每次会重置为空，不用赋值变量直接传递进去
        '''
        return([self.dfs(c,d,m,set()) if((c in m) and (d in m)) \
                else -1.0 for c,d in queries]) 
    
    def dfs(self,x,y,dic,visited):
        if(x==y):
            return(1.0)
        visited.add(x)
        for i in dic[x]:
            if(i in visited):
                continue
            visited.add(i)
            t=self.dfs(i,y,dic,visited)
            if(t!=-1.0):
                return(dic[x][i])
        return(-1.0)
        



#解法2：迭代
class Solution:
    def calcEquation(self,equations,values,queries):
        import collections
        m=collections.defaultdict(list)
        res=[]
        for i in range(len(equations)):
            m[equations[i][0]].append((equations[i][0],1.0))
            m[equations[i][0]].append((equations[i][1],values[i]))
            m[equations[i][1]].append((equations[i][1],1.0))
            m[equations[i][1]].append((equations[i][0],1.0/values[i]))
        for e in queries:
            if((e[0] not in m) or (e[1] not in m)):
                res.append(-1.0)
                continue
            st=[]
            st.append((e[0],1.0))
            visited=set()
            visited.add(e[0])
            found=False
            while(st and not found):
                tmp=st.pop()
                if(tmp[0]==e[1]):
                    res.append(tmp[1])
                    found=True
                    break
                for i in m[tmp[0]]:
                    if(i[0] in visited):
                        continue
                    visited.add(i[0])
                    st.append((i[0],i[1]*tmp[1]))
            if(not found):
                res.append(-1.0)
        return(res)
        







