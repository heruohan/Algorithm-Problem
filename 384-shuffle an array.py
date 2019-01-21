# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:38:53 2019

@author: hecongcong
"""

'''
The problem 384:shuffle an array
shuffle a set of numbers without duplicates.
Example:
//init an array with set 1,2 and 3.
int[] nums={1,2,3}
Solution solution=new Solution(nums)

//shuffle the array [1,2,3] and return its result.any permutation of [1,2,3] must
equally likely to be returned.
solution.shuffle()

//resets the array back to its original configuration [1,2,3].
solution.reset()

//returns the random shuflling of array [1,2,3].
solution.shuffle().
'''

'''
The answer:本题是对一个数组进行重新排列，并且以等概率将其返回，同时在实现一个reset方法，将数组重置
到其原始配置；本题的难点在于实现shuffle方法.

解题思路：
1.对于一个数组cur_lst,设其长度为lens,则其全部的组合数nums等于lens的阶乘,每一个出现的概率就为1/nums.
2.同时，一个数组的排列都必定可以通过多次随机交换其元素生成，比如，cur_lst=[1,2,3],它全部的排列数位3!=6个，
[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1];例如，要生产[2,3,1],
可以采取以下路径：[1,2,3]>=[1,2,3]>=[2,1,3]>=[2,3,1];则通过此路径生成[2,3,1]的概率P=1*1/2*1/3=1/6;
因此，满足题意要求.
代码如下.

注意问题：
因为例如:对于复杂数据结构a=[1,2,3],将其赋值给b=a,两者会完全共享资源，一个值的改变，另一个值也会改变，因此
需要将其拷贝一份，切断其共享路径；
'''

class Solution:
    def __init__(self,nums):
        '''
        :ype nums:List[int]
        '''
        self.lst=head
    def reset(self):
        '''
        resets the array to its original configuration and return it.
        :rtype:List[int]
        '''
        return(self.lst)
    def shuffle(self):
        '''
        returns a random shuffling of the array.
        :rtype:List[int]
        '''
        import random
        import copy
        cur_lst=copy.copy(self.lst)  #重新拷贝一份，而并不是直接赋值
        for idx,value in enumerate(cur_lst):
            j=random.randint(0,idx)
            cur_lst[idx],cur_lst[j]=cur_lst[j],value
        return(cur_lst)
        



