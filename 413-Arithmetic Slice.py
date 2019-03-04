# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:38:38 2019

@author: hecongcong
"""


'''
The problem 413:Arithmetic Slice
A sequence of number is called arithmetic if it consists of at least three elements,if the difference between any two
consecutive elements is the same.
For example,these are arithmetci sequence:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
the following sequence is not arithmetic:
1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given.A slice of that array is any pair of integers (P,Q) such that 0 <= P < Q < N.
A slice (P,Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic.in particular,this means that P + 1 < Q.
the function should return the number of arithmetic slices in the array A.

Example:
A=[1, 2, 3, 4]
return:3,for 3 arithmetic slices in A:[1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
'''



'''
The answer:本题是给定一个数组A，求其算术切片的数量，算术切片其实就是一个长度不小于3的等差数列；
思路：首先，如果一个数列lst是长度为n的等差数列，则其总共的算术切片数量是sums=0.5*(n-1)*(n-2).
比如，lst=[1,2,3,4,5,6,7],以7为结尾的算术切片个数为7-2,以6为6-2，直到3为1，终止；所以如果lst长度
为n，则sums=1+2+3+....+(n-3)+(n-2),根据等差数列的求和公式sums=(n-2)*1+0.5*(n-2)*(n-3)*1=0.5*(n-1)*(n-2).


解法1：
1.首先，找出长度不小于3的算术序列的长度，dist,然后把个数循环累加到res.
2.然后在从上一个算术序列的末尾元素开始循环.因为，此时start可以不从上一个算术序列的开始位置的下一个元素开始，
因为其和后面的元素肯定不会构成一个等差数列；
代码如下；


解法2：和解法1的思路相同，只是知道长度后直接用公式算出一个等差数列有多少个算术切片.

解法3：
思路：算法的进一步优化，构建count表示最长等差数列的长度，在不构成等差数列时，如果count>2,则用公式将其计算出，
并将count设置为2.


解法4：动态规划
1.构建一个长度为len(A)的一维数组，其中dp[i]表示以A[i]元素为尾算术切片的个数，因此，如果A[i]-A[i-1]==A[i-1]-A[i-2]时，dp[i+1]=dp[i]+1.
2.然后把dp[i]各个位置上的值累加.


解法5：也是动态规划的思想，是对解法4的空间的一个优化，直接不要dp数组，用一个int类型的数字tmp来更新；
代码如下；
'''
#解法1
class Solution:
    def numberOfArithmeticSlice(self,A):
        start=0
        lens=len(A)
        res=0
        while(lens-start>=3):
            tmp=start+1
            diff=A[tmp]-A[start]
            end=tmp+1
            while(end<lens and A[end]-A[tmp]==diff):
                end+=1
                tmp+=1
            dist=end-start
            count=2
            while(dist-count>=1):
                res+=(dist-count)
                count+=1
            start=end-1
        return(res)



#解法2
class Solution:
    def numberOfArithmeticSlice(self,A):
        start=0
        lens=len(A)
        res=0
        while(lens-start>=3):
            tmp=start+1
            diff=A[tmp]-A[start]
            end=tmp+1
            while(end<lens and A[end]-A[tmp]==diff):
                end+=1
                tmp+=1
            dist=end-start
            res+=(0.5*(dist-1)*(dist-2))
            start=end-1
        return(int(res))
        


#解法3：
class Solution:
    def numberOfArithmeticSlice(self,A):
        lens=len(A)
        res=0
        count=2
        for i in range(2,lens):
            if(A[i]-A[i-1]==A[i-1]-A[i-2]):
                count+=1
            else:
                if(count>2):
                    res+=0.5*(count-1)*(count-2)
                    count=2
        return(int(res) if(count==2) else int(res+0.5*(count-1)*(count-2)))
     
    
    

#解法4：动态规划
class Solution:
    def numberOfArithmeticSlice(self,A):
        lens=len(A)
        res=0
        dp=[0]*lens
        for i in range(2,lens):
            if(A[i]-A[i-1]==A[i-1]-A[i-2]):
                dp[i]=dp[i-1]+1
            res+=dp[i]  #当不满足上述判断条件时，dp[i]为0
        return(res)
        
    


#解法5：
class Solution:
    def numberOfArithmeticSlice(self,A):
        lens=len(A)
        res=0
        tmp=0
        for i in range(2,lens):
            if(A[i]-A[i-1]==A[i-1]-A[i-2]):
                tmp+=1
                res+=tmp
            else:
                tmp=0    #当A[i]不满足上述判断条件时，将tmp令为0，因为以A[i]为尾的算术切片的个数此时为0.
        return(res)
        











