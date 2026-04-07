# 파이썬 내장 함수(Built-in)
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절대값
# abs()

print(abs(-3))


# all, any : iterable 요소 검사(참, 거짓)
print(all([1, 2, 2]))  # and 빈문자열, 공백일 경우 false
print(any([1, 2, 0]))  # or


# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(44))
print(ord("c"))


# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(["abc", "bcd", "efg"]):
    print(i + 1, name)


# filter 함수 (여과) : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2


print(list(filter(conv_pos, [1, -3, 2, 0, -1, 6])))

print(list(filter(lambda x: abs(x) > 2, [1, 3, 2, -1, 0, 2])))

# id : 객체의 주소값(레퍼런스) 반환

print(id(int(5)))
print(id(4))

# len : 요소의 길이 반환
print(len("absdfsf"))
print(len([1, 2, 3, 4, 5, 5]))

# max, min : 최댓값, 최소값
print(">>>>>>>")
print(max([1, 2, 3]))
print(max("python study"))
print(min([1, 2, 3]))
print(min("python study"))  # 최소값은 공백


# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)


print(list(map(conv_abs, [1, -2, 3, 0, 1])))
print(list(map(lambda x: abs(x), [1, -2, 3, 0, 1])))


# pow : 제곱값 반환
print(pow(2, 10))  # 2를 10번 곱한 것


# range : 반복가능한 객체 반환
print(list(range(1, 9, 2)))
print(list(range(0, -15, -1)))

# round : 반올림
print(round(5.375, 2))  # 소숫점 두번째까지 반올림해라

# sorted : 반복가능한 객체(Iterable)를 정렬 후 반환
print(sorted([6, 7, 8, 1, 2, 3]))
print(sorted(["p", "y", "t", "h", "o", "n"]))

# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6, 7, 8, 9, 19]))
print(sum(range(1, 101)))

# type : 자료형 확인
print(type(3))
print(type({3, 4}))
print(type((1, 2)))
print(type([1, 2]))


# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10, 20, 30], [40, 50])))  # 짝이 맞는 것만 반환
print(type(list(zip([10, 20, 30], [40, 50, 777]))[0]))  # 튜플로 반환
