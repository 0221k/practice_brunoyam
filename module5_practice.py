# m5 p1 lvl1

class StringVar:

	def __init__(self, string_var = None):
		self.string_var = string_var

	def set(self, new_string):
		self.string_var = new_string

	def get(self):
		return self.string_var

sv1 = StringVar()
sv2 = StringVar('Hi, world')
print(sv1.get())			# None
print(sv2.get())			# Hi, world
sv1.set('Hello, world!')
print(sv1.get())			# Hello, world!
sv1.set(sv2.get())
print(sv1.get())			# Hi, world
sv1.set('Goodbye, world')
print(sv1.get())			# Goodbye, world

# m5 p1 lvl2

class Point:

	def __init__(self, x = 0, y = 0):
		self.x, self.y = x, y

	def middle_of(self, other):
		middle_x = round((self.x + other.x) / 2)
		middle_y = round((self.y + other.y) / 2)
		return Point(middle_x, middle_y)

	def string_points(self):
		return f'x = {self.x} y = {self.y}'

	def step(self, other):
		self.x, self.y = other.x, other.y

p1 = Point(10, 10)
p2 = Point(5, 20)
print(p1.string_points())	# x = 10 y = 10
print(p2.string_points())	# x = 5 y = 20
p3 = p1.middle_of(p2)
print(p3.string_points())	# x = 8 y = 15
p1.step(p3)
print(p1.string_points())	# x = 8 y = 15

#m3 p1 lvl3

from random import randint

class Warrior:
	
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.armor = 100
		self.stamina = 100

	def attack(self, other, other_action):
		if other_action == True:
			if self.stamina > 0:
				if other.stamina <= 0:
					self.health -= randint(0, 10)
					other.stamina = 0
				else:
					self.health -= randint(10, 30)
					other.stamina -= randint(10, 30)
				self.stamina -= randint(0, 10)
			else:
				if other.stamina <= 0:
					self.health -= randint(0, 10)
					other.health -= randint(0, 10)
					other.stamina = 0
				else:
					self.health -= randint(10, 30)
					other.health -= randint(0, 10)
					other.stamina -= randint(10, 30)
				self.stamina = 0

			print(f'{self.name} attacked. \t{other.name} has {other.health} health')
			print(f'{other.name} attacked. \t{self.name} has {self.health} health')

	def defend(self, other, other_action):
		if other_action == True:
			if self.armor > 0:					
				self.health -= randint(0, 20)
				self.armor -= randint(0, 10)
				other.stamina -= 10
			else:
				self.health -= randint(10, 30)
				self.armor = 0
				other.stamina -= 10
			print(f'\n{other.name} attacked. \t{self.name} has {self.health} health\n')

w1 = Warrior('Conor')
w2 = Warrior('Khabib')
warriors_list = [w1, w2]

def start_battle(w_arr):
	if w_arr[0].health > 10 and w_arr[1].health > 10:
		warrior1_attack = randint(0, 1) == 1
		warrior2_attack = randint(0, 1) == 1
		battle(w_arr, warrior1_attack, warrior2_attack)
	else:
		if w_arr[0].health <= 10:
			finish_him = print(f'Finish {w_arr[0].name}? y/n: ') # input
			print(f'{w_arr[1].name} won')
		else:
			finish_him = print(f'Finish {w_arr[1].name}? y/n: ') # input
			print(f'{w_arr[0].name} won')


def battle(w_arr, warr1_attack, warr2_attack): # Рекурсия
	if warr1_attack == True and warr2_attack == True:
		w_arr[0].attack(w_arr[1], warr2_attack)
	elif warr1_attack == True and warr2_attack == False:
		w_arr[1].defend(w_arr[0], warr1_attack)
	elif warr2_attack == True and warr1_attack == False:
		w_arr[0].defend(w_arr[1], warr2_attack)
	start_battle(w_arr)

start_battle(warriors_list)
print(w1.__dict__)
print(w2.__dict__)

# m3 p2 lvl1

import json

class CarModel:

	def __init__(self, brand = None,  wheels = None, doors = None, engine = None):
		self.brand = brand
		self.wheels = wheels
		self.doors = doors
		self.engine = engine

	def save(self):
		attributes_dict = self.__dict__

		with open('testjson.json', 'w') as f:
				json.dump(attributes_dict, f)

cm1 = CarModel('Honda', 4, 2, 'v8')
cm1.save()		# {"brand": "Honda", "wheels": 4, "doors": 2, "engine": "v8"}