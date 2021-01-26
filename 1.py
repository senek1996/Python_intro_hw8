# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:43:20 2021

@author: Lenovo
"""

#не работает, но разработана логика

class Date():
    
    days_1=[31,28,31,30,31,30,31,31,30,31,30,31]
    days_4=[31,29,31,30,31,30,31,31,30,31,30,31]
    
    def __init__(self,s):
        self.day=s[:2]
        self.month=s[3:5]
        self.year=s[6:]
    
    @classmethod
    def toNum(cls):
        cls.day=int(cls.day)
        cls.month=int(cls.month)
        cls.year=int(cls.year)
    
    @staticmethod
    def valiDate(self):
        if self.month>=1 and self.month<=12:
            if self.year%4==0: #високосный год
                if self.day>=1 and self.day<=self.days_4[self.month-1]:
                    print("Дата корректная")
                else:
                    print("Некорректный день")
            else:
                if self.day>=1 and self.day<=self.days_1[self.month-1]:
                    print("Дата корректная")
                else:
                    print("Некорректный день")
                
            
        else:
            print("Некорректный месяц")
    
d=Date('04-05-2014')
d.toNum() #преобразование в числа
Date.valiDate(d)