#직선 운동의 쉬운 예시
x += dx
y += dy

#곡선 운동(점프)의 쉬운 예시
dy = 100
y += dy
dy -= 10

#리스트를 빠르게 만들기 위한 독특한 문법 구조
numbers = [n for n in range(1, 10)]
numbers = [n for n in range(1, 10 + 1) if n % 2 == 0]
numbers = [n * 3 for n in range(1, 10)]
