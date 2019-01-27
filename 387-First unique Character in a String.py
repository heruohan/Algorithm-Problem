# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:49:31 2019

@author: hecongcong
"""

'''
The problem 387:First unique character in a string
Given a string,find the first non-repeating character in it and return its index.if it does not exist,return -1.

Example:
s = "leetcode"
return:0

s = "loveleetcode",
return:2
'''


'''
The answer:本题是给定一个字符串s，在它里面找出第一个不重复的字符，并且返回它的索引，如果
不存在就返回-1.本题用两种解法.

解法1：
1.首先构建一个集合sts,循环字符串s，如果其中的字符元素不在sts和字符串后面中，则满足条件，返回相应
的索引.
2.否则，更进一步，如果字符串不再集合中，则将其添加到sts中.
3.循环完毕，还未找到，则返回-1.

解法2：
1.构建一个字典dic，循环s,统计其中的各个元素出现的个数，并作映射.
2.然后在依次循环s，如果在字典中相应元素的值位1，则满足条件，返回索引，如
循环完毕还未找到则返回-1.
'''
#解法1
class Solution:
    def firstUniqChar(self,s):
        sts=set()
        lens=len(s)
        for i in range(lens):
            if(s[i] not in sts and s[i] not in s[i+1:]):
                return(i)
            else:
                if(s[i] not in sts):
                    sts.add(s[i])
        return(-1)
        
            

#解法2
class Solution:
    def firstUniqChar(self,s):
        dic={}
        for i in s:
            if(i not in dic):
                dic[i]=1
            else:
                dic[i]+=1
        for i in range(len(s)):
            if(dic[s[i]]==1):
                return(i)
        return(-1)
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
