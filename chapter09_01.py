# 파일 읽기 및 쓰기

# 읽기 모드 : r
# 쓰기모드 w
# 추가 모드 a
# 텍스트 t
# 바이너리 b
# 상대 경로('../, ./'), 절대 경로 ('C:\..')

# 절대 경로
# f = open(
#     "C:\\Users\\DKSYSTEMS\\Desktop\\Project\\777.project\\python_study\\source_code\\resource"
# )


# 파일 읽기
# 상대 경로
f = open("./resource/it_news.txt", "r", encoding="UTF-8")

# 속성 확인
print(dir(f))

# 인코딩 확인
print(f.encoding)

# 파일 이름
print(f.name)

# 모드 확인
cts = f.read()
print(cts)

# 반드시 close
f.close()


# 예제2
with open("./resource/it_news.txt", "r", encoding="UTF-8") as f:
    c = f.read()
    print(iter(c))
    print(list(c))

print()


# 예제3
# read() : 전체 읽기, read(10) : 10Byte
with open("./resource/it_news.txt", "r", encoding="UTF-8") as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    # 커서 : 자기가 어디까지 읽었는지 기억함 (내부적으로 동작)
    f.seek(0, 0)  # 처음으로 돌아감 from, to
    c = f.read(20)
    print(c)

print()

# 예제4
# readline 한줄 한줄(개행이 되기 전까지) 읽어오는것
with open("./resource/it_news.txt", "r", encoding="UTF-8") as f:
    c = f.readline()
    print(c)

print()


# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open("./resource/it_news.txt", "r", encoding="UTF-8") as f:
    c = f.readlines()  # 줄바꿈 공백은 정규표현식이용
    print(c)
    for c in cts:
        print(c, end="")  # 다시 원문으로

print()


# 파일 쓰기(write)

# 예제1
with open("./resource/contents1.txt", "w") as f:
    f.write("i love python\n")


# 예제2
with open("./resource/contents1.txt", "a") as f:
    f.write("i love python2\n")

# 예제3
with open("./resource/contents2.txt", "a") as f:
    list = ["Orange\n", "Apple\n", "Banana\n"]
    f.writelines(list)

# 예제4
with open("./resource/contents2.txt", "a") as f:
    print("Test Text Write!", file=f)
    print("Test Text Write!", file=f)
    print("Test Text Write!", file=f)
# 프린트문에 파일 인자를 넣어서 오픈함수 인자랑 연결해주게 되면 파일로 직접 출력

#
