# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 00:38:56 2019

@author: hecongcong
"""


'''
The problem 414:Third Maximum Number
Given a non-empty array of integers,return the third maximum number in this array.if it dose not exist,return the maximum number.
the time complexity must be in O(n).

Example1:
input:[3, 2, 1]
output:1
Explanation:the third maximum is 1.
Example2:
input:[1, 2]
output:2
explanation:the third maximum does not exist,so the maximum(2) is returned instead.
example3:
input:[2, 2, 3, 1]
output:1
explanation:note that the third maximum here means the third maximum distinct number.
both numbers with value 2 are both considered as second maximum.
'''



'''
The answer:本题是给定一个非空的整数数组nums，返回第三大的数字，如果不存在则返回此数组中的最大值.并且在时间复杂度O(n)内完成.

解法1和解法2思路相同，解法1是先对nums进行排序，然后统计去重；解法2先是用集合数据结构将其去重，然后排序；
但是这两种解法不满足时间复杂度的要求；


解法3：
思路：维持一个长度为3的s数组，运用二分查找法将其按升序插入；并且构建一个集合visited去重；循环我完毕后，如果s的长度小于3则证明没有找到
第三大的元素，返回数组的最大值；否则返回数组的第一个值；但是时间复杂度也不满足题目要求；
代码如下；

解法4：
思路：构建三个变量first,second,third分别表示第一大，第二大，第三大的元素，然后循环数组，分情况讨论，维持三个变量的升序关系，同时，使得不在
已存在的变量端点上，可以自动去重，最后判断并返回结果；此种解法可以实现时间复杂度O(n);
代码如下；
'''
#解法1
class Solution:
    def thirdMax(self,nums):
        nums.sort(reverse=True)
        count=1
        lens=len(nums)
        for i in range(1,lens):
            if(nums[i]!=nums[i-1]):
                count+=1
            if(count==3):
                return(nums[i])
        return(nums[0])




#解法2：
class Solution:
    def thirdMax(self,nums):
        s=set(nums)
        lst=list(s)
        lst.sort(reverse=True)
        if(len(lst)<3):
            return(lst[0])
        return(lst[2])
        



#解法3：
class Solution:
    def thirdMax(self,nums):
        import bisect
        s=[]
        visited=set()
        for i in nums:
            if(i not in visited):
                bisect.insort_left(s,i)   #运用二分查找法升序插入
                if(len(s)>3):
                    s.pop(0)
        return(s[0] if(len(s)==3) else s[-1])



#解法4：
class Solution:
    def thirdMax(self,nums):
        import math
        first=-math.inf
        second=-math.inf
        third=-math.inf    
        for i in nums:
            '''
            循环过程中维持first,second,third升序排列
            '''
            if(i>first):
                third=second
                second=first
                first=i
            elif(i!=first and i>second):  #!=first自动去重
                third=second
                second=i
            elif(i!=first and i!=second and i>third):   #自动去重
                third=i
        return(third if(third!=-math.inf) else first)
        
        
        
        
        
        
        
        
        
        
