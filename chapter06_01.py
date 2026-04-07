# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해

# 예제1
# 클래스 : 붕어빵 틀, 인스턴스 : 그 틀을 가지고 코드에서 사용하는 어떤 객체
# 인스턴스가 객체에 포함된다고 볼 수 있음
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재
class Dog:  # object 상속
    # 클래스 속성
    species = 'firstdog'
    
    # 모든 클래스는 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 클래스 정보
print(Dog)


# 인스턴스화
a = Dog("mikky", 2)  # 변수를 활용할 수 있는 대상
b = Dog("baby", 3)


# 비교
print(a == b, id(a), id(b))  # 인스턴스마다 고유 주소를 할당


# 네임 스페이스 : 객체를 인스턴스화 할 때 저장된 공간
print('dog1', a.__dict__)
print('dog2', b.__dict__)


# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))


if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))
    
print(Dog.species)
print(a.species)
print(b.species)


# 예제2
# self의 이해
class SelfTest:
    def func1():
        print('Func1 called')
        
    def func2(self):  # self가 붙으면 인스턴스 메서드
        print(id(self))  # 공통 메서드로도 사용가능
        print('Func2 called')


f = SelfTest()


# print(dir(f))
print(id(f))
# f.func1()  # 예외 :: 매개 변수가 없는데 하나가 넘어옴
f.func2()
SelfTest.func1()  # 바로 클래스로 직접 호출 매개변수가 없기 때문

# SelfTest.func2()  # 예외
SelfTest.func2(f)  # 인스턴스화 시킨 변수를 넣어주면 에러 x

# 즉 클래스로 바로 접근을 해서 호출할 때 self가 없으면 생성한 인스턴스 변수를 넣어주면 되고
# 인스턴스화 시켜서 호출하면 바로 self로 바로 인스턴스 값이 넘어간다


# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0  # 재고
    
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print(user1.stock_num)

# 공유하고 있기때문에 
# 인스턴스 네임스페이스에 stock_num이 없으면
# 클래스 네임스페이스에서 찾아보고 있는 stock_num으로 알아서 가져온다
# 만약 클래스에서도 없다면 에러난다

del user1
print(Warehouse.__dict__)


# 예제4
class Dog:  # object 상속
    # 클래스 속성
    species = 'firstdog'
    
    # 모든 클래스는 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)


# 인스턴스 생성
c = Dog('july', 4)
# 메서드 호출
print(c.info())
# 메서드 호출
print(c.speak('wal wal'))
print(c.speak('mung mung'))