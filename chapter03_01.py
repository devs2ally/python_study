# Chapter03_01

# 숫자형
# 파이썬 지원 자료형
"""
int 정수
float 실수
complex 복소수
bool 불린
str 문자열(시퀀스)
list 리스트(시퀀스)
tuple 튜플(시퀀스)
set 집합
dict 사전
"""

str1 = "python"
bool = False
str2 = 'Anaconda'
float = 1.0
int = 7
list = [str1, str2]
dict = {
    "name" : "dsfsdf"
    , "sdf" : "sdf"
}

tuple = 7, 8, 9
tuple = (21, 4, 23)
set = {1, 2, 3}

print(dict)

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) => 2 ** 3 : x의 y제곱 계산
"""

# 정수 선언
i = 77
i2 = -14
big_int = 77777777777777777777777777777777777777777777777

print(i)
print(i2)
print(big_int)

# 실수
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f, f2, f3, f4)

i1 = 39
i2 = 939
big_int = 752890457982437582375893427589423572
big_int2 = 193024870148901489301284908124
f1 = 1.234
f2 = 3.939


import math

print(math.pi) # 원주율
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수