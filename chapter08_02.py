# 외장 함수
# 종류 os, sys, time, pickle, shutil, temfile, random 등

# 예제1
import sys

print(sys.argv)

# 예제2 (강제 종료)
# sys.exit() # 숏다운

# 예제3 (파이썬 패키지 위치)
print(sys.path)

# pickle : 객체 파일 쓰기 (저장장치에 리스트, 튜플, 오브젝트 등등 저장 하고 싶을떄)
import pickle

# 예제 4
f = open("test.obj", "wb")
obj = {1: "python", 2: "study", 3: "basic"}
pickle.dump(obj, f)
f.close()  # 리소스 반환


f = open("test.obj", "rb")  # 실행되는 위치
data = pickle.load(f)
print(data, type(data))
f.close()


# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), rename

# 예제 6
import os

print(os.environ)
print(os.environ["username"])

# 예제7
print(os.getcwd())

# time : 시간 관련 처리
import time


# 예제 8
print(time.time())

# 예제 9
print(time.localtime(time.time()))

# 예제10
print(time.ctime())

# 예제11(형식 표현)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

# 예제 12(시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(2)


# random : 난수 리턴
import random

# 예제 13
print(random.random())

# 예제 14
print(random.randint(1, 14))
print(random.randrange(1, 45))

# 예제 15
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)


# 예제 16 (무작위 선택)
c = random.choice(d)
print(c)


# webbrrowser : 본인 os의 웹 브라우저 실행

import webbrowser

# webbrowser.open("www.naver.com")
webbrowser.open_new("www.naver.com")
