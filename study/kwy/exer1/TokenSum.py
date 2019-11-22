# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 00:43:01 2019

@author: Owner
"""
str = "1 2 3 4 5".split()
"""
공백을 기준으로 토큰 분리 
"""
i = 0
sum = 0

while i < 5:
    sum += int(str[i])
    i = i+1
print("토큰의 총합=%d"%sum)
    
