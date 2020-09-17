Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "Hello"
>>> s
'Hello'
>>> d = 'Hello'
>>> d
'Hello'
>>> s == d
True
>>> s = "Hello \"Dave\""
>>> s
'Hello "Dave"'
>>> d = 'Hello "Dave"'
>>> d
'Hello "Dave"'
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = 10.0
>>> type(a)
<class 'float'>
>>> a = 10>3
>>> type(a)
<class 'bool'>
>>> first = "Hello"
>>> last = "World"
>>> first + last
'HelloWorld'
>>> first * 5
'HelloHelloHelloHelloHello'
>>> first[0]
'H'
>>> first[-1]
'o'
>>> first[0:4]
'Hell'
>>> first(0:4]
SyntaxError: invalid syntax
>>> #[inclusive - exclusive] 즉, [는 포함, (는 미포함
>>> twice = ['a', 'b', 'c']
>>> #List
>>> 
>>> score = {'a' : 1, 'b' : 2, 'c' : 3}
>>> #Dict
>>> 
>>> #List는 indes-value, Dict는 key-value
>>> 
>>> t1 = (1,2,3)
>>> #Tuple
>>> (x, y, z) = t1
>>> x
1
>>> y
2
>>> z
3
>>> pos = 10, 20
>>> #turtle.goto(pos) X, turtle.goto(*pos) O
>>> 
>>> s1 = { 'a1', 'a2', 'a3' }
>>> #Set
>>> s1 | {'a4'}
{'a4', 'a1', 'a2', 'a3'}
>>> 
>>> 
>>> #Turtle Graphics
>>> import turtle
>>> turtle
<module 'turtle' from 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38\\lib\\turtle.py'>
>>> turtle.forward(100)
>>> turtle.reset()
>>> turtle.shape('turtle')
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.reset()
>>> for i in range(4):
	turtle.forward(100)
	turtle.left(90)

	
>>> 
>>> turtle.reset()
>>> turtle.speed(10)
>>> #import turtle 수행 후 여러 함수 사용 가능
>>> turtle.circle(200)
>>> turtle.right(90)
>>> turtle.circle(200)
>>> turtle.undo()
>>> turtle.goto(100,100)
>>> #머리 방향은 고정, 시작점이 (0,0)
>>> #x 오른쪽으로 증가, y 위로 증가 : pico2d
>>> turtle.reset()
>>> turtle.forward(50)
>>> turtle.penup()
>>> turtle.forward(50)
>>> turtle.pendown()
>>> turtle.forward(50)
>>> #File - New File을 이용하면 >>> 없이 프로그래밍 가능
>>> 
>>> 
>>> #random
>>> import random
>>> random
<module 'random' from 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38\\lib\\random.py'>
>>> random.randint(1,6)
5
>>> random.randint(1,6)
4
>>> random.randint(1,6)
5
>>> random.randint(1,6)
2
>>> random.uniform(10,20)
10.000031835669628
>>> random.uniform(10,20)
18.073706942414656
>>> m = input("Enter hour:")
Enter hour:4
>>> m
'4'
>>> m*4
'4444'
>>> #input의 리턴값이 문자열 형태이므로 이런 결과가 나옴
>>> type(m)
<class 'str'>
>>> mm=int(m)
>>> m*4
'4444'
>>> mm*4
16
>>> type(mm)
<class 'int'>
>>> "KOREA" == "korea"
False
>>> "abcdefg" == 'abcdefg'
True
>>> #조건문
>>> if(mm>10):
	big

	
>>> if(mm<10):
	big

	
Traceback (most recent call last):
  File "<pyshell#105>", line 2, in <module>
    big
NameError: name 'big' is not defined
>>> if(mm<10):
	"big"

	
'big'
>>> #C언어에서의 elseif는 python에서 elif로 사용
>>> 