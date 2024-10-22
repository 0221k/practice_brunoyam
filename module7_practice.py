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

dates1 = soup.find_all('table', {'class': 'mfd-table mfd-currency-table'})
all_tr = dates1[0].find_all('tr')

# m7 p1 lvl1

for tr in all_tr:
	all_td = tr.find_all('td')
	if len(all_td) > 1:
		first_td = all_td[0]
		second_td = all_td[1]
		print(first_td.get_text(strip=True)[2:])
		print(second_td.get_text(strip=True))

# m7 p1 lvl2

dates = []
currency = []

for tr in all_tr:
	all_td = tr.find_all('td')
	if len(all_td) > 1:
		first_td = all_td[0]
		second_td = all_td[1]

		date = first_td.get_text(strip=True)[2:]

		if '*' not in second_td.get_text():
			dates.append(datetime.strptime(date, '%d.%m.%Y'))
			currency.append(float(second_td.get_text(strip=True)))
		else:
			continue

fig, ax = plt.subplots()
ax.plot(dates, currency, marker='o')
ax.set_xlabel('Date')
ax.set_ylabel('Currency value')
ax.set_title('USD Currency')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))

plt.show()