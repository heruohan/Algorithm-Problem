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
The answer:本题的题意是给定一个代表文件系统的字符串，返回其中最长绝对路径的长度，没有文件的话就返回0.
本题可用三种思路解答.
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
        













           
