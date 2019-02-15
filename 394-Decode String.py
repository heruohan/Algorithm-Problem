# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:06:11 2019

@author: hecongcong
"""

'''
The problem 394:Decode String
Given an encoded string,return it is decoded string.
The encoding rule is:k[encoded_string],where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.
you may assume that the input string is always valid:No extra white spaces,square brackets are well-formed,etc.
furthermore,you may assume that the original data does not contain any digits and that digits are only for those repeat numbers,
k.For example,there will not be input like 3a or 2[4].

Examples:
s="3[a]2[bc]",return "aaabcbc".
s= "3[a2[c]]",return "accaccacc".
s= "2[abc]3[cd]ef",return "abcabccdcdcdef".
'''



'''
The answer:本题是给定一个编码的字符串，返回它的解码字符串，编码规则如下：k[encoded_string],指的是encoded_string的k次，其中k是一个正整数；
在这个字符串中只有左右中括号，数字，字母几种字符，本题有两种解题思路，一种是迭代加栈数据结构辅助，另一种是递归，如下：

解法1：迭代+栈
1.构造一个栈st,然后循环s,当遇到']'时，则栈中的顶元素肯定为字母，则循环取出组成字符串res,并删除，直到遇到'[';
2.而'['的前面肯定为数字，然后将其依依取出，将字符串数字转换为数字，并将res合并成重复的字符串res,压入栈中；
3.循环s时，如遇到其他元素，则直接压入栈中；
4.将栈中的元素合并，并返回.
代码如下.


解法2：递归
1.构造一个辅助函数helps,其中有两个参数，其中第二个参数是一个单元素的列表，列表中的元素为指向s的指针(这里不能直接用数字来表示指针，
原因见后),递归的终止条件为指针到达字符串s的最末尾，及指针指向s的']'元素；
2.因为数字后面只能跟'['，当遇到数字的时候就不断后移，将其取出，转化成数字，直到遇到'[',但是指针向前移动一位，跳过'[',必然会指向字母，
然后递归，将括号里的内容转化为字符串，求出来即为t，这时指针指向']'，然后向前移动一位跳过，并将结果存入到res中；
3.直到循环结束，求出的res即为从指针指向的开始位置，到满足结束条件，之间的内容，转化为合适的字符串结果；
4.在整个递归过程中，指针是不断向前移动的，递归函数的指针参数需带有记忆性，并且指针起始位置只会指向数字或者字母；

代码技巧：
1.在迭代过程中，辅助函数中的指针参数会不断的移动，这时迭代函数中的指针参数需要有记忆性，不能够就由一个整数作为参数，因为如果一个整数数据类型
作为参数传入函数中时，其不断赋值做运算，值不断改变，id也不断在改变，所以并不具有传递性；
如果用一个列表作为参数，由于其中元素的改变，但是整个列表的id并不会发生变化，所以传进函数的列表会随之变化，例子如下：

例1：
a=1
def fn(x):
    x+=1
    return(x)
fn(a),,return:2,但是a还是等于1；

例2：
a=[1]
def fn(x):
    x[0]+=1
    return(x)
fn(a),,return:[2],同时a=[2];

2.为了避免上述用列表的麻烦，可以用相当于全局变量的实例化对象的属性，来当作指针，如代码2；
'''
#解法1:迭代+栈
class Solution:
    def decodeString(self,s):
        ret=''
        st=[]
        for i in s:
            if(i==']'):
                tmp=st.pop()
                res=tmp
                while(tmp!='['):
                    tmp=st.pop()
                    if(tmp!='['):
                        res=tmp+res
                num=''
                while(st and ('0'<=st[-1]<='9')):
                    num=st.pop()+num
                res=res*int(num)
                st.append(res)
            else:
                st.append(i)
        for j in st:
            ret+=j
        return(ret)
        
                
    
#解法2:递归(重点，难点)
class Solution:
    def decodeString(self,s):
        lst=[0]
        return(self.helps(s,lst))
        
    def helps(self,s,lst):
        res=''
        lens=len(s)
        while(lst[0]<lens and s[lst[0]]!=']'):
            if(s[lst[0]]<'0' or s[lst[0]]>'9'):
                res+=s[lst[0]]
                lst[0]+=1
            else:
                count=0
                while(s[lst[0]]>='0' and s[lst[0]]<='9'):
                    count=10*count+int(s[lst[0]])
                    lst[0]+=1
                lst[0]+=1
                t=self.helps(s,lst)
                lst[0]+=1
                res=res+t*count
        return(res)
        

#代码3：
class Solution:
    def decodeString(self,s):
        self.i=0
        return(self.helps(s))
        
    def helps(self,s):
        res=''
        lens=len(s)
        while(self.i<lens and s[self.i]!=']'):
            if(s[self.i]<'0' or s[self.i]>'9'):
                res+=s[self.i]
                self.i+=1
            else:
                count=0
                while(s[self.i]>='0' and s[self.i]<='9'):
                    count=10*count+int(s[self.i])
                    self.i+=1
                self.i+=1
                t=self.helps(s)
                self.i+=1
                res=res+t*count
        return(res)
        
                        











