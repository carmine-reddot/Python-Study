# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:45:32 2019

@author: Owner
"""

# 튜플 기본 구조
t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4=1,2,3
t5 = ('a','b',('ab','cd'))


t1 = (1,2,'a','b')

print(t1[0])
print(t1[3])

print(t1[1:])#슬라이싱

t2=(3,4)
print(t1+t2) #집합 추가

print(t2*3) #3번 연속 출력
