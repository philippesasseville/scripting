import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='webCrawler')
parser.add_argument('base',metavar='baseurl')
args = parser.parse_args()

def recursiveCrawl(base_url,href=None):
	href = ''
	source_code = requests.get(base_url+href)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for link in soup.findAll('a'):
		href = link.get("href")
		print(base_url + href)
		crawledUrls = set()
		crawledUrls.add(href)
		if link not in crawledUrls:
			recursiveCrawl(base_url,href)

recursiveCrawl(args.base)
