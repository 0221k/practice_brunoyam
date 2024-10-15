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