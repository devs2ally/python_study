str4 = "i am python"
str1 = 'python'
str2 = """How are you?"""
str3 = '''Thx'''

print(type(str4), type(str2), type(str3), type(str1))
print(len(str1), len(str2), len(str3), len(str4))

str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프
print('I\'m girl')
print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = "what\'s on TV?"
print(escape_str2)

t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check"
print(t_s1)
print(t_s2)

# Row String 출력
raw1 = r'D:\python\test' # 역슬레시 있는 그대로 표현
print(raw1)

# 멀티라인
# 역슬래시 사용
multi = \
'''
String
Multi
Line
'''
print(multi)

# 문자열 연산
o1 = "python"
o2 = "apple"
o3 = "How are you doning"
o4 = "Seoul Deajeon Busan Jinju"

print(o1 * 3) # 곱하기 연산은 반복되어 출력됨
print(o1 + o2) # 둘 더해서 출력
print('y' in o1) # 있기 떄문에 True
print('d' in o1) # 없기 떄문에 False
print('z' not in o1) # 없기 때문에 True
print()

# 문자열 형변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

# 문자열 함수 upper, isalunm, startswith, count, endswith, isalpha..
print("Capitalize: ", o1.capitalize()) # 첫번째 시작 글자를 대문자로 변경
print('endswith? :', o2.endswith('!')) # 문자열 끝에 !를 붙였는지 확인 False
print('replace :', o1.replace('p', '')) 
print('sorted:' , sorted(o1)) # 리스트로 반환
print('split', o4.split(' ')) # 리스트로 반환

# 반복 (시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) # iter라는게 있음 (반복할 수 있음)

for i in im_str: 
    print(i)
    
print()
# 슬라이싱 연습
str_s1 = "Nice Python"

print(len(str_s1))
print(str_s1[0:3]) # 3-1 까지 나옴 0 1 2 번 나옴
print(str_s1[5:]) # 마지막 기재 안해도 마지막까지 가져옴
print(str_s1[:len(str_s1)]) # str_s1[:11] 끝 부분을 모르겠으면 비워두거나 len함수
print(str_s1[:len(str_s1)-1])
print(str_s1[1:4:2]) # 두칸씩 건너 뛰어서 가져와라. 3번쨰 인수는 건너뛰는 놈
print(str_s1[-5:]) #뒤에서부터 끝까지 -1부터 시작함
print(str_s1[1:-2])
print(str_s1[::2]) # 처음부터 끝까지 두칸 점프
print(str_s1[::-1]) # 음수는 오른쪽에서 왼쪽으로 1칸씩 출력

# 아스키 코드
a = 'z'
print(ord(a)) # 아스키코드로
print(chr(122)) # 문자로


