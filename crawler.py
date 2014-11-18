import requests
from bs4 import BeautifulSoup

def trade_spider():
	url = 'https://buckysroom.org/trade/search.php'
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for link in soup.findAll('a',{'class': 'item-name'}):
		href = "https://buckysroom.org" + link.get('href')
		title = link.string
		print(title)
		print(href)
		get_single_item_data(href)

def get_single_item_data(item_url):
	source_code = requests.get(item_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for item_name in soup.findAll('div',{'class' : 'i-name'}):
		print(item_name.string)

trade_spider()
