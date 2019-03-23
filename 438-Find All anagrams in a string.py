# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:59:47 2019

@author: hecongcong
"""


'''
The problem 438:Find All anagrams in a string
Given a string S and a non-empty string p,find all the start indices of P's anagrams in s.
Strings consists of lowercase english letters only and the length of both strings s and p
will not be larger than 20100.
the order of output does not matter.

Example1:
input:s="cbaebabacd"  p:'abc'
output:[0,6]
Explanation:the substring with start index=0 is 'cba',which is an anagram of 'abc'.
the substring with start index=6 is 'bac',which is an anagram of 'abc'.
'''

'''
The answer:本题是给定两个字符串S和P，在S中找出P的所有重构字串的开始位置的索引；
本题可以用滑动法来解答，循环S中的元素，每次拿出P的长度的字串sub_s，比较其是否与P构成
重构字符，如果为真，则将其索引加入到结果res中；而解决sub_s与P的比较问题，则可用两个字典m1和m辅助，
字典中分别是各自的元素与其统计量的映射；如果两个字典相等，则sub_s和P为重构字符串；
为了优化效率，m1可以重复使用，即维护一个长度的len_p的字串，每次开始位置向后移动一位，则m1中对应的
内容进行调整，比如'abcd',从'abc'移动一位到'bcd'的话，将'a'和'd'的信息在m1中调整即可；


解法1：
1.首先将P中的信息对应m，将S的前len_p长度的字串信息对应m1，然后比较，如果相等，则将索引0放入res中；
2.然后从S中的第一位循环，利用滑动的思路更新m1,每次与m进行比较；
代码如下；

解法2：
1.用一个默认字典m，其含义为如果字典中键的值大于等于0,则表示S中字串对应的字符分别还差几个才能与P构成重构字符串；
count表示S中的字串sub_s总共缺少多少各字符才能与P构成重构字符串；
2.分别定义变量left和right表示字符的开始和结束位置；
3.循环S，向前移动right，即将s[right]加入到字串中，如果m[s[right]]的值num大于等于1,则表示对应的字符s[right]在在串中还缺少num个，
才能与P构成重构字符串，因此将s[right]放入字串后，对应的count减1；如果m[s[right]]小于等于0的话，表示子串与P构成重构字符串相对应的
元素已经够了，或者已经多了，此时count不更新；然后在更新m[s[right]]和right.
4.如果count==0的话，表示字串与P构成重构字符串，其中的元素满足要求，即缺少0个；
5.当right-left==len_p的时候，则说明需要删除left这个元素，字串才能保持len_p的长度，如果m[s[left]]的值num大于等于0,即子串与P构成重构字符串
相应的字串还缺少num个，当把s[left]从子串中删除以后，则相应的字串会缺少的多一个,因此count加1；而如果m[s[left]]小于0的话，表示子串中相应的元素
已经多了num个，则不更新count;然后再更新m[s[left]]和left;
代码如下；
'''


#解法1：
class Solution:
    def findAnagram(self,s,p):
        m={}
        m1={}
        res=[]
        len_s=len(s)
        len_p=len(p)
        if(len_s<len_p):
            return([])
        for i in range(len_p):
            m[p[i]]=m.get(p[i],0)+1
            m1[s[i]]=m1.get(s[i],0)+1
        if(m1==m):
            res.append(0)
        for i in range(1,len_s-len_p+1):
            if(s[i-1]==s[i+len_p-1]):  #如果前后相等，则m1不变
                if(m1==m):
                    res.append(i)
                    continue
            else:
                m1[s[i-1]]-=1  #s[i-1]一定在m1中
                if(m1[s[i-1]]==0):   #如果m1[s[i-1]]为0,则将其键值对从字典中删除
                    m1.pop(s[i-1])
                m1[s[i+len_p-1]]=m1.get(s[i+len_p-1],0)+1
                if(m1==m):
                    res.append(i)
        return(res)
        
        



#解法2：滑动窗口法
class Solution:
    def findAnagram(self,s,p):
        import collections
        len_s=len(s)
        len_p=len(p)
        res=[]
        m=collections.defaultdict(int)
        count=len_p
        for i in p:
            m[i]+=1
        left,right=0,0
        while(right<len_s):
            if(m[s[right]]>=1):
                count-=1
            m[s[right]]-=1
            right+=1
            if(count==0):
                res.append(left)
            if(right-left==len_p):
                if(m[s[left]]>=0):
                    count+=1
                m[s[left]]+=1
                left+=1
        return(res)
        





