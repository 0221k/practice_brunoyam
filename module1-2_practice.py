# m1, p1, lvl1

value = (5 + ((7 * 5) / 8)) / (3 ** 5)
print(value)

# m1, p1, lvl2

dist = 109
speed = int(input('speed: '))
time = int(input('hours: '))
print((speed * time) % dist)

# m1, p1, lvl3

num1 = float(input('first number: '))
num2 = float(input('second number: '))
if num1 > num2:
	print(num1)
else:
	print(num2)

# m1, p2, lvl1

first_number = int(input('first number: '))
second_number = int(input('second number: '))
third_number = int(input('third number: '))
if first_number == second_number:
	counter = 2
	if first_number == third_number:
		counter = 3
elif second_number == third_number:
	counter = 2
elif third_number == first_number:
	counter = 2
else:
	counter = 0
print(counter)

# m1, p2, lvl2

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if ((x1 == x2) & (y1 != y2)) or ((x1 != x2) & (y1 == y2)):
	print('YES')
else:
	print('NO')

# m1, p2, lvl3

password = ''
while len(password) < 8:
	password = input()
print(password)
