# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:09:19 2019

@author: hecongcong
"""


'''
The problem 424:Longest Repeating Character Replacement
Given a string that consists of only uppercasr english letters,you can replace any letter in the string with another letter at
most k times.Find the length of a longest subtring containing all repeating letters you can get after performing the above operations.
Note:
Both the string's length and k will not exceed 10**4.

Example1:
input:s = "ABAB", k = 2
output:4
Explanation:replace the two 'A''s with two 'B' or vice versa.
Example2:
input:s = "AABABBA", k = 1
output:4
Explanation:replace the one 'A' in the middle with 'B' and form 'AABBBBA'.
the subtring 'BBBB' has the longest repeating letters,which is 4.
'''


'''
The answer:本题是给定一个只由大写字母构成的字符串s和一个正整数k,其中s中的元素可以被任意字母替换k次，求能组成的最长子字符串的长度，其中子字符串中
的所有元素都一样；
    本题可以用滑动窗口法来解法，但是需要分析一个知识点，如果给定一个字符串strings和k，问怎么满足什么条件替换后就能构成一个所有元素都一样的字符串？思路是统计strings
    中各个字符的个数，再用string的长度减去其中出现最多的字母的个数的结果Q，如果Q<=k的话，则可以构成，同时Q是strings能构成所有字符都一样的字符串需要
    的最少次数；
核心思路：针对s，如果其子串sub_s满足其长度lens,减去其中出现最多字母的个数max_count,即Q=lens-max_count<=k的话，其就能满足题意，所以现在我们的问题变成
了，怎么样在s中找出一个最长子串，使得其满足上述条件，那么这个最长子串的长度即为所求；


解法1：原始解法
思路：每次循环，右窗口的位置为i，左窗口的位置start从0开始向右边更新，直至子串长度i-start+1减去max_count小于等于k;
1.初始化start=0，将其作为滑动窗口的左边，为了统计出现字母的个数，并且方便选出最大值，我们初始化一个长度为26的数组count,可以用大写字母的ascii码减去
65，来一一对应每个字母的位置；
2.循环s，更新count,因为count是单层数据结构，可以用浅拷贝复制一个为tmp,并求出出现次数最多的个数，然后循环，直到子串的长度i-start+1减去max_count的
值<=k;
3.然后更新res,外层循环结束后，返回res.
代码如下；


解法2：优化解法
思路：优化解法和原始解法的整体思路一样，但是原始解法每次左窗口start都是从0开始，而优化解法的start是从上一次的start开始；
因为，上一次的的start肯定刚刚满足i-start+1-max_count=k的，这时候如果i增加1的话，如果增加的一个字母不是max_count所对应的字母，
则会有i-start+1-max_count>k,如果增加的一个字母是max_count所对应的字母，则i-start+1-max_count=k,因此，优化解法的思路正确，即每次
循环可以从上次满足条件的start位置开始；
代码如下；
'''



#解法1：原始解法
class Solution:
    def characterReplacement(self,s,k):
        import copy
        res=0
        max_count=0
        start=0
        lens=len(s)
        count=[0]*26
        for i in range(lens):
            count[ord(s[i])-65]+=1
            tmp=copy.copy(count)
            max_count=max(tmp)
            while(i-start+1-max_count>k):
                tmp[ord(s[start])-65]-=1   #更新子串中的出现次数
                start+=1      #更新左窗口
                max_count=max(tmp)  #更新max_count
            res=max(res,i-start+1)   #更新最终结果res
            start=0  #start再初始化为0
        return(res)
        




#解法2：优化解法
class Solution:
    def characterReplacement(self,s,k):
        res=0
        max_count=0
        start=0
        lens=len(s)
        count=[0]*26
        for i in range(lens):
            count[ord(s[i])-65]+=1
            max_count=max(count)
            while(i-start+1-max_count>k):
                count[ord(s[start])-65]-=1
                start+=1
                max_count=max(count)
            res=max(res,i-start+1)
        return(res)
        







