# m6 p1 lvl1

import time
from threading import Thread

def get_thread(thread_name):
	time.sleep(1)
	print(thread_name)

threads = [Thread(target = get_thread, args = (f'Thread {i + 1}',),) for i in range(5)]

for t in threads:
	t.start()

for t in threads:
	t.join()

# m6 p1 lvl2

import time
from threading import Thread
from datetime import datetime

def get_thread(thread_name):
	time.sleep(3)
	print(thread_name)

threads1 = [Thread(target = get_thread, args = (f'Thread {i + 1}',), name = f'Thread {i + 1}') for i in range(5)]

def sequent_time():
	t1 = datetime.now()
	print('Start sequentially')

	for i in range(5):
	 	get_thread(f'Thread {i + 1}')

	return f'Finish. Time {(datetime.now() - t1).total_seconds()} seconds'

def parallel_time():
	t2 = datetime.now()
	print('Start in parallel')

	for t in threads1:
		t.start()

	for t in threads1:
		t.join()

	return f'Finish. Time {(datetime.now() - t2).total_seconds()} seconds'

print(sequent_time())
print(parallel_time())

# m6 p1 lvl3

import time
from threading import Thread
from datetime import datetime
import requests

url = 'https://brunoyam.com/'

def get_html(link):
	time.sleep(3)
	response = requests.get(link)
	if response.status_code == 200:
		page_content = response.text
		#print(page_content)			# закомментировал на всякий случай
	else:
		print(response.status_code)

threads2 = [Thread(target = get_html, args = (url,), name = f'Thread {i + 1}') for i in range(5)]

def sequent_time_requests():
	t1 = datetime.now()
	print('Start sequentially')

	for i in range(5):
	 	get_html(url)
	 	print(f'Thread {i + 1}')

	return f'Finish. Time {(datetime.now() - t1).total_seconds()} seconds'

def parallel_time_requests():
	t2 = datetime.now()
	print('Start in parallel')

	for t in threads2:
		t.start()

	for t in threads2:
		t.join()
		print(t.name)

	return f'Finish. Time {(datetime.now() - t2).total_seconds()} seconds'

print(sequent_time_requests())
print(parallel_time_requests())
