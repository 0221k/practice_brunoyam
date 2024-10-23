import sqlite3
from peewee import *

## p8 p1 lvl1-2

conn = sqlite3.connect('mod8testdb.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Students 
	(s_id int, name Varchar(16), surname Varchar(16), age int, city Varchar(8))''')

cursor.execute('''CREATE TABLE Courses 
	(c_id int, name Varchar(16), time_start datetime, time_end datetime)''')

cursor.execute('''CREATE TABLE Student_courses (student_id int, course_id int, 
		PRIMARY KEY (student_id, course_id), 
		FOREIGN KEY (student_id) REFERENCES Students (s_id), 
		FOREIGN KEY (course_id) REFERENCES Courses (c_id))''')

cursor.executemany('''INSERT INTO Courses 
	VALUES (?, ?, ?, ?)''', [
	(1, 'python', '2021-07-21', '2021-08-21'), 
	(2, 'java', '2021-07-13', '2021-08-16')])

cursor.executemany('''INSERT INTO Students 
	VALUES (?, ?, ?, ?, ?)''', [
	(1, 'Max', 'Brooks', 24, 'Spb'), 
	(2, 'John', 'Stones', 15, 'Spb'), 
	(3, 'Andy', 'Wings', 45, 'Manhester'), 
	(4, 'Kate', 'Brooks', 34, 'Spb')])

cursor.executemany('''INSERT INTO Student_courses 
	VALUES (?, ?)''', [(1, 1), (2, 1), (3, 1), (4, 2)])

conn.commit()

cursor.execute('''SELECT Students.name FROM Students WHERE Students.age > 30''')
print(cursor.fetchall())	# [('Andy',), ('Kate',)]

cursor.execute('''SELECT Students.name FROM Students 
	JOIN Student_courses ON Students.s_id = Student_courses.student_id 
	JOIN Courses ON Student_courses.course_id = Courses.c_id
	WHERE Courses.name = 'python' ''')
print(cursor.fetchall())	# [('Max',), ('John',), ('Andy',)]

cursor.execute('''SELECT Students.name FROM Students 
	JOIN Student_courses ON Students.s_id = Student_courses.student_id 
	JOIN Courses ON Student_courses.course_id = Courses.c_id
	WHERE Courses.name = 'python' AND Students.city == 'Spb' ''')
print(cursor.fetchall())	# [('Max',), ('John',)]

conn.close()	# !!! Закомментить первый уровень задачи перед работой со вторым !!!

## m8 p1 lvl3

conn1 = SqliteDatabase('mod8testdb.sqlite')

class Students(Model):

	s_id = IntegerField(primary_key=True, column_name='s_id')	# без primary_key не итерируется
	name = CharField(column_name='name')
	surname = CharField(column_name='surname')
	age = IntegerField(column_name='age')
	city = CharField(column_name='city')

	class Meta:
		database = conn1

class Courses(Model):

	c_id = IntegerField(primary_key=True, column_name='c_id')	# без primary_key не итерируется
	name = CharField(column_name='name')
	time_start = DateTimeField(column_name='time_start')
	time_end = DateTimeField(column_name='time_end')

	class Meta:
		database = conn1

class Student_courses(Model):

	student_id = ForeignKeyField(Students) 
	course_id = ForeignKeyField(Courses)

	class Meta:
		database = conn1

def new_student(s_id, course_id, name, surname, age, city):			# Создаём нового студента
	Students.create(s_id=s_id, name=name, surname=surname, age=age, city=city)
	Student_courses.create(student_id=s_id, course_id=course_id)	# Сразу связываем айди студента с айди курса
	conn1.commit()

def new_course(c_id, name, time_start, time_end):					# Создаём новый курс, если нужен
	Courses.create(c_id=c_id, name=name, time_start=time_start, time_end=time_end)
	conn1.commit()

def add_query(course_name=None, min_age=None, city=None):			# Опциональные поля
    q = Students.select().join(Student_courses).join(Courses)
    conditions = []

    if min_age:
        conditions.append(Students.age > min_age)
    if course_name:
        conditions.append(Courses.name == course_name)
    if city:
        conditions.append(Students.city == city)
    if conditions:
        q = q.where(*conditions)				# Объединяем условия
    return q

def some_fetch(query, field):					# Выбираем, какое поле хотим поместить в список для вывода
	return [getattr(i, field) for i in query]	# Для каждого query создаём список из field

# conn1.drop_tables([Student_courses, Students, Courses], safe=True)	# Опционально - по условию задачи не нужно
# conn1.create_tables([Students, Courses, Student_courses])

conn1.connect()

new_student(5, 3, 'Phoebe', 'Waller-Bridge', 39, 'London')	# student id = 5, course id = 3 (C#)
new_course(3, 'C#', '2024-10-15', '2024-10-16')
new_student(6, 1, 'Copper', 'Horseman', 192, 'Spb')			# student id = 6, course id = 1 (python)

query = add_query(min_age=30)						# Создаём query всех age > 30
print(some_fetch(query, 'name'))					# Выводим все имена для query: ['Andy', 'Kate', 'Phoebe', 'Copper']
query = add_query(course_name='python')				# Создаём query всех pyton
print(some_fetch(query, 'name'))					# ['Max', 'John', 'Andy', 'Copper']
query = add_query(course_name='python', city='Spb')	# Создаём query всех pyton и Spb
print(some_fetch(query, 'name'))					# ['Max', 'John', 'Copper']

conn1.close()