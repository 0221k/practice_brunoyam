# m3 p1 lvl1

account_value = float(input())
annual_rate = int(input())
target_value = int(input())

def years_calculation(x, p, y):
	calculations = [account_value, 0]
	while calculations[0] < y:
		calculations[0] += (x / 100) * p
		calculations[0] = round(calculations[0])
		calculations[1] += 1
	return calculations[1]

print(years_calculation(account_value, annual_rate, target_value))

# m3 p1 lvl2

repeat_number = int(input())

while repeat_number > 0:
	print('for is a special case for the while loop')
	repeat_number -= 1

# m3 p1 lvl3

integer_lst = list(input())
for i in range(0, len(integer_lst)):
	integer_lst[i] = int(integer_lst[i])
print(sum(integer_lst))

# m3 p2 lvl1

l = [1, 4, 1, 6, "hello", "a", 5, "hello"]

def double_items(lst):
	l_counter = []
	l_doubles = []
	for i in lst:
		if i in l_counter and i not in l_doubles:
			l_doubles.append(i)
		else:
			l_counter.append(i)
	print(l_doubles)

double_items(l)

# m3 p2 lvl2

from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
print(m)

def max_in_matrix(lst):
	max_value = 0
	for i in m:
		if max(i) > max_value:
			max_value = max(i)
	print(max_value)

max_in_matrix(m)

# m3 p2 lvl3

d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}

def swap_pairs(dictionary):
	swap_dict = {}
	for key, value in dictionary.items():
		swap_dict[value] = key
	return swap_dict

d = swap_pairs(d)
print(d)

# m3 p3 lvl1

import math

def area(a, b, c):
	p = (a + b + c) / 2
	return math.sqrt(p * (p - a) * (p - b) * (p - c))

print(round(area(2, 3, 4), 3)) # 2.905

# m3 p3 lvl2

s = '''It was just cloudy, 
blowing from the north. gray. - swim!'''

def less_than_five(str):
	split_words = str.split()
	result = []
	for i in split_words:
		if len(i) < 5 and i.isalpha():
			result.append(i)
		elif len(i) < 6 and (i.endswith(',') or i.endswith('.') or i.endswith('!')):
			result.append(i.replace(',', '').replace('.', '').replace('!', ''))
	return result

print(less_than_five(s))

# m3 p3 lvl3

lst_number = [56, 9, 11, 2]
lst_string = list(map(str, lst_number))

def max_sort(lst):
	result = ''
	for i in range(9, -1, -1):
		for j in lst:
			if j[0] == str(i):
				result += j
				lst.remove(j)
	return result

print(max_sort(lst_string))

# m3 p4 lvl1-lvl2

import json

def save_data(login, password):
	login_details = {login:password}
	with open('testjson.json', 'r') as f:
		login_details1 = json.load(f)
	for i in login_details:
		if (i not in login_details1.keys()) and (i not in login_details1.values()):
			with open('testjson.json', 'w') as f:
				json.dump(login_details, f)
		else:
			print('Login is taken')

save_data(input('Enter login: '),input('Enter password: '))

# m3 p4 lvl3

import json

def login_function(login, password):
	login_details = {login:password}
	with open('testjson.json', 'r') as f:
		login_details1 = json.load(f)
	if login_details == login_details1:
		print('Succesful login!')
	else:
		print('Wrong login or password')

login_function(input('Enter login: '),input('Enter password: '))