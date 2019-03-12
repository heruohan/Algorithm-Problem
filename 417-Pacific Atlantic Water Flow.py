# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:54:24 2019

@author: hecongcong
"""


'''
The problem 417:Pacific Atlantic Water Flow
Given an mXn matrix of non-negative integers reprepsenting the height of each unit cell in a continent,the 'Pacific Ocean' touches the
left and top edges of the matrix and the 'Atlantic Ocean' touches the right and bottom edges.
Water can only flow in four directions(right,left,bottom,top)from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
Note:
1.the order of returned grid coordinates does not matter.
2.both m and n are less than 150.
Example:
Given the following 5x5 matrix:
Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic
return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]](positions with parentheses in above matrix).
'''



'''
The answer:本题给一个mxn的非负矩阵matrix代表陆地上的单元格的高度，其中太平洋连接着matrix的左边和上面，大西洋挨着右边和下面，水可以流向四个
方向，并且只能向相等或者更低的地方流动；找出所有同时能流到两个洋的点的坐标的列表；
本题可以用经典的深度优先搜索和广度优先搜索进行解答，如果一个点能流到pacific或者atlantic中，则其肯定能搜索到其相应的两条边上，所以我们可以从边上
进行搜索，如果可以搜索到一个地方，则这个地方必然会流到相应的洋里；

解法1：深度优先搜索
核心思路：可以分别构建两个二维数组p_v和a_v，v[i][j]表示其是否搜索到了这个位置，如果p_v[i][j]为True,则(i,j)这个位置必然可以流到pacific中，如果
a_v[i][j]为True，则(i,j)这个位置必然可以流到atlantic中，如果同时为True，则这个点满足题意；
1.首先构建辅助函数dfs,其从四个方面搜索，并且标记满足条件既能搜索到的位置为True.
2.在主函数中分别从两条边上对pacific和atlantic进行搜索，最后循环如果p_v和a_v中某个位置同时为True,则将其放入结果；
代码如下；


解法2：广度优先搜索
核心思路：思路基本和深度优先搜索一样，只是用栈结构queue辅助搜索；
代码如下；
'''


#解法1：深度优先搜索
class Solution:
    def pacificAtlantic(self,matrix):
        import math
        h=len(matrix)
        if(h==0):
            return([])
        w=len(matrix[0])
        p_v=[[False]*w for _ in range(h)]   #分别构建访问数组
        a_v=[[False]*w for _ in range(h)]
        res=[]
        for i in range(h):   #从左边和右边两条边上分别进行搜索
            self.dfs(matrix,p_v,-math.inf,i,0)
            self.dfs(matrix,a_v,-math.inf,i,w-1)
        for j in range(w):   #从上面和下面两条边上分别进行搜索
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
           matrix[x][y]>=pre):   #未被访问且高度要大于等于前面一个，因为为反方向搜索
            visited[x][y]=True
            for d in dirs:
                self.dfs(matrix,visited,matrix[x][y],x+d[0],y+d[1])
                
        



#解法2：广度优先搜索
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
        for i in range(h):  #将左右边上的点分别加入到pacific和atlantic对应的栈结构中
            a.append((i,w-1))
            p.append((i,0))
        for j in range(w):  #将上下边上的点分别加入到对应的栈结果中
            a.append((h-1,j))
            p.append((0,j))
        self.bfs(matrix,p_v,p) #分别进行广度优先搜索
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






        
        
        
        
        
        
