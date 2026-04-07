# 집합 자료형()
# set
# 순서x, 중복x

# 선언
a = set()
b = set([1, 2, 3, 4, 4, 4, 4])
c = set([1, 4, 6, 8])
d = set([1, 2, 'pen', 'cap', 'plan'])
e = {'foo', 'bar'} # 리스트 처럼 나열하는건 딕셔너리x 셋임
f = {42, 'foo', (1, 2, 3), 3.1323}

print('a - ', type(a), a)
print('a - ', type(b), b)
print('a - ', type(c), c)
print('a - ', type(d), list(c))
print('a - ', type(e), list(e))
print('a - ', type(f), tuple(f))

# 튜플 변환
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# list 변환
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 - ', l2)

print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2) # 교집합
print('s1 & s2 : ', s1.intersection(s2)) # 교집합

print('s1 | s2 : ', s1 | s2) # 합집합
print('s1 | s2 : ', s1.union(s2)) # 합집합

# s1 - s2
print('s1 - s2 : ', s1 - s2) # 차집합
print('s1 - s2 : ', s1.difference(s2)) # 차집합

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # 교집합이 있으면 Fasle, 없으면 True

# 부분 집합 확인
print('subset', s1.issubset(s2)) # s1이 s2의 부분집합이냐 
print('superset', s1.issuperset(s2)) # s1이 s2에 포함이 되는거냐

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print(s1)
s1.remove(5) # 예외 발생 :: 원소가 없으면 에러남 있는지 코드 먼저 짜고 써야함
print(s1) 
s1.discard(3)
print(s1)
s1.discard(7) # 예외 발생 안 함!
print(s1)

s1.clear();
print(s1) # 전부 제거