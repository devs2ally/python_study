# while <expr>:
#   <statment(s)>

# 조건에 만족하는동안 계속 반복

# 예제1
n = 5
while n > 0:
    print(n)
    n -= 1

# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop(-1)) # 끝에서 부터
    # print(a.pop(-1))

# 예제3
# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('loop end')

# 예제4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('loop end')

# if 중첩
i = 1
while i <= 10:
    print('i', i)
    if i == 6:
        break
    i += 1

# while - else
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')
    
    
# 예제7
print('>>>>>>>')
i = 0
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print('s not found in list')
    

# 무한 반복
# while True:
#     print('')

# 예제8
a = ['foo', 'bar', 'bax']

while True:
    if not a:  # a가 False라는 것은 비어있다임
        break
    print(a.pop())