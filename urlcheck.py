#!/usr/bin/env python
import argparse
import requests
import re
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='details a url')
parser.add_argument('url',metavar='urlreference')
args = parser.parse_args()

def getUrlDetails(url):
	print("url :"+url)
	match = re.search(r'(\w+)+://', url)
	if match:
		print("protocol : "+match.group(1))
	match = re.search(r'://+(\w+)+\.', url)
	if match:
		print("sub domain : "+match.group(1))
	match = re.search(r'\.+(\w+)+\.', url)
	if match:
		print("domain : "+match.group(1))
	match = re.search(r'\.+(\w+)+/', url)
	if match:
		print("top-level domain : "+match.group(1))
	
	source_code = requests.get(url)
	
	if source_code:
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text)

		match = re.search(r'DOCTYPE\s+(\w+)', plain_text)
		if match:
			print("DOCTYPE : "+match.group(1))
		else:
			print("This page doesnt have a doctype declaration")

		res = soup.findAll('title')	
		if len(res) == 0:
			print("There is no title on this page")	

		for title in res:
			print("title : "+title.text)

		res = soup.findAll('p')
		nbp = 0
		for paragraphs in res:
			nbp+=1

		print("Number of paragraphs : "+str(nbp))

	

getUrlDetails(args.url)


