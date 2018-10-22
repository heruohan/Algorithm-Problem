# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:29:37 2018

@author: hecongcong
"""
'''
The question 342:Power of Four
    Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
   
Example 1:
Input:16
Output:True

Example 2:
Input:5
Output:False

Follow up:Could you solve it without loops/recursion?
'''

'''
The answer:本题的题意是给一个整数，判断其是否是4的次方数.更进一步，是否可以不用循环或者递归来解答.
本题有两种思路及解法，分别如下：
解法1：
    首先，一个正整数num，如为4的次方数，则必为2的次方数，即num=2**n,因此必有(num-1)&num==0;再次，
如num=4**n,则num-1=4**n-1=4*(4**(n-1)-1)+3,可解得num-1=4**n-1=3+3*4+3*4**2+....+4**(n-1)*3+3*4**(n-2),
即num-1可被3整除.
代码如下.

解法2：
    如num为4的次方数，则其二进制码为0001,100,10000,1000000等等，其中1的位置为奇数位；而其余2的次方数，如8,其
二进制码为1000，1在偶数位，因此，在num-1&num==0的基础上，num与1431655765，即二进制1010101010101010101010101010101进行按位与
运算，如果其结果等于其自身，则证明num是4的次方数，而不是2的次方数.
'''
#解法1
def isPowerOfFour(num):
    return(num>0 and (not num-1 & num) and (num-1)%3==0) #条件顺序不能颠倒，下同
 

#解法2
def isPowerofFour1(num):
    a='1010101010101010101010101010101'
    num1=int(a,2)
    return(num>0 and (not (num-1 & num)) and (num1 & num==num))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
