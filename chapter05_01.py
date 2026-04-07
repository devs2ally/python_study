# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lamda)

# 함수 정의 방법
# def function_name(param):
#   code

# 예제1
def first_func(w):
    print("Hello, ", w)
    

# 실행
first_func('sally')


# 예제2
def return_func(w):
    value = "Hello, " + w 
    return value


# 실행
value = 'sally'
return_func(value)
    

# 예제3(다중 반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3


# 실행
x, y, z = func_mul(10)
print(x, y, z)


def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)


# 실행
q = func_mul2(10)
print(type(q), q, list(q))


def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]


# 실행
p = func_mul3(30)
print(type(p), p)


def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {y1, y2, y3}


# 실행
x = func_mul4(30)
print(type(x), x)

# 함수형 프로그래밍, 일반 명령형 프로그래밍 차이 공부 필요


# 딕셔너리
def func_mul5(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}


# 실행
y = func_mul5(40)
print(type(y), y, y.items(), y.keys(), y.get('v2'))


# 중요
# *arg, **kwargs

# *args(언팩킹) : 풀다, 튜플 형태가 넘어올때 사용
def args_func(*args):
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('----')


args_func('Lee')
args_func('Lee', 'Park') # 너가 묶어서 보낸다고 함수는 생각 할거고 함수에 와서 풀어서 자료구조로써 메서드로 사용하게 해줄게
# 즉 하나의 튜플로 간주함, 함수를 유연하게 사용할 때 가변 인자를 사용할 수 있게 하는 별표가 하나 붙은 *args


# kwargs(언팩킹) 딕셔너리 
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('-----')
    

# 언패킹이 아닐 때
f = dict(
    Name1='Lee',
    Name2='qee'
)

kwargs_func(name1='Lee', name2='Kim')


# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)


example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)


# 중첩 함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('in func')
    func_in_func(num + 100)
    
    
nested_func(100)


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화 (효율적으로 메모리 사용)
# 남발 시 가독성 오히려 감소

# def mul_func(x, y):
#     return x * y

# a = lambda x, y: x * y
# a(5, 6)

print('>>>>>>>>>')


# 일반 함수 할당
def mul_func(x, y):
    return x * y


q = mul_func(10, 50)
print(q)


mul_func_var = mul_func
print(mul_func_var(10, 50))
    
    
# 람다 함수 -> 할당    
lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50, 50))


def func_final(x, y, func):
    print(x * y *  func(100, 1000))
    
    
func_final(10, 20, lambda x, y: x * y)