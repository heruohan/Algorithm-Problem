# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 23:19:08 2019

@author: hecongcong
"""

'''
The problem 392:Is Subsequence
Given a string s and string t,check if s is subsequence of t.
you may assume that there is only lower case english letters in both s and t.t is potentially a very long
string,and s is a short string.
A subsequnce of a string is a nre string which is formed from the original string by deleting some(can be none)of
characters without disturbing the relative positions of the remain characters.(ie,'ace' is a subsequnce of 'abcde' 
while 'aec' is not)

Example1:
s = "abc", t = "ahbgdc"
return:True
Example2:
s = "axc", t = "ahbgdc"
return:False.
'''

'''
The answer:本题是给定两个字符串s和t，检查s是否是t的子序列；
解法：
1.可以运用两个指针i,j分别指向s和t,如果当s[i]==t[j]时，则两个指针分别向前移动一位，否则，只把j向前移动一位；
2.判断i是否到达s的最后，如果到达最后，则证明其是t的子序列，返回True.如果跳出循环，则返回False.

代码如下，其中代码2是代码1的简写版，思想都一样.
'''


#代码1
class Solution:
    def isSubsequence(self,s,t):
        i,j=0,0
        len_s=len(s)
        len_t=len(t)
        if(len_s==0):
            return(True)
        while(j<len_t):
            if(s[i]==t[j]):
                i+=1
                j+=1
            else:
                j+=1
            if(i>=len_s):
                return(True)
        return(False)
    

#代码2
class Solution:
    def isSubsequence(self,s,t):
        i,j=0,0
        len_s=len(s)
        len_t=len(t)
        if(len_s==0):
            return(True)
        while(i<len_s and j<len_t):
            if(s[i]==t[j]):
                i+=1
            j+=1
        return(i==len_s)







