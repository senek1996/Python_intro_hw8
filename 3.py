# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:47:31 2021

@author: Lenovo
"""

class NotNum(Exception):
    def __init__(self, text):
        self.text=text
    
def checkElem(Elem):
    avai_symb='0123456789-.E+'
    for sym in Elem:
        if sym not in avai_symb:
            raise NotNum('Вы ввели не число')
        
    
l=[]
s=input('Введите число. Для окончания ввода просто введите Enter:')
while s!='':
    try:
        checkElem(s)
        l.append(float(s))
    except:
        print('Я же сказал - введите ЧИСЛО!')
    
    s=input('Введите число. Для окончания ввода просто введите Enter:')
    

print('Введенные числа')
for el in l:
    print(el)