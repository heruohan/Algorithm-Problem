# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 00:42:20 2019

@author: hecongcong
"""

'''
The problem 393:UTF-8 Validation
A character in UTF8 can be from 1 to 4 bytes long,subjected to the following rules:
1.for 1-byte character,the first bit is a 0,followed by its unicode code.
2.for n-bytes character,the first n-bits are all one's,the n+1 bit is 0,followed by n-1 bytes with most significant
2 bits being 10.
This is how the utf-8 encoding would work:
Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx


Given an array of integers representing the data,return whether it is a valid utf-8 encoding.
Notes:
the input is an array of integers,only the least significant 8 bits of each integer is used to store the data.
this means each integer represents only 1 byte of data.

Example1:
data=[197, 130, 1],which represents the octet sequence:11000101 10000010 00000001.
return True.
it is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example2:
data=[235, 140, 4],which represented the octet sequence:11101011 10001100 00000100.
return false.
the first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
the next byte is a continuation byte which starts with 10 and that is correct.
but the second continuation byte does not start with 10,so it is invalid.
'''



'''
The answer:这道题读了很久才读懂题意，就是给定一个整数数组，判断其实不是一个有效的Utf-8编码.其中utf-8的规则如下：
1.对于一个字节的字符，其二进制的第一位是0,；
2.对于n个字节的字符，其中一个字节的前n位全部是1，第n+1位是0，而接下来的n-1个字节的前两位都是10.
本题可以用位运算进行求解；其思路是如果第一位非0的话，统计出前n位1的个数，即字符字节的长度；其中的字符字节长度
只能是1到4；


解法1：与运算符
1.初始化一个指针i,然后循环data,当data[i]>255时不满足题意，直接返回false.
2.运用与运算符统计字符字节的长度n-1,即其后所跟的字节开头的10的字节个数；如果长度不在1-4之间的情况，则直接返回False.
3.然后循环data[i]其后的n-1个元素，检查是否其开始两位为10,但是要保证在字符总长度之内；
4.然后使指针跳过n-1个元素，重新开始；（此处不能用for循环，要用while循环，因为在python中for循环始终是按顺序循环，并不会跳跃）
代码技巧：
1.当需要循环跳跃的时候，不能使用for循环，因为在python中for循环始终是按顺序进行循环；

解法2：右移运算符+控制循环开关
1.此种解法，不需要再循环中跳跃，按顺序进行循环，但是相当于加一个开关控制循环过程；
2.首先统计第一位非0的情况，字符的长度减1即count,然后最后一个判断将字节右移7位如果结果非0的话，直接返回false.因为此种情况
排除了长度为1个字节的字符，即首位为0的情况，同时也排除了长度为2-4的情况，因为在它前面已经讨论过；所以剩下的都是长度不为1-4的情况
即直接返回false.（note:但是此条件必须写在最后进行判断）
3.对于控制循环过程，当count==0时，即进行统计得出count.当count!=0时，依次向下循环，检查其前两位是否为10，如不满足直接返回
false,如果满足，count自减1；
4.最后循环完毕后，判断count是否等于0;
'''
#解法1
class Solution:
    def validUtf8(self,data):
        i=0
        lens=len(data)
        while(i<lens):
            if(data[i]>255):
                return(False)
            count=0
            if((data[i] & 0b10000000)==0):
                count=0
            elif((data[i] & 0b11100000)==0b11000000):
                count=1
            elif((data[i] & 0b11110000)==0b11100000):
                count=2
            elif((data[i] & 0b11111000)==0b11110000):
                count=3
            else:               #字符字节的长度不在1-4的情况中
                return(False)
            for j in range(i+1,i+count+1):
                if(j>=lens or (data[j] & 0b11000000)!=0b10000000):
                    return(False)
            i+=count+1
        return(True)
        



#解法2
class Solution:
    def validUft8(self,data):
        count=0
        for dt in data:
            if(count==0):
                if(dt>>5==0b110):
                    count=1
                elif(dt>>4==0b1110):
                    count=2
                elif(dt>>3==0b11110):
                    count=3
                elif(dt>>7):   ##此判断条件必须位于最后
                    return(False)
            else:
                if(dt>>6!=0b10):
                    return(False)
                count-=1
        return(count==0)











