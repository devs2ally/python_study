# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True)) # 0이 아닌 수, "abc", [1,2,3..]
print(type(False)) # 0, "", [], {}...

# 예1
if False:
    print('good')

if False:
    print('bed')
    
# 예2
if False:
    print('bed')
else:
    print('good')

# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

# 양 변이 같을 때 참
print(x == y)

# 양 변이 다를 때 참
print(x != y)

# 왼쪽이 클때 참
print(x > y)

# 왼쪽이 크거나 같을 때 참
print(x >= y)

# 오른쪽이 클때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y)

city = ""

if city:
    print("You are in:", city)
else:
    print("Please enter your city")
    
city2 = "seoul"
if city2:
    print("You are in:", city2)
else:
    print("Please enter your city")


# 논리 연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and:', a > b and b > c)
print('or:', a > b or b > c)
print('not:', not a > b)
print('not:', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1 :', 3 + 12 > 7 + 3)
print('e2 :', 5 + 10 > 7 + 3 * 20)
print('e3 :', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 :', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

id1 = 'vip'
id2 = 'admin'
grade = 'platinum'


if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')
    
    
# 다중조건문
num = 90
if num >= 90:
    print('A')
elif num >= 80:
    print('B')
elif num >= 70:
    print('C')
else:
    print('F')

# 중첩 조건문
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    elif total >= 70:
        print('장학금 70%')
else:
    print('없음')

# in, not in
q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {
        "name": "Lee",
        "city": "Seoul",
        "grade": "A"
    }
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print('name' in e)
print('Seoul' in e.values())