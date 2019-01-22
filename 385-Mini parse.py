# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:48:47 2019

@author: hecongcong
"""

'''
The problem 385:Mini parse
Given a nested list of integers representing as a string,implement a parse to deserialize it.
each element is either an integer,or a list--whose elements may also be integers or other lists.
Note:you may assume that the string is well-formed:
1.string is non-empty.
2.string does contain white-spaces.
3.string only contain digits 0-9, [, - ,, ].

Example1:
Given s='324'
you should return a NestedInteger object which contains a single integer 324.
Example2:
given s='[123,[456,[789]]]",
return a NestedInteger object containing a nested list with 2 elements:
1.an integer containing value 123.
2.a nested list containing two element:
     i:an integer containing value 456.
     ii:a nested list with one element:
          (1)a integer containing value 789.
'''


'''
this is the interface that allows for creating nested lists.
you should not implement it,or speculate about its implementation.
''''

#class NestedInteger:
#    def __init__(self,val):
#        '''
#        if val is not specified,initializes an empty list.
#        otherwise initializes a single integer equal to val.
#        '''
#    def isIntegers(self):
#        '''
#        return true if the nestedinteger holds a single integer,ranther than a nested list.
#        :rtype:bool
#        '''
#    def add(self,elem):
#        '''
#        set this nestedinteger to hold a nested list,and adds a nested integer elem to it.
#        :rtype:void
#        '''
#    def setInteger(self,value):
#        '''
#        set this nestedinteger to hold a single integer equal to value.
#        :rtype:void
#        '''
#    def getInteger(self):
#        '''
#        return the single integer that this nestedinteger holds,if it holds a single integer.
#        return None if this nestedinteger holds a nested list.
#        rtype:int
#        '''
#    def getList(self):
#        '''
#        return the nested list that this nestedinteger holds,if it holds a nested list.
#        return None if this nestedinteger holds a single integer.
#        :rtypr:List[nestedinteger]
#        '''


'''
The answer:本题是给定一个字符串，实现一个解析器解析它.本题有两种解法，一种方法是递归，另一种方法是
迭代辅助栈数据结构.

解法1：迭代+栈
1.首先构建栈st和start,start是记录起始位置的索引，然后循环字符串s；
2.当s[i]为'['时，初始化一个NestedInteger对象，并将其压入栈中，同时将start更新为i+1;
3.因为同一层级的NestedInteger对象中的元素是用','分开，以']'结尾的，所以如果s[i]==','时，
将子字符串加入进去，start加1，当s[i]==']'时，表示最内层的nestedlist以取完，则看st的长度是否
大于1，如果大于1，则将其删除并加入到栈顶的nestedinteger中；
代码如下.

解法2：递归
1.构建递归退出条件：首先当len(s)==0时，直接返回nestedinteger对象，当s的首个元素不为'['时，表示其时一个数字字符串，
则直接返回，当s的首个字符为'['并且len(s)<=2时，表示s为空，则直接返回；
2.否则初始化一个nestedineger对象res,start记录起始位置，以及tmp，当tmp为0时，表示'['和']'是同以层级的，既NestedInteger
对象的开始和结束.
3.从索引1开始循环字符串，当tmp==0并且s[i]==','或者已到达当前字符串的最后位置时，表明取得是当前字符串s相同层级的元素，则
进行递归求解，并将其加入到res中，start则向前移动一位；
4.如果s[i]=='['，则tmp加1，s[i]==']'时，则tmp减1；
代码如下.
'''
        
#解法1:迭代+栈
class Solution:
    def deserialize(self,s):
        if(len(s)==0):
            return(NestedInteger())
        if(s[0]!='['):
            return(NestedInteger(int(s)))
        st=[]
        start=1
        for i in range(len(s)):
            if(s[i]=='['):
                st.append(NestedInteger())
                start=i+1
            elif(s[i]==',' or s[i]==']'):
                if(i>start):
                    st[-1].add(NestedInteger(int(s[start:i])))
                start=i+1
                if(s[i]==']'):
                    if(len(st)>1):
                        tmp=st.pop()
                        st[-1].add(tmp)
        return(st[-1])
        
        
#解法2：递归
class Solution:
    def deserialize(self,s):
        if(len(s)==0):
            return(NestedInteger())
        if(s[0]!='['):
            return(NestedInteger(int(s)))
        if(len(s)<=2):
            return(NestedInteger())
        res=NestedIneger()
        start=1
        tmp=0
        for i in range(1,len(s)):
            if(tmp==0 and (s[i]==',' or i==len(s)-1)):
                res.add(self.deserialize(s[start:i]))
                start=i+1
            elif(s[i]=='['):
                tmp+=1
            elif(s[i]=']'):
                tmp-=1
        return(res)
        
        
        
        
        
        
        
                    
                
                
