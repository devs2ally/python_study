# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서, 중복, 수정x, 삭제x) 불변


# 선언
a = ()
b = (1, ) # 원소가 하나일때 컴마로 찍어야함, 컴마 없으면 int형
c = (1, 2, 3) 
d = (100, 1000, 'ace', 'base', 'cap')
e = (100, 1000, ('ace', 'base', 'cap'))

# 인덱싱
print('>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', d[-1][1])
print('d - ', list(d[-1][1])) # 리스트 형변환

# 수정 x
# d[0] = 1500 에러 발생

# 슬라이싱
print('>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:])

# 튜플 연산
print('>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
print('>>>>>>>')
a = (5, 1, 3, 2, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언팩킹(Packing, and Unpacking)
t = ('foo', 'bar', 'baz', 'qwe') # 팩킹
print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t # 괄호가 없어도 됨
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3 # 튜플은 괄호가 없어도 됨
t3 = 4,
x1, x2, x3 = t2 # 언패킹 (t2의 첫 번째는 x1에, 두 번째는 x2에...)
x4, x5, x6 = 4, 5, 6 

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)

