# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:41:26 2019

@author: hecongcong
"""

'''
The problem 399:Evaluate Division
Equations are given in the format A/B=k,where A and B are variables represented as string,and k is 
a real number(floating point number).Given some queries,return the answers.if the answer does not exist,
return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are:a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return:[6.0, 0.5, -1.0, 1.0, -1.0 ].
The input is:vector<pair<string, string>> equations,vector<double>&values,vector<pair<string, string>> queries,
where equations.size() == values.size(),and the values are positive,this represents the equations,return vector<double>.

according to the example above:
equations=[ ["a", "b"], ["b", "c"] ],
values=[2.0, 3.0],
queries=[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
the input is always valid,you may assume that evaluating the queries will result in no division by zero and there is no
contradiction.
'''



'''
The answer:本题是给定一个以列表表示的字符串方程equations,和其对应的值values,以及需要计算的列表queries,求出其相对应的值，如果求不
出来则返回-1.0.本题实际上是一道很简单的转换出发运算，但是由程序表示出来就有一定难度；

核心思路：本题可以抽象成一道有向图的题，而values中的值分别表示其对应的权重，比如'a'到'b'，'b'到'c'可以连接为一个有向图，'a'到'b'的权重为
2.0，'a'到'a'的权重为'1.0','b'到'a'的权重则为1/2.0;因此可以用深度优先搜索和广度优先搜索进行解答.


解法1：深度优先搜索
1.构建一个嵌套字典m,其key为图中的每个元素，values为其直接指向的下一个元素，以及这两个元素所连接的权重；
2.构建一个辅助函数dfs(x,y,dic,visited),其中x,y分别表示queries,dic为构建的嵌套字典，visited为一个集合，
如果访问了图中的某个元素就将其放进去，防止在图中寻找的时候走回头路，其每次都要重置为空集合；这个函数的返回值
是x/y的结果；
3.dfs递归退出条件为x==y,然后遍历x在图中所直接连接的节点，如果访问过则直接跳过，否则将节点加进去，然后递归求解
其直接连接的节点i/y的值t；
4.然后返回x/y的值，即x直接连接的节点i所对应的权重乘以t.如果变量完成没有找到的话，则返回-1.0.
5.在主函数里面使用列表推导式遍历queries.
代码如下.
代码技巧：
1.visited每次重新计算一个新的方程式时都要重置为空集合；
2.visited集合在dfs函数递归过程中，具有传递性；



解法2：广度优先搜索
1.首先构建一个临接列表字典m，其key为图中的每个元素，values为其直接指向的下一个元素及其权重的元组列表；
2.循环queries列表元素e，当e中有一个元素不在m中时，便将-1.0放入结果res中，直接进行下一循环；否则，构建一个栈st,
将第一个元素和其权重1.0的元组放入，初始化一个visited集合，然后一个开关变量found;
3.当st不为空，以及没有找到结果时，弹出栈顶元素tmp,如果tmp的第一个元素与e的第二个元素相等，则说明已经找到结果，放入res中
并变换开关，直接跳出循环；否则遍历当前节点tmp[0]直接连接的所有节点，并将下一个节点i以及e[0]到i的累积乘积元组放入st中，直到
退出循环，然后判断found，如果没有找到的话，则将-1.0放入res中；
4.循环结束,返回res;
'''

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
    
    def dfs(self,x,y,dic,visited):   #visited具有传递性
        if(x==y):
            return(1.0)
        visited.add(x)
        for i in dic[x]:
            if(i in visited):
                continue
            visited.add(i)
            t=self.dfs(i,y,dic,visited)
            if(t!=-1.0):
                return(dic[x][i]*t)
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
            st=[]   #每次重置
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
        







