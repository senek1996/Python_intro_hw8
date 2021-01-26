# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 00:01:36 2021

@author: Lenovo
"""

class CompNum:
    
    def __init__(self,re,im):
        self.re=re
        self.im=im
    
    def __add__(self,b):
        return(CompNum(self.re+b.re,self.im+b.im))
    
    def __mul__(self,b):
        return(CompNum(self.re*b.re-self.im*b.im,self.re*b.im+self.im*b.re))
    
    def __str__(self):
        return(str(self.re)+" + "+str(self.im)+"i")
    
a=CompNum(5,5)
b=CompNum(3,7)
c=a+b
d=a*b
print(c)
print(d)