# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:54:24 2019

@author: hecongcong
"""



#解法1：
class Solution:
    def pacificAtlantic(self,matrix):
        import math
        h=len(matrix)
        if(h==0):
            return([])
        w=len(matrix[0])
        p_v=[[False]*w for _ in range(h)]
        a_v=[[False]*w for _ in range(h)]
        res=[]
        for i in range(h):
            self.dfs(matrix,p_v,-math.inf,i,0)
            self.dfs(matrix,a_v,-math.inf,i,w-1)
        for j in range(w):
            self.dfs(matrix,p_v,-math.inf,0,j)
            self.dfs(matrix,a_v,-math.inf,h-1,j)
        for i in range(h):
            for j in range(w):
                if(p_v[i][j] and a_v[i][j]):
                    res.append([i,j])
        return(res)

    
    def dfs(self,matrix,visited,pre,x,y):
        dirs=((0,1),(0,-1),(1,0),(-1,0))
        m=len(matrix)
        n=len(matrix[0])
        if(x>=0 and x<m and y>=0 and y<n and not visited[x][y] and \
           matrix[x][y]>=pre):
            visited[x][y]=True
            for d in dirs:
                self.dfs(matrix,visited,matrix[x][y],x+d[0],y+d[1])
                
        



#解法2：
class Solution:
    def pacificAtlantic(self,matrix):
        h=len(matrix)
        if(h==0):
            return([])
        w=len(matrix[0])
        a_v=[[False]*w for _ in range(h)]
        p_v=[[False]*w for _ in range(h)]
        a=[]
        p=[]
        res=[]
        for i in range(h):
            a.append((i,w-1))
            p.append((i,0))
        for j in range(w):
            a.append((h-1,j))
            p.append((0,j))
        self.bfs(matrix,p_v,p)
        self.bfs(matrix,a_v,a)
        for i in range(h):
            for j in range(w):
                if(p_v[i][j] and a_v[i][j]):
                    res.append([i,j])
        return(res)

    
    def bfs(self,matrix,visited,queue):
        dirs=((0,1),(0,-1),(1,0),(-1,0))
        m=len(matrix)
        n=len(matrix[0])
        while(queue):
            tmp=queue.pop()
            visited[tmp[0]][tmp[1]]=True
            for d in dirs:
                x=tmp[0]+d[0]
                y=tmp[1]+d[1]
                if(x>=0 and x<m and y>=0 and y<n and not visited[x][y] and \
                   matrix[x][y]>=matrix[tmp[0]][tmp[1]]):
                    queue.append((x,y))






        
        
        
        
        
        