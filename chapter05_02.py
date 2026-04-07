# 사용자 입력 (Input)
# input으로 받는건 기본 타입은 무조건 str 이다

# 예제1
name = input("Enter Your name")
grade = input("Enter Your grade")
company = input("Enter Your company")

# print(name, grade, company)


# 예제2
number = input("Enter number : ")
name = input("Enter name : ")

# print("type of number", type(number))
# print("type of name", type(name))

# 예제3
# 계산식을 원할경우 형변환해서 사용하면 된다
f_number = int(input("Enter number1 : "))
s_number = int(input("Enter number2 : "))

total = f_number + s_number
print('first_number + second number : ', total)


# 예제4
float_num = float(input("Enter a float number : "))

print("input float : ", float_num * 3.3254235)
print("input float : ", type(float_num))


# 예제5
print("First Name - {0}, Last Name - {1}".format(
        input("Enter first name : "),
        input("Enter second name : ")
    )
)


# 파이썬 idle에서 인터프리터 바로 실행 가능



