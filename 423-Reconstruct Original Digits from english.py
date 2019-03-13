# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:38:21 2019

@author: hecongcong
"""


'''
The problem 423:Reconstruct Original Digits from English
Given an non-empty string containing an out-of-order English representation of digits 0-9,output the digits in ascending order.
Note:
1.input contains only lowercase english letters.
2.input is guaranteed to be valid and can be transformed to its original digits.that means invalid input such as 'abc' or 'zerone'
are not permitted.
3.input length is less than 500000.
Example1:
input:"owoztneoer"
output:'012'
Example2:"fviefuro"
output:'45'
'''


'''The answer:本题是给定一个包含代表0-9数字小写英文字符的无序字符串s，输出数字升序；
核心思路：1.首先统计s中各个字符的个数；
         2.然后观察0-9各个数字的因为字符的特点，可以看出0，2,4,6,8只包含字母'z','w','u','x','g'.因此可以直接确定出0,2,4,6,8几个数字的个数；
         然后字母'o'只在数字0,1,2,4中，所以可以确定出1的个数；字母'h'只在数字3,8中，因此可以确定出3的个数；字母'f'只在数字4,5中，因此可以确定
         出5的个数；字母's'只在数字6,7中，则可以确定出7的个数；字母'i'只在数字5,6,8,9中，因此可以确定出9的个数；
         代码如下；
'''
#解法1
class Solution:
    def originalDigits(self, s):
        mps={}
        tables=['zero','one','two','three','four','five','six','seven','eight','nine']
        res=''
        chs=('z','w','u','x','g','o','h','f','s','i')
        m={'z':'zero','w':'two','u':'four','x':'six','g':'eight',\
             'o':'one','h':'three','f':'five','s':'seven','i':'nine'}   #这些字母的先后顺序不能变化
        for i in s:
            if(i not in mps):
                mps[i]=1
            else:
                mps[i]+=1
        for i in chs:
            if(i in mps and mps[i]>0):
                while(mps[i]):
                    for j in m[i]:
                        mps[j]-=1
                    res+=str(tables.index(m[i]))
        return(''.join(sorted(res)))
        
        
                
#代码2
class Solution:
    def originalDigits(self,s):
        import collections
        mps={}
        tables=['zero','one','two','three','four','five','six','seven','eight','nine']
        res=''
        m=collections.OrderedDict([('z','zero'),('w','two'),('u','four'),('x','six'),\
                                  ('g','eight'),('o','one'),('h','three'),('f','five'),\
                                  ('s','seven'),('i','nine')])    #因为一般的字典是无序的，不符合解法要求，所以可以用有序字典替代
        for i in s:
            if(i not in mps):
                mps[i]=1
            else:
                mps[i]+=1
        for i in m:
            if(i in mps and mps[i]>0):
                while(mps[i]):
                    for j in m[i]:
                        mps[j]-=1
                    res+=str(tables.index(m[i]))
        return(''.join(sorted(res)))
    
            
            
            
            
            
            
            
