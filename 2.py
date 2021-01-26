# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:42:52 2021

@author: Lenovo
"""

class zeroDiv(Exception):
    def __init__(self, text):
        self.text = text
    
def dvd(a,b):
    if b==0:
        raise zeroDiv('Делитель не должен быть равен 0!')
    
    return a/b

a=50
b=20
c=0

print(dvd(a,b))
print(dvd(a,c))