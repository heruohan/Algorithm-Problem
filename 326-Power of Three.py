'''
Problem:
326:Power of Three.
Given a integer,write a function to determine if it is a power of three.
Example:
Input:27
Output:True

Follow up:
Could you do it without using loop/recursion?
'''
'''
Answer:
自己的思路：这道题的主要难点在于是否可以不用循环和递归.
然后我找规律，发现1-10之间有3(3**1)和9(3**2)两个数，10-100之间有
27(3**3)和81(3**4)两个数，100-999之间有243(3**5)和729(3**6)两个数，
1000-9999之间有2187(3**7)和6561(3**8)两个数，以此类推。
第一步：将n转为str，求其长度，比如n=2187,其长度lens=4，其与对应的3(3**1)差的
倍数即为3**(2*lens-2).
第二步：判断n能不能被3**(2*lens-2)整除，如能整除，判断其商是不是在[3,9]内，如在，
则为True,否则False.
'''

class Solution:
     def isPowerOfThree(self,n):
          if(n==1):
            return(True)
          str_n=str(n)
          lens=len(str_n)
          if(n%(3**(2*lens-2))==0 and n//(3**(2*lens-2)) in [3,9]):  ##判断n能不能被3**(2*lens-2)整除，如能整除，判断其商是不是在[3,9]内
            return(True)
          return(False)
          
