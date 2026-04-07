# 배열 List
# 순서, 중복, 수정, 삭제 가능

#선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'a', 'b']
e = [1000, 10000, d]
f = [21.42, False, 'dfsdf', 3.14]
g = [1000, 10000, ['ace', 'cap']]

# 인덱싱
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1])
print('e - ', e[-1][2])
print('g - ', g[-1][1])
print('list - ', list(g[-1][1]))

# 슬라이싱
print('>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[-1][1:3])

# 리스트 연산
print('>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'test' + c[0]", 'Test' + str(c[0])) #문자+숫자 에러남 형변환 필요

# 값 비교
print(c == c[:3] + c[3:])

# id
tmp = c
print(id(tmp) == id(c)) # 둘 다 같은 주소를 가지고 있음, 한쪽에서 값을 지우면 tmp도 지워짐

# 리스트 수정, 삭제
print('>>>>>>>')
c[0] = 4
c[1:2] = ['a', 'b', 'c'] # 슬라이싱을 했을 때는 원소가 들어감
print('c - ', c)
c[1] = ['a', 'b', 'c'] # 슬라이싱 안 할 경우 리스트가 들어감 중첩리스트
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2]
print('c - ', c)

# 리스트 함수
print('>>>>>>>')
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(10)
print('a - ', a)
a.sort() 
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7) # 위치, 넣을것
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[] 데이터 개수 적을 때
a.remove(10) # 원소 삭제
print('a - ', a)
a.pop() # 기존 리스트 끝 원소 제거
print('a - ', a)
a.pop()  # 기존 리스트 끝 원소 제거
print('a - ', a)
print('a - ', a.count('apple')) # 찾는 값이 몇개인지
ex = [8, 9]
a.extend(ex)
print('a - ', a)  

# 삭제 : remove, pop, del

# 반복문

while a:
    data = a.pop()
    print(data)
    print(a)