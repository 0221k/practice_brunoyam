import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

url = 'https://mfd.ru/currency/?currency=USD'

page = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 '
'Firefox/50.0'})

soup = BeautifulSoup(page.content, 'html.parser')

all_tr = soup.select('table.mfd-table.mfd-currency-table tr')

# m7 p1 lvl1

def currency_parse(table_rows):
	for tr in all_tr:
		all_td = tr.find_all('td')
		if len(all_td) > 1:
			first_td, second_td = all_td[0], all_td[1]
			print(f'{first_td.get_text(strip=True)[2:]}: {second_td.get_text(strip=True)}')

currency_parse(all_tr)

# m7 p1 lvl2

dates = []
currency = []

def currency_plot(dates_list, currency_list, table_rows):
	for tr in table_rows:
		all_td = tr.find_all('td')
		if len(all_td) > 1:
			first_td, second_td = all_td[0], all_td[1]

			date = first_td.get_text(strip=True)[2:]

			if '*' not in second_td.get_text():
				dates_list.append(datetime.strptime(date, '%d.%m.%Y'))
				currency_list.append(float(second_td.get_text(strip=True)))
			else:
				continue

def draw_plot(dates_list, currency_list):
	fig, ax = plt.subplots()
	ax.plot(dates_list, currency_list, marker='o')
	ax.set_xlabel('Date')
	ax.set_ylabel('Currency value')
	ax.set_title('USD Currency')

	ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))

	plt.show()

currency_plot(dates, currency, all_tr)
draw_plot(dates, currency)