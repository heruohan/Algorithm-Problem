# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 13:33:04 2019

@author: hecongcong
"""


'''
The problem 434:Number of segments in a string
count the number of segments in a string,where a segment is defined to be a contiguous
sequence of non-space characters.
please note that the string does not contain any non-printable characters.
Example:
input:'hello, my name is john'
output:5
'''


'''
The answer:本题是给定一个字符串s,求出其中的段数，段定义为连续的非空字符序列；

解法1：
1.运用字符串的s.split()方法，将一个字符串s,用特定的分隔符进行分开，并返回字符串列表lst；
2.本题种直接用split()默认的分隔符即空格分开，然后lst的长度即为所求；

解法2：
1.首先，将s两端的空字符去掉，然后辅助一个开关变量flag进行统计；

解法3：
1.遇到空格直接跳过进入下一轮循环，否则结果加1，并将索引移动到一个segment的末尾；

解法4：
1.因为一个segment的第一位字符前一位必定是空格或者在开头；所以根据这个性质进行统计；

代码如下；
'''
#解法1:
class Solution:
    def countSegments(self,s):
        lst=s.split()
        return(len(lst))



#解法2：
class Solution:
    def countSegment(self,s):
        s_diff=s.strip()
        res=0
        flag=False
        for i in s_diff:
            if(not flag and i==' '):
                res+=1
                flag=True
            elif(flag and i!=' '):
                flag=False
        return(res+1 if(s_diff) else res)



#解法3：
class Solution:
    def countSegment(self,s):
        res=0
        lens=len(s)
        i=0
        while(i<lens):
            if(s[i]==' '):
                i+=1
                continue
            res+=1
            while(i<lens and s[i]!=' '):
                i+=1
        return(res)
        



#解法4:
class Solution:
    def countSegment(self,s):
        res=0
        lens=len(s)
        for i in range(lens):
            if(s[i]!=' ' and (i==0 or s[i-1]==' ')):
                res+=1
        return(res)
        





