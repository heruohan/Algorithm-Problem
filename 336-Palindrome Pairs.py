# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:12:48 2018

@author: hecongcong
"""
class Solution:    
    def isPalindrome(self,word,left,right):
        while(left<right):
            if(word[left]!=word[right]):
                return(False)
            left+=1
            right-=1
        return(True)
       
    def palindromePairs(self,words):
        res=[]
        tab={}
        lens_set=set()
        for i in range(len(words)):
            tab[words[i]]=i
            lens_set.add(len(words[i]))
        for i in range(len(words)):
            lens=len(words[i])
            word=words[i][::-1]
            if((word in tab) and (tab[word]!=i)):
                res.append([i,tab[word]])
            for j in lens_set:
                if(j<lens):
                    if(self.isPalindrome(word,0,lens-j-1) and \
                       (word[lens-j:] in tab)):
                        res.append([i,tab[word[lens-j:]]])
                    if(self.isPalindrome(word,j,lens-1) and \
                       (word[:j] in tab)):
                        res.append([tab[word[:j]],i])
                        
        return(res)
    
            
            
            
            
            
            
            
            
            
            
            
            
            