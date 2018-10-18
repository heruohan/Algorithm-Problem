# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:12:48 2018

@author: hecongcong
"""
'''
The problem:336：Palindrome Pairs
    Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
 so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
 
 Example1:
 Input:["abcd","dcba","lls","s","sssll"]
 Output:[[0,1],[1,0],[3,2],[2,4]] 
 Explanation:The palindrome are ["dcbaabcd","abcddcba","slls","llssssll"]. 
'''

'''
The answer:本题的题意是从给定独一无二的字符串列表中，找出不同的两个元素能组成回文字符串.本题用传统方法求解
效率不高.通过分析假设有s1和s2两个字符串，两者连接构成回文有以下几种情况：
第一：s1和s2互为相反，则s1+s2或s2+s1都可构成回文字符串,比如：s1='abc',s2='cba'.
第二：s1的前i个字符s1[:i]是回文字符串，s1[i:]与s2互为相反，则s2+s1构成回文字符串,其中i小于s1的长度.
第三：s1的后i个字符s1[i:]是回文字符串，s1[:i]与s2互为相反，则s1+s2构成回文字符串，其中i小于s1的长度.

解题步骤：
第一：写一个函数isPalindrome判断word中word[left:right+1]字符串是否为回文字符串.
第二：建立字典tab,其是words中字符串与索引的映射；建立集合lens_set,其为words中每个字符长度的集合(可自动排序)；
然后遍历words列表,分别讨论上述三种情况.
'''
class Solution:    
    def isPalindrome(self,word,left,right):
        while(left<right):
            if(word[left]!=word[right]):
                return(False)
            left+=1
            right-=1
        return(True)
       
    def palindromePairs(self,words):
        res=[]
        tab={}
        lens_set=set()
        for i in range(len(words)):
            tab[words[i]]=i
            lens_set.add(len(words[i]))
        for i in range(len(words)):
            lens=len(words[i])
            word=words[i][::-1]
            if((word in tab) and (tab[word]!=i)): #第一种情况，第二个条件保证不会取到同一个元素.
                res.append([i,tab[word]])
            for j in lens_set:
                if(j<lens): #保证子字符串小于word的长度.
                    if(self.isPalindrome(word,0,lens-j-1) and \
                       (word[lens-j:] in tab)):   #第二种情况
                        res.append([i,tab[word[lens-j:]]])
                    if(self.isPalindrome(word,j,lens-1) and \
                       (word[:j] in tab)):  #第三种情况
                        res.append([tab[word[:j]],i])
                        
        return(res)
    
            
            
            
            
            
            
            
            
            
            
            
            
            
