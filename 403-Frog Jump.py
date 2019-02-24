# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:49:06 2019

@author: hecongcong
"""


'''
The problem 403:Frog Jump
A frog is crossing a river.The river is divided into x units and at each unit there may or may not
exist a stone.the frog can jump on a stone,but it must not jump into the water.
Given a list of stones position(in units) in sorted ascending order,determing if the frog is able to cross
the river by landing on the last stone.initially,the frog is on the first stone and assume the first jump 
must be 1 unit.
if the frog's last jump was k units,then its next jump must be either k-1,k or k+1 units,Note that the frog can 
only jump in the forward direction.

Note:
1.the number of stones is >=2 and is <1100.
2.each stone's position will be a non-negative integer <2**31.
3.the first stone's position is always 0.

Example1:
Input:[0,1,3,5,6,8,12,17]
There are a total of 8 stones.
the first stone at the 0th unit,second stone at the 1st unit,third stone at the 3rd unit,and so on...
the last stone at the 17th unit. 

return:true.The frog can jump to the last stone by jumping 1 unit to the 2nd stone,then 2 units to the 3rd stone,
then 2 units to the 4th stone,then 3 units to the 6th stone,4 units to the 7th stone,and 5 units to the 8th stone.

Example2:
input:[0,1,2,3,4,8,9,11]
return:False;there is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
'''



'''
The answer:本题是给定一个按升序排列的代表石头位置的列表，问青蛙能否跳到最后一个石头过河，假定青蛙一开始是在第一个石头上的，并且第一下只能
跳1单位，其余，如果前一次跳k单位，则后一次可跳k-1,k或者k+1个单位；本题的解题思路可以借鉴动态规划的思想，如下：
解题思路：
1.首先构建一个字典数据结构m，key表示石头的位置，value为对应的能跳到这个石头的所有jump列表；
2.对与stones中任意一个元素的索引i,m[stones[i]]=diff=stones[i]-stones[j],其中j<i,且diff,diff+1,diff-1中任意一个
元素在m[stones[j]]中；
3.循环完毕后，如果字典中stones中的最后一个元素所对应的列表不为空的话，则表明可以可以跳到最后一个石头，则可过河；


解法1：
1.构建一个字典m，循环stones,每次构建一个空列表tmp,然后在循环之前的元素j，计算两者的距离为diff.
2.如果diff,diff-1,diff+1在字典中j所对应的列表中，则表示可以从j跳到当前元素，则将diff加入到tmp中；
3.每次内层循环完毕后，将tmp在字典中赋值给当前元素；
4.外层循环完毕后，如果最后一个元素对应的列表不为空，则表明可以过河，返回True,否则返回false.
这种解法的内循环，每次都要从头开始，效率比较底下；
代码如下；

解法2：是对解法1的进一步优化，是对内部循环可以每个不从头开始，思路类似.
1.首先初始化一个value为list的字典m；字典的Key用stone的索引表示，因为索引和stone的位置对应，都是唯一存在的；
2.同时，在构建一个dp数组，dp[i]表示能跳到相对应的stone上的最大jump.并初始化k=0.
3.进入循环后，首先检查stones[i]与stones[k]的距离是否大于k对应位置上最大的jump+1,即dp[k]+1;如果大于的话，则k向前移动
减少距离；
4.然后循环k到i之间的元素，思路和解法1相似，跟新m和dp;
5.循环完毕后，如果dp的最后一个元素大于0，则返回True;
代码如下；

解法3：递归
1.首先构建一个辅助函数helps(stones,pos,jump,dic).其中pos代表在stones的哪个位置，jump表示在pos位置所具有的弹跳力,dic是一个字典，
此函数的意义是在pos位置拥有jump的弹跳力能否跳到河对岸，输出是bool.
2.如果pos已经大于stones的长度-1，说明已经到了对岸，则返回True；将pos和jump构成一个元素，作为此种条件的唯一标识key;
3.如果key已经在dic种，则直接返回；然后从pos+1开始循环，设两个之间的距离为dist;
4.如果dist小于jump-1，表明dist过小，则跳过继续循环，增大dist;此时下一种情况肯定是dist在jump-1和jump+1之间，则进行递归，如果此时的
pos,jump可以到达对岸，则前一种情况肯定可以到达对岸，将其key加入到dic种，并返回True;
5.如果在jump-1和jump+1之间的这种情况没有进入，则会进入dist>jump+1这种情况，因为stones是递增，则此种情况肯定不能到达对岸，将key放入dic,
并返回False.
6.如果循环完毕后，还没有返回值，则说明dist太小，一直处于dist<jump-1,则必定到不了对岸，放入字典，返回False.
代码如如下；
'''
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
            dist=stones[i]-stones[pos]   #dist必定是正整数
            if(dist<jump-1):
                continue
            elif(dist>jump+1):   #最后一种情况，如果dist在[jump-1,jump+1]这种情况函数未返回值，则进入这种情况，必定不能到达对岸
                dic[key]=False
                return(False)
            if(self.helps(stones,i,dist,dic)): #因为dist必定是正整数，同时dist必定在[jump-1,jump+1]之间，则此时必定能从pos跳到i位置
                dic[key]=True
                return(True)
        dic[key]=False   #始终处于dist<jump-1这种情况，不能到达对岸
        return(False)







