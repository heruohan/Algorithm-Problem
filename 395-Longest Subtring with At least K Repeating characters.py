# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:50:43 2019

@author: hecongcong
"""

'''
The problem 395:Longest Substring with at least k repeating characters
Find the length of the longest substring T of a given string(consist of lowercase letters only) such that
every character in T appears no less than k times.

Example1:
Input:s = "aaabb", k = 3
return:3.
Explanation:the longest substring is 'aaa',as 'a' is repeated 3 times.
Exapmple2:
Input:s = "ababbc", k = 2
return:5
Explanation:the longest substring is 'ababb',as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''


'''
The answer:本题是给定一个字符串s，找到其最长子串的长度，其中子串中的每个元素都要至少出现k次；
本题可用递归和迭代两种解法解答，如下：

解法1：迭代(经典标记法)
思路：可以从s的i位置开始，向后循环，然后二重循环再从i开始到最后，判断每个子字符串s[i:j+1]是否满足条件，如果满足条件则更新res.
所以现在最重要的问题就是如何判断一个字符串是否满足每个字符出现的次数不小于K次，这里用到经典的标记法，如下：
1.因为所有小写英文字母只有26个，因此，可以用diff=ord(s[j])-ord('a'),为每个字母产生唯一的标记数字，比如z就为25；
2.然后设mask=0,其0到25二进制位，分别代表每个字母是否满足条件，如果满足，则相应二进制位为0,否则为1，如果一个字符串
所更新后的mask==0,则表示其所有二进制位都为0，则其所包含的所有字符均满足条件，则这个字符串满足条件，更新res；

步骤：
1.循环s,初始化一个字典m,mask=0,idx=i,构建从i开始的二重循环，利用标记法判断每个字符串是否满足要求；
2.如果满足要求，则更新res,同时更新idx=j;
3.二重循环结束后，更新i=idx+1,因为前一个字符到最后的满足条件的最长子串已经找到，所以不必每次向前移动一位，
因为向前移动一位后，相比于前一次，少了一个字符，其找到的最长子串肯定小于前一次；所以可以直接将指针移动到
中断的位置，重新开始；


解法2：递归(分治法）
思路：
1.如果当一个字符串s的长度小于K时，其结果肯定为0.
2.如果字符串中包含有次数少于k的字符C时，其肯定不满足条件，因此，相当于字符C将字符串s,分成一个个不包含C的子串，
分别对子串进行求解，分分而治，不断迭代；
3.如果一个s中的所有字符都满足条件，则返回s的长度；

代码1：
1.构建一个字典m,开关flag,和表示不满足次数字符的位置的idx.
2.循环s，用字典统计出s中字符和其对应次数的映射.:
3.再循环s，如果遇到不满足条件的字符是s[j]时，则对s[idx:j]调用递归函数，更新res.将flag变为False,表示排除了所有字符均
满足条件的可能；同时，令idx=j+1;
4.当flag为True时，直接返回s的长度，否则返回res和s[idx:lens]的最长子串，因为循环完毕后，自动退出，可能会漏掉s[idx:lens]这一项.

代码2：
代码2的思路和代码1一样，写法更加简洁;
'''

#解法1：
class Solution:
    def longestSubstring(self,s,k):
        res=0
        lens=len(s)
        i=0
        while(i+k<=lens):
            m={}
            mask=0
            idx=i
            for j in range(i,lens):
                diff=ord(s[j])-ord('a')   #创建s[j]唯一的标记数字diff
                m[diff]=m.get(diff,0)+1
                if(m[diff]<k):
                    mask|=(1<<diff)
                else:
                    mask&=~(1<<diff)
                if(mask==0):
                    res=max(res,j-i+1)
                    idx=j
            i=j+1
        return(res)
        
        
        
#解法2：代码1
class Solution:
    def longestSubstring(self,s,k):
        res=0
        lens=len(s)
        if(lens<k):
            return(0)
        m={}
        flag=True
        idx=0
        for i in s:
            if(i not in s):
                m[i]=1
            else:
                m[i]+=1
        for j in range(lens):
            if(m[s[j]]<k):
                res=max(res,self.longestSubstring(s[idx:j],k))
                flag=False
                idx=j+1
        return(lens if(flag) else max(res,\
               self.longestSubstring(s[idx:lens],k)))
        
        
#解法2：代码2
class Solution:
    def longestSubstring(self,s,k):
        lens=len(s)
        if(lens<k):
            return(0)
        for i in set(s):
            if(s.count(i)<k):
                return(max(self.longestSubstring(t,k) \
                           for t in s.split(i)))
        return(lens)









