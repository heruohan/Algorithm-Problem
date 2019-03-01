# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 22:45:36 2019

@author: hecongcong
"""


'''
The problem 409:Longest Palindrome
Given a string which consists of lowercase or uppercase letters,find the length of the longest palindromes that can be
built with those letters.
This is case sensitive,for example 'Aa' is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1010.
Example:
input:s="abccccdd"
output:7
Explanation:one longest palindrome that can be built is "dccaccd" ,whose length is 7.
'''


'''
The answer:本题是给定一个由大写和小写字母组成的字符串，找出由它组成的最长回文字符的长度.
回文字符组成只有两种情况，第一种是有一个奇数的字符，其余字符全是偶数，比如'acbca';另一种情况是所有字符全是偶数个，比如'aabbaa';

解法1：
1.用字典m统计s里面所有字符的个数;
2.然后循环m,如果未偶数则直接加入结果res中，如果为奇数则将小于等于其且最大偶数加入res中；同时count加1；
3.如果count为0则直接返回res,否则返回res加1；
代码如下；

解法2：
1.构建一个集合a,如果s中的字符没在a中就加入，如果在a中就删除，循环完毕后，a的长度就是s中有奇数个数字符的数量；
2.如果a的长度为0,则返回s的长度减0；如果a的长度不为0，则返回s的长度减去a的长度在加1，即len(s)-(len(a)-1).
综上，就是返回len(s)减去0和len(a)-1中的较大值；
代码如下；
'''
#解法1
class Solution:
    def longestPalindrome(s):
        m={}
        for i in s:
            if(i not in m):
                m[i]=1
            else:
                m[i]+=1
        res=0
        count=0
        for i in m:
            if(m[i] % 2==0):
                res+=m[i]
            else:
                res+=(m[i]-1)
                count+=1
        return(res if(count==0) else res+1)



#解法2
class Solution:
    def longestPalindrome(s):
        a=set()
        for i in s:
            if(i not in a):
                a.add(i)
            else:
                a.remove(i)
        return(len(s)-max(0,len(a)-1))









