Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 'AAA'
>>> b = 'BBB'
>>> a, b = b, a
>>> a
'BBB'
>>> b
'AAA'
>>> 
>>> 
>>> import turtle
>>> turtle.setheading(90)
>>> #각도는 degree(radian = pi * degree / 180)
>>> 
>>> 
>>> #반복문
>>> #for i in 리스트
>>> #	수행할 문장
>>> for n in [1,2,3,4]
SyntaxError: invalid syntax
>>> for n in [1,2,3,4]:
	print(n)

	
1
2
3
4
>>> 
>>> 
>>> #함수를 만드는 이유
>>> #1. 코드 중복 방지
>>> #2. 동작의 추상화
>>> #def 함수면(매개변수):
>>> #	수행할 문장
>>> #호출보다 정의가 나중에 나오면 안됨
>>> 
>>> 
>>> def sum(a, b):
	return a + b

>>> sum('아', '이')
'아이'
>>> sum(1, 2)
3
>>> 
>>> 
>>> 
>>> turtle.onkey(turtle.forward(20), ' ')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    turtle.onkey(turtle.forward(20), ' ')
  File "<string>", line 5, in forward
turtle.Terminator
>>> 
>>> 
>>> #재귀함수 예시
>>> import turtle as t
>>> ANGLE = 20
>>> MIN_LENGTH = 5
>>> REDUCE_RATE = 0.7
>>> 
>>> def tree(Length):
	t.forward(Length)
	if(Length>MIN_LENGTH):
		sub=length*REDUCE_RATE
		t.left(ANGLE)
		tree(sub)
		t.right(ANGLE)
		tree(sub)
		t.left(ANGLE)
	t.backward(Length)

	
>>> tree(80)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    tree(80)
  File "<pyshell#56>", line 4, in tree
    sub=length*REDUCE_RATE
NameError: name 'length' is not defined
>>> #좀 더 자연스럽게? -> tree1.py ~ tree4.py 참조
>>> #tree4의 random.random()은 0~1.0 사이의 값 리턴, 따라서 if(random.random() < 0.3) 이라고 함은 30%의 확률을 의미함
>>> 
>>> 
>>> #curve.py의 bezier와 numpy는 명령 프롬프트에서 pip install bezier을 하면 설치됨
>>> 