# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:55:54 2018

@author: hecongcong
"""

class Solution:
    def isValidSerialization(self,preorder):
        preorder=preorder.split(',')
        if(preorder==['#']):
            return(True)
        if(preorder[0]=='#'):
            return(False)
        s=[preorder[0]]
        for i in range(1,len(preorder)):
            if(s[0]=='#'):
                return(False)
            if(preorder[i]=='#'):
                while(s and s[-1]=='#'):
                    s.pop()
                    s.pop()
            s.append(preorder[i])
        return(True if(s==['#']) else False)
        
                           
                           
        
                          
                          
                   
               
                
           
           
                      
                      

        
             
    
    

                                