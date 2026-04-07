# function
# 함수란?
# 파이썬 함수 쌩기초

# 함수
# 프로그래머가 이름을 통해서 정의 후 필요할 때 마다 호출
# 반복 되는 코드를 한 번 구현 후 재사용 가능한 코드의 집합
# 함수 구현 -> 재사용, 루틴(프로시저, 서브루틴)

# 종류
# 1. 매개변수가 필요한 함수
# 2. 매개변수가 필요하지 않은 함수
# 3. 결과값을 반환하는 함수(return)
# 4. 결과값을 반환하지 않는 함수

# 예제1 - 매개변수가 필요하지 않은 함수
def function1():
    print('예제 1 호출')
    
    
# 실행
function1()


# 예제2 - 매개변수 필요한 함수
def function2(a, b):
    print('예제 호출', a, b)
    
    
# 실행
function2(1, 2)


# 예제3 - 결과값 반환 x
def function3(x, y):
    print('예제 3 호출', x, y)
    
    
# 실행
function3(100, 200)


# 예제4 - 결과값 반환
def function4(x, y):
    return x + y
    
    
# 실행
r = function4(50, 50)
print(r)