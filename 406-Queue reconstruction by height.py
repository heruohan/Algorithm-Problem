# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:54:27 2019

@author: hecongcong
"""


'''
The problem 406:Queue reconstruction by height
suppose you have a random list of people standing in a queue.Each person is described by a pair of integers (h,k) where h is the
height of the person and k is the number of people in front of this person who have a height greater than or equal to h.
write an algorithm to reconstruct the queue.
Note:
the number of people is less than 1100.

Example:
input:[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
output:[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''


'''
The answer:本题是随机给定人站队队列，每个人都由一对数字(h,k)描述，其中h表示人的身高，k表示前面有多少人的身高大于等于这个人的身高；
叫写一个算法重新按条件对队列进行排序；本题有好几种不同的做法，如下：

解法1：迭代
思路：对于一个随机排序的people数组，其按条件排列后的一个元素肯定是k=0且h在k=0里面h最小的一个元素；找到这个元素tmp后,将其在people数组中
删除，同时，循环people各元素p,如果p第一个元素小于等于tmp的h的话，则p的第一个元素减tmp的第一个元素，且p的k在自减1.否则，只需要更新P的第一个元素；
然后重复以上过程；
代码技巧：
1.需要深拷贝一个mps，因为不能随people的更新而更新mps.
代码如下；

解法2：思路如解法1；


解法3：
思路：首先对people进行排序，首先按h从大到小排序，在h相等时按照k从小到大；比如：people=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]].
排序后：[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]；依次循环排序后的元素，比如循环到索引为i的元素，此时表示其前面有i个人的身高都大于等于
它，如果此时i元素的k不等于i,则将其插入到结果数组中i元素的k位置即可；循环完毕后，即为排序后的数组；

解法3,4,5的思路都类似，只是看是不是在使用额外的空间；
代码分别如下;
'''
#解法1:迭代
class Solution:
    def reconstructQueue(self,people):
        import copy
        mps=copy.deepcopy(people)  #深拷贝一个mps，使得其与people隔断联系，这样才能对应的取出原始数组
        ret=[]
        while(people):
            idx=self.helps(people)
            tmp=people[idx]
            ret.append(mps[idx])
            del(people[idx])
            del(mps[idx])
            for p in people:
                if(p[0]<=tmp[0]):
                    p[0]-=tmp[0]
                    p[1]-=1
                else:
                    p[0]-=tmp[0]
        return(ret)
    
    def helps(self,lst):  #此函数为取出lst数组中，k==0且h最小的元素的索引
        import math
        res=0
        h=math.inf
        for i in range(len(lst)):
            if(lst[i][1]==0 and lst[i][0]<=h):
                h=lst[i][0]
                res=i
        return(res)
        


#解法2：递归
class Solution:
    def reconstructQueue(self,people):
        import copy
        mps=copy.deepcopy(people)
        ret=[]
        self.helps(people,mps,ret)
        return(ret)
    
    def helps(self,lst,mps,ret):
        import math
        res=0
        h=math.inf
        if(not lst):
            return
        for i in range(len(lst)):
            if(lst[i][1]==0 and lst[i][0]<=h):
                h=lst[i][0]
                res=i
        ret.append(mps[res]) #ret不是赋值，因此ret在递归过程中的id始终不会变，因此其具有传递性
        tmp=lst[res]
        del(lst[res])
        del(mps[res])
        for p in lst:
            if(p[0]<=tmp[0]):
                p[0]-=tmp[0]
                p[1]-=1
            else:
                p[0]-=tmp[0]
        self.helps(lst,mps,ret)



#解法3：
class Soluiton:
    def reconstructQueue(self,people):
        ret=[]
        people.sort(key=lambda x:(-x[0],x[1]))
        for p in people:
            ret.insert(p[1],p)
        return(ret)
        


#解法4：
class Solution:
    def reconstructQueue(self,people):
        people.sort(key=lambda x:(-x[0],x[1]))
        for i in range(len(people)):
            count=i
            tmp=people[i][1]
            while(count!=tmp):
                people[count],people[count-1]=people[count-1],people[count]
                count-=1
        return(people)
        
#解法5：
class Solution:
    def reconstructQueue(self,people):
        people.sort(key=lambda x:(-x[0],x[1]))
        for i in range(len(people)):
            p=people[i]
            if(p[1]!=i):
                people.pop(i)
                people.insert(p[1],p)
        return(people)
        

