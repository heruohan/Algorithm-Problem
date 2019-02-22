# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:23:37 2019

@author: hecongcong
"""


'''
The problem 402:Remove K digits
Given a non-negative integer num represented as a string,remove k digits from the number so that the new number is the
smallest possible.
Note:
1.the length of the number is less than 10002 and will be >=k.
2.the given num does not contain any leading zero.

Example1:
input:num = "1432219", k = 3
output:"1219"
Explanation:remove the three digits 4,3 and 2 to form the new number 1219 which is the smallest.

Example2:
input: num = "10200", k = 1
output:'200'
Explanation:remove the leading 1 and the number is 200.note that the output must not contain leading zeros.

Example3:
input: num = "10", k = 2
output:'0'
Explanation:remove all the digits from the number and it is left with nothing which is 0.
'''



'''
the answer:本题是给定以字符串表示的非负整数，移去其中的k个数字，使得剩下的数字尽可能的小.
本题有两种解法，思路基本相同，如下：
假设有任意一个num,其中任意位置有两个连续的字符数字A和B，比如设为num=****ABCDE****.因为有以下原则,既：位数越高，放越小的数字，整数值越小；
第一种情况当A>B时:
    如删除A产生的数字为num_A=****BCDE*****,如删除B产生的数字为num_B=****ACDE****,由于A>B,所以num_A<num_B,所以这种情况需要删除A；
第二种情况当A<B时:
    这种情况删除A要比删除B产生的数字大，暂时的最优解是****ACDE****,而如果C>B,则删除C为****ABDE****;;则删除C的结果更小，因此这种情况需要不断
的向后找，直到某个字符X大于其后的字符为止，即第一种情况为止，然后将X删除；
    

因此整体解题思路如下：
1.从前到后循环num,直到找到第一个字符X大于其后一个的字符，然后删除X，重复第一个过程，直到删除掉K个元素为止；
2.删除完毕后，如果前面有0需要将0也删除掉；
3.如果此时的结果长度还是大于其本来应该的长度，则表明此时结果中的元素肯定为依次递增，则依次从末尾删除，直至长度为其本应该的长度；


解法1：迭代+栈
1.构建一个栈数据结构st,循环num,如果st不为空，k>0且栈顶元素大于循环当前元素i的话，则弹出栈顶元素，k减1；否则将i压入栈中；
因为这样才能从前到后将最小的元素放在高位.
2.完毕后，删除前面的0，以及看长度是否为diff.返回结果；
代码如下；


解法2：递归
1.构建一个辅助函数helps(num,k),当k为0时直接返回num,然后循环num,如果遇到第一个字符大于其后一个字符的话，则将此字符串删除，
然后更新num,进行递归，同时k减去1；
2.如果循环完毕，都无返回值，则表示num是一个递增字符串，则直接返回num.
3.在主函数中，求出结果后，进行删除前缀0等操作；
代码如下；
'''
#解法1
class Solution:
    def removeKdigits(self,num,k):
        st=[]
        lens=len(num)
        diff=lens-k
        for i in num:
            '''
            不断迭代，将最小的元素向高位移动
            '''
            while(st and k>0 and st[-1]>i):
                st.pop()
                k-=1
            st.append(i)
        while(st and st[0]=='0'):   #将结果前面的0删除
            st.pop(0)
        while(len(st)>diff):    #如果st的长度大于diff,且此时st中的元素都是递增的,所以从后删除
            st.pop()
        return(''.join(st) if(len(st)>0) else '0')  



#解法2
class Solution:
    def removeKdigits(self,num,k):
        lens=len(num)
        diff=lens-k
        res=self.helps(num,k)
        while(len(res)>0 and res[0]=='0'):
            res=res.replace(res[0],'',1)
        while(len(res)>diff):
            res=res.replace(res[-1],'',1)
        return(res if(len(res)>0) else '0')
    
    def helps(self,nums,k):
        if(k==0):
            return(nums)
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                return(self.helps(nums[:i]+nums[i+1:],k-1))
        return(nums)











