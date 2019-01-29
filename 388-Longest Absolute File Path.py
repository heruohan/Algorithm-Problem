# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 23:45:22 2019

@author: hecongcong
"""

'''
The problem 388:Longest absolute file path
Suppose we abstract our file system by a string in the following manner:
the string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2
containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2.subdir1 contains a file file1.ext and 
an empty second-level sub-directory subsubdir1.subdirs contains a second-level subsubdir2 containing a file
file2.ext.
we are interested in finding the longest(number of characters)absolute path to a file within our file system.
For example,in the second above example,the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",and its 
length is 32(not including the double quotes).
Given a string representing the file system in the above format,return the length of the longest absolute path to 
file in the abstracted file system.if there is no file in the system,return 0.

Note:
1.The name of file contains at least a '.' and an extension.
2.The name of a directory or sub-directory will not contain a '.'.
Time complexity required:O(n) where n is the size of the input string.
Notice that a/aa/aaa/file1.txt is not the longest file path,if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
'''


'''
The answer:本题的题意是给定一个代表文件系统的字符串input，返回其中最长绝对路径的长度，没有文件的话就返回0.
本题可用三种思路解答,但是核心思想都是动态规划，其解法都是在动态规划思想上的延伸，比如：
input="dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",然后以
'\n'将其分割成字符串列表lst=['dir', '\tsubdir1', '\t\tfile1.ext', '\t\tsubsubdir1', '\tsubdir2', '\t\tsubsubdir2', '\t\t\tfile2.ext'].
然后构建一个相应长度的dp数组：
dp[i]:表示到达lst[i]时，所构成的绝对文件路径的长度；
状态转移方程：统计lst[i]中'\t'的个数count,依次向前寻找比其个数少1的lst[j]所对应的dp[j].既
             dp[i]=dp[j]+len(lst[i].lstrip('\t'))+1,其中j是lst[j]所对应的'\t'个数比lst[i]的
             '\t'少1，且离lst[i]最近的元素的索引；
因为字典中如果key相同的话，可以覆盖前面的key，因此根据状态转移方程的性质，可以用字典代替dp数组;


解法1：
1.构建res,字典m={0:0},start,表示深度的level.
2.循环input,当到最后或者遇到'\n'时，提取字符串tmp,如果'.'在里面的话，证明是个文件，则更新res.
否则，更新深度level，并将其放入字典中;同时，将level初始化为0，start更新为i+1;
3.如果遇见的是'\t',则level加1，start加1；循环完毕后，返回res;
代码如下.


解法2：
1.此种解法和解法1的思路相同，但是是直接将input转化为字符串列表，并循环；
2.然后统计每个字符串中'\t'的个数，既深度；
3.如果'.'在元素里面，则更新res,否则，更新深度并将其放入字典中；循环完毕后返回；
代码如下.


解法3：运用栈数据结构
1.构建一个栈结构st,里面元素为元组，元组里元素分别表示对应元素的深度和绝对文件路径的长度;
2.将input转换为字符串列表，并循环，统计相应元素的深度depth，如果当栈顶元素的深度top_depth>=depth时，
则把栈顶元素删除，直至top_depth+1=depth;
3.然后统计当前元素的绝对文件路径长度lens_sum,然后判断'.'如在当前元素里面，则更新res,否则，
将(depth,lens_sum)压入栈中；
4.直至循环完毕，返回res.
代码如下.

'''
#解法1
class Solution:
    def lengthLongestPath(self,input):
        res=0
        m={0:0}
        start=0
        level=0
        lens=len(input)
        for i in range(lens+1):
            if(i==lens or input[i]=='\n'):
                tmp=input[start:i]
                if('.' in tmp):
                    res=max(res,m[level]+len(tmp))
                else:
                    m[level+1]=m[level]+len(tmp)+1
                level=0
                start=i+1
            elif(input[i]=='\t'):
                level+=1
                start+=1
        return(res)
        

#解法2
class Solution:
    def lengthLongestPath(self,input):
        res=0
        m={0:0}
        for dirs in input.splitlines():
            name=dirs.lstrip('\t')
            depth=len(dirs)-len(name)
            if('.' in name):
                res=max(res,m[depth]+len(name))
            else:
                m[depth+1]=m[depth]+len(name)+1
        return(res)
        

#解法3
class Solution:
    def lengthLongestPath(self,input):
        lens_sum=0
        res=0
        st=[(-1,0)]
        for dirs in input.splitlines():
            depth=dirs.count('\t')
            name=dirs.lstrip('\t')
            top_depth,top_lens=st[-1]
            while(top_depth>=depth):
                st.pop()
                top_depth,top_lens=st[-1]
            lens=len(name)+(depth>0)
            lens_sum=top_lens+lens
            if('.' in name):
                res=max(res,lens_sum)
            else:
                st.append((depth,lens_sum))
        return(res)
        













           
