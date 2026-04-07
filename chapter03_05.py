# 파이썬 딕셔너리
# 범용적 가장 많이 사용
# 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {
        'name': 'kim'
        , 'phone': '01033337777'
        , 'birth': '951202'
    }
b = {0: 'hello python'}
c = {'arr': [1, 2, 3, 4]}
d = {
        'name': 'lee'
        , 'city': 'Seoul'
        , 'age': '32'
        , 'grade': 'A'
        , 'status': True
    }

e = dict([
    ('name', 'lee')
    , ('city', 'Seoul')
    , ('age', 32)
    , ('grade', 'A')
    , ('status', True)
])

f = dict(
    Name='Niceman'
    , City='Seoul'
    , Age=33
    , Grade='A'
    , Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

print('a - ', a['name'])  # key가 없으면 에러가 뜸 속성 접근
print('a - ', a.get('name'))  # key가 없을 때는 None으로 뜬다. get을 많이 사용함
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))


# 딕셔너리 길이
a['name'] = 'Seoul' # 동적 수정 가능
print('a : ', a)
a['rank'] = [1, 2, 3]
print('a - ', len(a))
print('a - ', len(b))

# dict_keys, dict_values, dict_items : 반복문 (__iter__) 에서 사용 가능

print('a - ', list(a.keys())) # 리스트로 형변환 가능
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print()

print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', d.values())

print()

print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', d.items())

print()

print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem()) # 무작위로 꺼내옴
print('f - ', f)

print()

print('a - ', 'birth' in a)
print('d - ', 'city2' in d)
print('d - ', 'city2' not in d)

# 수정
a['test'] = 'test_dict'
print(a)

a['address'] = 'dj'
print(a)

a.update(birth='333333')
print(a)

tmp = {'address' : 'Busan'}
a.update(tmp)
print(a)