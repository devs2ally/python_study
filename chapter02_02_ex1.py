# 파이썬 3가지 프린트 포멧팅

# \n 개행
# \t 탭
# \\ 문자
# \' 문자
# \" 문자
# \000 널 문자


x = 50
y = 100
text = 308276567
n = 'Lee'

ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x+y))
print(ex1)

ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

ex3 = f'n = {n}, s = {text}, sum = {x+y}'
print(ex3)

# 구분기호
m = 10000000

print(f'm : {m:,}')

# 정렬
# ^ 가운데 정렬
# < 왼쪽 정렬
# > 오른쪽 정렬

astar = '*'
print(f'{astar:*>5}')
print(f'{astar:*^4}')

print(f'{astar:^5}')
print(f'{astar:*<3}')
