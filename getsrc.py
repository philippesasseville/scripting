#!/usr/bin/env python
import argparse
import requests
import re
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='details a url')
parser.add_argument('url',metavar='urlreference')
parser.add_argument('outputFileName',metavar='ouputname')
args = parser.parse_args()

def getSrc(url,outputFileName):
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	fd = open(outputFileName,'w')
	fd.write(plain_text.encode('utf-8'))

getSrc(args.url,args.outputFileName)
