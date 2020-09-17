Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #pico2d 설치 방법: pip install pico2d 이용
>>> import pico2d
Pico2d is prepared.
>>> pico2d.open_canvas()
>>> pico2d.close_canvas()
>>> import pico2d as p
>>> p.open_canvas()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    p.open_canvas()
  File "C:\Users\user\AppData\Local\Programs\Python\Python38\lib\site-packages\pico2d\pico2d.py", line 50, in open_canvas
    SDL_Init(SDL_INIT_EVERYTHING)
OSError: exception: access violation reading 0x0000000000001F2C
>>> #팁: 모듈에서 특정 함수만 쓰는 법
>>> from random import randint
>>> randing(1, 6)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    randing(1, 6)
NameError: name 'randing' is not defined
>>> randint(1,6)
1
>>> from pico2d import *
>>> open_canvas()
>>> close_canvas()
>>> import os
>>> os.getcwd()
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38'
>>> #프로그램의 실행 위치
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python38.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
>>> #그 위치에 있는 파일들
>>> open_canvas()
>>> image = load image('C:/Users/user/Desktop/2주차/cat.jpg')
SyntaxError: invalid syntax
>>> image = load_image('C:/Users/user/Desktop/2주차/cat.jpg')
>>> image.draw_now(400, 300)
>>> #하지만 절대경로는 좋지 않음
>>> os.getcwd()
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38'
>>> os.chdir('C:/Users/user/Desktop/2주차/cat.jpg')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    os.chdir('C:/Users/user/Desktop/2주차/cat.jpg')
NotADirectoryError: [WinError 267] 디렉터리 이름이 올바르지 않습니다: 'C:/Users/user/Desktop/2주차/cat.jpg'
>>> os.chdir('C:/Users/user/Desktop/2주차/')
>>> os.listdir
<built-in function listdir>
>>> image = load_image('cat.jpg')
>>> close_canvas()
>>> #혹은 cat.py 참조
>>> 
>>> open_canvas()
>>> show_lattice()
>>> hide_lattice()
>>> imgae = load_image('C:/Users/user/Desktop/2주차/character.png')
>>> image = load_image('character.png')
>>> image.draw_now(300, 200)
>>> show_lattice()
>>> imgae.draw_now(300, 200)
>>> #좌표 (300, 200)에 캐릭터가 그려짐
>>> clear_canvas_now()
>>> for y in range(100, 501, 80):
	for x in range(100, 701, 35):
		image.draw_now(x, y)

		
>>> clear_canvas_now()
>>> for y in range(100, 501, 50):
	for x in range(100, 701, 20):
		image.draw_now(x, y)

		
>>> #나중에 그려진 것이 위에 덧씌워짐
>>> grass = load_image('grass.png')
>>> grass.draw_now(400, 90)
>>> close_canvas()
>>> 
================ RESTART: C:/Users/user/Desktop/2주차/2주차 2차시_2.py ===============
Pico2d is prepared.
#그런데 반짝이는 문제점이 발생
#-> 더블 버퍼링으로 해결
