# 모듈 사용 실습
import sys

print(sys)


# 환경변수에 파이썬 패스에 추가해줘야 등록
# 파이썬 패스에 영구적으로 등록
print(sys.path)

print(type(sys.path))

# sys.path.append('C:/Users/DKSYSTEMS/Desktop/Project/777.project/python_study/math')

# print(sys.path)

import chapter06_02


print(chapter06_02.power(3, 11))


# 불필요한 것들이 출력이 될 때는 __main__ 사용
