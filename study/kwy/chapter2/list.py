# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:19:15 2019

@author: Owner
"""

a=[1,2,3]
a.append(4)

a.append([5,6])

a= [1,4,3,2]
a.sort()

a = ['a','c','b']
"""
알파벳 오름차순으로 정렬
"""
a.sort()
"""
역순으로 저장
"""
a.reverse()
"""
a 배열안에 해당 데이터가 어느 인덱스에 있는지 조회
"""
print(a.index('a'))

"""
insert
insert(0,4) -> 0번째 인덱스에 4를 삽입
"""
a=[1,2,3]
a.insert(0,4)
"""
remove
"""
a=[1,2,3,1,2,3]
a.remove(3)
a.remove(3)
"""
pop
"""
a=[1,2,3]
a.pop()
a.pop(1) # 첫번쨰 인덱스 삭제

"""
list count
"""
a=[1,2,3,1]
print(a.count(1)) # 데이터 1이 몇개 있는지 카운트

"""
extend
"""
a=[1,2,3]
a.extend([4,5])
b=[6,7]
a.extend(b)


