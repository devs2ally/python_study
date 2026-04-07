# 운영 환경에서 발생, 하드웨어적 에러
# 의도한 대로 동작하지 않을 경우
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)에서 발생하는 예외 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다
# 3. 예외는 던져진다
# 4. 예외 무시


# SyntaxError
# print('df)
# print(""dfsdf")
# if True
#     pass


# Nameerror : 참조 없음
a = 10
b = 10
# print(c)


# ZeroDvisionError
# print(100 / 0)


# IndexError
x = [50, 70, 90]
# print(x[1])
# print(x[4])
# print(x.pop())
# print(x.pop())
# print(x.pop())


# KeyError
dic = {"name": "Lee", "Age": 41}
# print(dic['hobby'])
# print(dic.get('babo'))

# 예외가 없는 것을 가정하고 프로그램 작성 ->
# 런타임 예외 발생 시 예외 처리 권장(EAFP)


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())


# ValueError
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)


# FileNotFoundError

# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
x = [1, 2]
y = 1, 2
z = "test"

# print(x + y)
# print(x + z)
# print(z + y)

# print(x + list(y))
# print(x + list(z))

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except : 에러명1: 여러개 가능
# except : 에러명2:
# else : try 블록의 에러가 없을 경우 실행
# final : 항상 마지막에 실행한다

name = ["Kim", "Lee", "Park"]


# 예제1
# try:
#     z = "Kim2"
#     x = name.index(z)
#     print("{} Found it! {} in name".format(z, x + 1))
# except ValueError:
#     print("Not found it")
# else:
#     print("Ok! else")
#
# print()


# 예제2
# try:
#     z = "Kim2"
#     x = name.index(z)
#     print("{} Found it! {} in name".format(z, x + 1))
# except (
#     Exception
# ) as e:  # 모든 예외 클래스 부모 (어떤 에러 발생 예측 불가), 에일리어스 가능
#     print(e)
#     print("Not found it")
# else:
#     print("Ok! else")
# finally:
#     print("finally")

# print()


# 예제 3
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = "Park"
    if a == "Kim":
        print("pass")
    else:
        raise ValueError  # 직접 설계한 예외 발생시 raise사용
except ValueError:
    print("Occurred!")
else:
    print("else")
