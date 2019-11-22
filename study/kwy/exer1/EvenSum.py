# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 00:35:47 2019

@author: Owner
"""

sum = 0
num = 1

while num <=10:
    if num%2 == 0:
        sum += num
    num = num+1
print("짝수의 총합=%d"%sum)
