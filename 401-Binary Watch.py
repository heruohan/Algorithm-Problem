# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 00:00:52 2019

@author: hecongcong
"""


'''
The problem 401:Binary Watch
A binary watch has 4 LEDs on the top which represents the hour(0~11),and 6 LEDs on the bottom represent the minutes(0~59).
Each LED represents a zero or one,with the least significant bit on the right.
Given a non-negative integer n which represents the number of LEDs that are currently on,return all possible times the watch
could represent.

Example:
Input:n=1
return:["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
1.the order of output does not matter.
2.the hour must not contain a leading zero,for example the "01:00" is not valid,it should be "1:00".
3.the minute must be consist of two digits and may contain a leading zero,for example  "10:2" is not valid,it
should be  "10:02".
'''



'''
The answer:本题是有一个二进制表，上面有4个LED代表小时(0~11),下面有6个代表分钟(0~59),给定一个非负的整数n，表示亮着灯的LED个数，返回表
所代表的可能时间，本题有两种解题方法，如下：

解法1：
1.小时在题目给定的范围内循环，分钟也在题目给定的范围内循环，然后分别用bin()函数将其转换为二进制，统计其中'1'的个数，如果
两者之和等于num,则满足题目要求.
2.但是需要注意分钟数如果小于10的话需要在其前面加个0，然后将其转化为字符串放入结果中即可；
代码如下.


解法2：
1.首先构建一个辅助函数generate(lst,count),其中lst表示分钟表或者小时表每个LED单独亮起的所代表时间的列表，count代表对应的表有几个LED亮灯，
其函数返回值是给定count个LED亮灯时，分钟时间和小时时间所有可能取到的时间集合；
2.然后进行循环，分别生成小时时间和分钟时间对应亮灯数的时间集合，然后循环集合，如果满足题目中的要求，则将其转化为字符串放入结果中；
代码如下；
'''



#解法1
class Solution:
    def readBinaryWatch(self,num):
        res=[]
        for h in range(12):
            for m in range(60):
                if(bin(h).count('1')+bin(m).count('1')==num):
                    if(m>=10):
                        res.append(str(h)+':'+str(m))
                    else:
                        res.append(str(h)+':'+'0'+str(m))
        return(res)




#解法2
class Solution:
    def readBinaryWatch(self,num):
        hour=[1,2,4,8]
        minutes=[1,2,4,8,16,32]
        res=[]
        for h in range(num+1):
            h_res=self.generate(hour,h)
            m_res=self.generate(minutes,num-h)
            for i in h_res:
                if(0<=i<=11):
                    for j in m_res:
                        if(0<=j<=9):
                            res.append(str(i)+':'+'0'+str(j))
                        elif(10<=j<=59):
                            res.append(str(i)+':'+str(j))
        return(res)
    
    def generate(self,lst,count):
        res=[]
        self.helpFn(lst,count,0,0,res)
        return(res)
    
    def helpFn(self,lst,count,start,val,res):  #因循环过程中不能有重复计算，所以start表示从上次循环的下个索引开始
        '''
        此函数不需要返回值，其在递归过程中，更新res列表.
        '''
        if(count==0):
            res.append(val)
            return
        for i in range(start,len(lst)):
            self.helpFn(lst,count-1,i+1,val+lst[i],res)
            










