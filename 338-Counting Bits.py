# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:42:17 2018

@author: hecongcong
"""
'''
The question 338:Counting Bits
    Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate
the number of 1's in their binary representation and return them as an array.

Example:
Input:5
Output:[0,1,1,2,1,2]
'''

'''
The answer:本题的题意是给一个正整数num，返回一个列表，其中的元素分别代表[0,num]之间的数所对应二进制中1的个数.
此题有两种解法，分别如下所示：
解法1：
    当数字i是2的指数时,比如4，8，16，其二进制码分别位100，1000，10000；再如当i等于8时，其二进制为1000，所以二进制1000到1111，即8到15之间
的数二进制中1的个数为二进制000到111之间的数，即0到7之间的数二进制中1个个数加1.所加的1即为1000到1111最前面那个1.
代码如下.

解法2：
    一个正整数num,其二进制中所有位的1，所对应的位数设为a,b,c，则num=2**a+2**b+2**c.
    所以当一个数num为奇数时，其二进制最后一位必为1，则将其进行右移运算,即num1=num>>1,因为舍弃掉num最后一位1，所以num二进制中所含1的个数等于num1
 中所含1的个数加1；
 如num为偶数时，其二进制的最后一位必为0，将其进行右移运算，即num1=num>>1,因为最后一位舍弃的时0，所以num二进制中1的个数等于num1二进制中1的个数;
 代码如下.
'''
#解法1
def countBits(num):
    res=[0,1,1,2]
    if(num<=3):
        return(res[:num+1])
    count=2
    for i in range(4,num+1):
        if(i==2*count):
            count=i
        res.append(1+res[i-count])
    return(res)


#解法2
def contBits1(num):
    res=[0]
    for i in range(1,num+1):
        if(i%2==0):
            res.append(res[i>>1])
        else:
            res.append(res[i>>1]+1)
    return(res)
    
    
    
    
    
    
    
    
    
    
    
    
    
