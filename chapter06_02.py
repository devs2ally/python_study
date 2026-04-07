# 모듈
# 연관관계가 있는 변수, 함수, 클래스를 모아둔 것의 집합
# 다른 파일에서 내가 필요할 때 가져오는 것
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


# print('-' * 15)
# print('called! inner')
# print(add(5, 15))
# print(substract(5, 15))
# print(multiply(5, 15))
# print(divide(5, 15))
# print(power(5, 15))
# print('-' * 15)


if __name__ == "__main__":
    print('-' * 15)
    print('called! inner')
    print(add(5, 15))
    print(substract(5, 15))
    print(multiply(5, 15))
    print(divide(5, 15))
    print(power(5, 15))
    print('-' * 15)