# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:14:58 2019

@author: hecongcong
"""



'''
The problem 421:Maximum XOR of Two numbers in an array
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2**31.
Find the maximum result of ai XOR aj,where 0<=i<j<n;
count you do this in O(n) runtime?
Example:
input:[3, 10, 5, 25, 2, 8]
output:28
Explanation:the maximum result is 5^25=28
'''


'''
The answer:本题是给定一个非负数组nums，找出其中两个数异或的结果最大.
本题的暴力解法非常简单，但是时间复杂度为O(n**2);
核心思路：两个数字异或的结果最大，遵循以下原则：
         1.对于一个数组，其越高的二进制位上为1，其越大；
         2.对于两个数字异或，如果相对应的二进制位不同，则其结果相应二进制位为1，则值越大；
         3.对于一个数字，其二进制上只有两种选择，既0或1；
         4.如果a^b=c,则a=b^c;
         因此，我们可以从数组中所能到的最高位开始，提取各个元素的前缀，并将其放到集合st中，然后每次假设相应的i位上的二进制位1，
         既为较大的值t=res | (1<<i),其中(1<<i)就是假设其第i位为1；然后验证其是否可以由st中的两个前缀元素异或得到；如果能得到的话
         就表明此位可以为1，则值会变大；然后找到后，可以直接跳出循环；
      总结：本题的思路就是从高位开始一位位验证相应的二进制位能不能为1，而且其每次都提取了i位之前的所有前缀，同时res是累加的，所以当某个
      唯一的数字贡献了之前1的位，其后都会锁定于这个数字；如果当某几个数组贡献了之前1的位，在后续的循环中会慢慢筛选出最优的；
代码如下；
'''


#解法1
class Solution:
    def findMaximumXOR(self,nums):
        res=0
        mask=0
        count=len(bin(max(nums)))
        for i in range(count-3,-1,-1):
            mask |=(1<<i)
            st=set()
            for num in nums:    #提取各个数字i位及之前的所有二进制前缀
                st.add(num & mask)
            t=res | (1<<i)    #假设i位上位1，既能取到较大值
            for s in st:
                if(s^t in st):  #验证是否可以取到较大值
                    res=t       #如果能取到的话，则将截止i位时，能取到的最大值i位上更新位1
                    break
        return(res)
            
            
            
            
            
            
            
            
            
            
    
