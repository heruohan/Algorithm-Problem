# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 00:32:05 2019

@author: hecongcong
"""



#解法1
class Solution:
    def trapRainWater(heightmap):
        import queue
        import math
        m=len(heightmap)
        if(m==0):
            return(0)
        n=len(heightmap[0])
        q=queue.PriorityQueue()
        visited=[[False]*n for _ in range(m)]
        dirs=[(0,-1),(0,1),(-1,0),(1,0)]
        mx=-math.inf
        res=0
        for i in range(m):
            for j in range(n):
                if(i==0 or i==m-1 or j==0 or j==n-1):
                    q.put((heightmap[i][j],i*n+j))
                    visited[i][j]=True
        while(not q.empty()):
            tmp=q.get()
            height=tmp[0]
            row=tmp[1]//n
            col=tmp[1] % n
            mx=max(height,mx)
            for d in dirs:
                x=row+d[0]
                y=col+d[1]
                if(x>=0 and x<m and y>=0 and y<n and \
                   not visited[x][y]):
                    if(heightmap[x][y]<mx):
                        res+=(mx-heightmap[x][y])
                    visited[x][y]=True
                    q.put((heightmap[x][y],x*n+y))
        return(res)
        
        
                
    

