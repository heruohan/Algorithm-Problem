# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:12:42 2019

@author: hecongcong
"""


'''
The problem 419:BattleShips in a Board
Given a 2D Board,count how many battleships are in it.The battleships are represented with 'X's,empty slots are represented with
'.'s.you may assume the following rules:
1.you recieve a valid board,made of only battleships or empty slots.
2.battleships can only be placed horizontally or vertically.in other words,they can only be made of the shape 1XN(1 row,N columns),
or NX1(N rows,1 column),where N can be of any size.
3.at least one horizontal or vertical cell separates between two battleships-there are no adjacent battleships.

Example:
X..X
...X
...X
in the above board,there are 2 battleships.
invalid example:
...X
XXXX
...X
this is an invalid board that you will not receive -as battleships will always have a cell separating between them.

Follow up:
could you do it in one-pass using only O(1) extra memory and without modifying the value of the board?
'''


'''
The answer:本题是给了一个甲板board,叫你统计上面有多少搜战舰，其中战舰满足只能向前水平延申和向下垂直延申，同时，不能有相邻的两个战舰；
本题可用三种方法进行解答，如下：

解法1：深度优先搜索
思路：构建一个二维的记忆数组visited,表示是否访问过相应的元素，然后循环board,当元素为'X'且未被访问，则res加1，然后沿向前水平和向下垂直两个方向
进行搜索，并且将搜索过的'X'在visited里面标记为True,最后返回res；
核心的思想就是如果一个'X'满足要求，就对其进行两个方向的搜索，并将其标记为已读，即将其相连的'X'优先搜索标记，搜索完成后，循环board如果已经标记则
直接跳过，直到下一个满足条件的；
代码如下；

解法2：
思路：如果一个元素为'X'同时，其上方和右边不是'X',则结果加1；因此循环board,返回结果；
代码如下；

解法3：广度优先搜索
思路：思路和深度优先搜索一样，只是用栈代替递归，进行两个方向的迭代，并标记；
代码如下；
'''


#解法1：深度优先搜索
class Solution:
    def countBattleships(self, board):
        h=len(board)
        w=len(board[0])
        res=0
        visited=[[False]*w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if(board[i][j]=='X' and not visited[i][j]):
                    res+=1
                    self.dfs(board,i,j,visited)
        return(res)
    
    def dfs(self,board,x,y,visited):  #visited具有传递性
        height=len(board)
        width=len(board[0])
        dirs=((0,1),(1,0))   #搜索路径
        visited[x][y]=True   #记忆数组
        for dir in dirs:
            m=x+dir[0]
            n=y+dir[1]
            if(m>=0 and m<height and n>=0 and n<width and board[m][n]=='X' and not visited[m][n]):
                self.dfs(board,m,n,visited)



#解法2
class Solution:
    def countBattleships(self, board):
        res=0
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if(board[i][j]=='.' or (i>0 and board[i-1][j]=='X') or (j>0 and board[i][j-1]=='X')):
                    continue
                res+=1
        return(res)                
                
                
                
                
                
#解法3：广度优先搜索
class Solution:
    def countBattleships(self,board):
        res=0
        h=len(board)
        w=len(board[0])
        dirs=((0,1),(1,0))
        visited=[[False]*w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if(board[i][j]=='X' and not visited[i][j]):
                    res+=1
                    st=[(i,j)]
                    while(st):
                        tmp=st.pop()
                        visited[tmp[0]][tmp[1]]=True
                        for d in dirs:
                            x=tmp[0]+d[0]
                            y=tmp[1]+d[1]
                            if(x>=0 and x<h and y>=0 and y<w and \
                               board[x][y]=='X' and not visited[x][y]):
                                st.append((x,y))
        return(res)
        
             
                
