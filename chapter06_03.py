# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 상대경로 ..(부모 디렉토리),  .(현재 디렉토리) -> 모듈 내부에서만 사용

# 예제1
import sub.sub1.module1
import sub.sub2.module2


# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()


# 예제2
# import 를 쓰면 줄이 길어짐
# 그래서 from 절을 써서 사용할 메서드만 가져오기
# from 뒤에는 파일명
from sub.sub1 import module1
from sub.sub2 import module2 as m2


module1.mod1_test1()
module1.mod1_test2()


m2.mod2_test1()
m2.mod2_test2()


# 예제 3
from sub.sub1 import *  # 사용하지도 않을 거를 다 가져올 필요는 x
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()


module2.mod2_test1()
module2.mod2_test2()


# _pycache는 런타임환경때 파일 빠른 실행을 위해 만들어줌

# __init__.py
# __init__py는 Python 3.3 부터는 없어도 패키지로 인식 
# -> 단, 하위 호환을 위해 작성 추천
# 만들 것들을 누군가에게 줄 때는 버전이 뭔지 모르기 때문에 써줘야 함
# 외부에서 읽어올 때 허가해주는 역할임. 파이썬이 먼저 읽음


# 예제 4
from sub3.chaptor06_04 import test



test