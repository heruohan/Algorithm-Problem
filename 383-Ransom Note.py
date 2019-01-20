# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:25:52 2019

@author: hecongcong
"""

'''
The problem 383:Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the
magazines,write a function that will return true if the ransom note can be construted from
the magazines;otherwise,it will return false.
Each letter in the magazine string can only be used once in your ransom note.
Note:
you may assume that both strings contain only lowercase letters.

Example:
canConstruct('a','b')  return:false
canConstruct('aa','ab') return:false
canConstruct('aa','aab') return:True
'''

'''
The answer:本题是给定两个字符串ransomNote和magazine,判断ransomNote是否可以用magazine中的字母构成，
magazine中的每个字母只能在ransomeNote中用一次，且字母都是小写.

解法1：
1.首先将magazine转换为字符串列表magazine_lst.
2.循环ransomNote，如果ransomNote中的字符不在magazine_lst中的话，直接返回False,如果在，将其从magazine_lst
中删除.
3.如循环完毕,则返回True.

解法2：
1.先构建一个字典dic，然后统计magazine中每个字符出现的次数，即建立字母与其出现的次数的映射.
2.循环ransomNote,如果字符不再dic中，或者其次数等于0，则直接返回False.
3.否则，将对应的字符次数减一.
4.循环完毕后，则返回True.

代码如下.
'''
#解法1
class Solution:
    def canConstruct(self,ransomNote,magazine):
        magazine_lst=list(magazine)
        for i in ransomNote:
            if(i not in magazine_lst):
                return(False)
            magazine_lst.remove(i)
        return(True)



#解法2
class Solution:
    def canConstruct(self,ransomNote,magazine):
        dic={}
        for i in magazine:
            if(i not in dic):
                dic[i]=1
            else:
                dic[i]+=1
        for i in ransomNote:
            if(i not in dic or dic[i]==0):
                return(False)
            dic[i]-=1
        return(True)
        
        
        
        
        
            
