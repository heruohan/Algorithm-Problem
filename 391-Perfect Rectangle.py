# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:07:47 2019

@author: hecongcong
"""

'''
The problem 391:Perfect Rectangle
Given N axis-aligned rectangles where N>0,determine if they all togeter form an exact cover of a
rectangular region.
Each rectangle is represented as a bottom-left point and a top-right point.For example,a unit square
is represented as [1,1,2,2].(coordinate of bottom-left point is (1,1) and top-right point is (2,2)).

Example1:
rectangles= [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
return True.all 5 rectangles together form an exact cover of a rectangular region.

Example2:
rectangles= [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]
return False.because there is a gap between the two rectangular regions.

Example3:
rectangles= [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]
return false.because there is a gap in the top center.

Example4:
rectangles=[
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]
return false.because two of the rectangles overlap with each other.
'''


'''
The answer:本题时给定N个矩形，看能不能组成一个严格覆盖的矩形区域，其中每个小矩形都是由左下角的点和右上角的点唯一定义.
本题不能用传统方法解答，首先想到的条件是所有小矩形面积加起来等不等于大矩形的面积，其次，在所有矩形中，顶点只有三种情况，
只有一个矩形构成的情况A，只有两个矩形构成的情况B，只有四个矩形构成的情况C，进而在分析：
1.一个矩形的顶点不能和另一个矩形的顶点相同，否则这两个矩形的就有重合的部分，则可直接返回False.
2.在最后的完美矩形中A情况的顶点只有四个,且各一个.
因此，为解决上述问题，可标记一个矩形的四个顶点，左下为1，左上为2，右上为4，右下为8，因此在最终的完美矩形中只有四个A中情况，即
1，2，4，8；B中情况是由两个矩形构成即有12，10，9，6，5，3六种情况，C中情况是由四个矩形构成既有15一种情况；


解法1：
1.我们构建一个字典m，和一个辅助函数isValid,辅助函数是如果一个顶点不再字典中的话，将顶点和相应的标记做映射，如果顶点在字典中的话
判断顶点的映射和传入的标记是否相等，如果相等则直接返回False.否则，就值相加；最后返回True.
2.循环完矩阵列表后，对字典中值为1,2,4,8的个数做统计count.
3.最后判断count是否为4，以及所有矩形的面积是否等于大矩阵的面积;
代码技巧：
1.因为字典m为复杂数据结构，所以其传入辅助函数isValid后，因为只是内部的数据变化，所以其id一直会保持不变，具有记忆性;


解法2：
1.首先构建一个集合st,因为矩阵中的顶点只有A,B,C三种情况，且B,C是由偶数个矩阵构成的，只有A是由奇数个矩阵构成，所以当一个点没在st
中时，将其加入；如果在st中，则将其删除；因此最后集合st中只剩下A中情况的顶点；
2.最后判断最终的大矩阵的四个顶点是否在集合st中，同时st中元素的个数要为4，否则返回False.
3.最后判断个矩阵面积和是否等于大矩阵的面积；
'''


#解法1
class Solution:
    def isrectangleCover(self,rectangles):
        import math
        erea_sum=0
        count=0
        m={}
        a1=math.inf
        a2=math.inf
        a3=-math.inf
        a4=-math.inf
        for rect in rectangles:
            a1=min(a1,rect[0])
            a2=min(a2,rect[1])
            a3=max(a3,rect[2])
            a4=max(a4,rect[3])
            erea_sum+=(rect[2]-rect[0])*(rect[3]-rect[1])
            if(not self.isValid(m,(rect[0],rect[1]),1)):
                return(False)
            if(not self.isValid(m,(rect[2],rect[3]),4)):
                return(False)
            if(not self.isValid(m,(rect[0],rect[3]),2)):
                return(False)
            if(not self.isValid(m,(rect[2],rect[1]),8)):
                return(False)
        for item in m:
            t=m[item]
            if(t==1 or t==2 or t==4 or t==8):
                count+=1
        return(count==4 and area_sum==(a3-a1)*(a4-a2))
        
    def isValid(self,dic,m1,m2):
        if(m1 not in dic):
            dic[m1]=m2
        else:
            tmp=dic[m1]
            if(tmp==m2):
                return(False)
            else:
                dic[m1]+=m2
        return(True)
        
    
    
#解法2
class Solution:
    def isrectangleCover(self,rectangles):
        import math
        st=set()
        area_sum=0
        a1=math.inf
        a2=math.inf
        a3=-math.inf
        a4=-math.inf
        for rect in rectangles:
            a1=min(a1,rect[0])
            a2=min(a2,rect[1])
            a3=max(a3,rect[2])
            a4=max(a4,rect[3])
            area_sum+=(rect[2]-rect[0])*(rect[3]-rect[1])
            if((rect[0],rect[1]) in st):
                st.remove((rect[0],rect[1]))
            else:
                st.add((rect[0],rect[1]))
            if((rect[2],rect[3]) in st):
                st.remove((rect[2],rect[3]))
            else:
                st.add((rect[2],rect[3]))
            if((rect[0],rect[3]) in st):
                st.remove((rect[0],rect[3]))
            else:
                st.add((rect[0],rect[3]))
            if((rect[2],rect[1]) in st):
                st.remove((rect[2],rect[1]))
            else:
                st.add((rect[2],rect[1]))
        s1=(a1,a2)
        s2=(a3,a4)
        s3=(a1,a4)
        s4=(a3,a2)
        if(s1 not in st or s2 not in st or s3 not in st or \
           s4 not in st or len(st)!=4):
            return(False)
        return(area_sum==(a3-a1)*(a4-a2))
        
        
    
    
    
    
    
    
    
        
