# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 00:32:05 2019

@author: hecongcong
"""


'''
The problem 407:Trapping Rain Water II
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.
Note:
Both m and n are less than 110.the height of each unit cell is greater than 0 and is less than 2000.

Example:
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
return:4.
'''


'''
The answer:本题是给定一个mxn的正整数矩阵，代表每个单元格的高度，计算下雨后这个东西能收集到多少体积的雨水；
解答本题需遵循以下原理：短板理论：一个容器能装的水多少，和其最短的地方相关；
对于此题，边缘的地方肯定不能装水，所以此题我们运用BFS(广度优先搜索)从其边缘不断向四周寻找，相互连同，且能装水的地方；
我们每次取出其最小的高度，因此用优先队列来存储；同时，我们用mx来表示从最小的高度开始上升计算，如果优先队列中元素的高度比其
小，则表示可以存储水，如果联通的单元格高度还是比mx小，则依然可以以mx来计算存水量，同时因为mx是从小往大升的，所以其可以表示找到能
存储水的单元格的最短的边；

解法1：
1.构建一个优先队列q，和二维存储结构visited，表示是否访问过某个元素；以及一个dirs路径列表，表示在某个元素上下左右进行搜索；设定最小高度mx.
2.循环heightMap,把边界放入q中，visited中对应的元素变为True;
3.然后循环有限列表q，每次取出最小的元素，表示出其高度，在heightMap中的行列；更新mx.
4.然后在其四周遍历联通的格子，计算新坐标，如果在heightMap内部及未被访问过，visited变为True,放入q中，同时如果其高度小于mx，则表示可以存储水，加入
到res中；
5.循环结束后，返回结果;
代码如下；
'''
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
        dirs=[(0,-1),(0,1),(-1,0),(1,0)]  #搜索路径，上下左右
        mx=-math.inf
        res=0
        for i in range(m):
            for j in range(n):
                if(i==0 or i==m-1 or j==0 or j==n-1):
                    '''
                    优先列表里虽然是一个元组，但是其取最小元素是，是以元组中第一个元素作为依据
                    '''
                    q.put((heightmap[i][j],i*n+j))  #有限队列中存储的是元组，第一个元素表示高度，第二个元素将其行列的信息转化在一个数上 
                    visited[i][j]=True
        while(not q.empty()):
            tmp=q.get()  #返回最小元素
            height=tmp[0]   #高度
            row=tmp[1]//n  #转化为行
            col=tmp[1] % n  #转化为列
            mx=max(height,mx) #如果h比mx大，则更新，如h比mx小，表示可以存水，最短边mx不变
            for d in dirs:
                x=row+d[0]
                y=col+d[1]
                if(x>=0 and x<m and y>=0 and y<n and \
                   not visited[x][y]):
                    if(heightmap[x][y]<mx):  #tmp的联通格子可以存水
                        res+=(mx-heightmap[x][y])
                    visited[x][y]=True
                    q.put((heightmap[x][y],x*n+y))
        return(res)
        
        
                
    

