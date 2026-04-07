# for문
# 파이썬 반복문
# 코딩의 핵심
# for in <collection>
# <Loop body>

for v1 in range(10):
    print(v1)
    
for v2 in range(78, 100):
    print(v2)
    
for v3 in range(1, 11, 3):
    print(v3)
    
sum1 = 0
for v4 in range(4, 1001, 4):
    sum1 += v4
print(sum1)

print(sum(range(1, 1001)))

print(type(range(1, 11)))
print('4의 배수의 합', sum(range(4, 1001, 4)))


# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 딕셔나리, 집합
# iterable 리턴 함수 : range, reverse, enumerate, filter, map, zip

# 예제 1
names = ['kim', 'bob', 'zang', 'lee']

for name in names:
    print('you are : ', name)


# 예제 2
lotto_number = [11, 4, 2, 16, 3, 32]

for item in lotto_number:
    print('current numbers : ', item)


# 예제 3    
word = "Beautiful"

for c in word:
    print(c)

# 예제 4
my_info = dict(
    Name='Lee',
    Age=20,
    City='Seoul'
)

for k in my_info:
    # print('key : ', my_info.get(k))
    print('key : ', my_info[k])
    
for v in my_info.values():
    print('values : ', v)
    
    
# 예제 5
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
        
# break
# 1000명학생에서 100점인 학생을 찾고싶어요
number = [14, 100, 23, 100, 34, 30, 60, 80, 20, 10]
for score in number:
    if score == 100:
        print('found 100')
        break
    else:
        print('not found 100')

# continue
lt = ['1', 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:
        continue
    print("current type is : ", v)
    print("multiply by 2", v * 3)

# for - else
numbers = [14, 100, 23, 100, 34, 30, 60, 80, 20, 10]

for num in numbers:
    if num == 14:
        print("found 14")
        break
else:
    print("not found 14") # 끝까지 찾았지만 14라는 것이 없으면 마지막으로 엘스 실행 break문 없으면 실행

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
    print()
    
# 변환
name2 = 'Aceman'
print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 순서 X
