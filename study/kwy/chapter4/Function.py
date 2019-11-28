# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 23:20:18 2019

@author: wykim
"""
#입력값이 없는 함수

def say():
    return 'Hi'

a = say()
print(a)

# 결과값이 없는 함수
def sum(a,b):
    print("%d, %d의 합은 %d입니다"%(a,b,a+b))
    
# 여러 개의 입력값을 받는 함수 만들기
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

result = sum_many(1,2,3)
print(result)

result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)

#입력 인수에 초깃값 미리 설정하기
def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다"% name)
    print("나이는 %d살입니다"%old)
    
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
        
# global 명령어 이용하기
a=1
def vartest():
    global a
    a=a+1
vartest()
print(a)
