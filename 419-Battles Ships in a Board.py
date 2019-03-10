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
2.
'''
#解法1
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
    
    def dfs(self,board,x,y,visited):
        height=len(board)
        width=len(board[0])
        dirs=((0,1),(1,0))
        visited[x][y]=True
        for dir in dirs:
            m=x+dir[0]
            n=y+dir[1]
            if(m>=0 and m<height and n>=0 and n<width and board[m][n]=='X' and not visited[m][n]):
                self.dfs(board,m,n,visited)



#解法2
class Solution1:
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
                
                
                
                
                
                
                
