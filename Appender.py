#!/usr/bin/env python
import subprocess
import argparse
import re

parser = argparse.ArgumentParser(description='append file1 to file2')
parser.add_argument('file1',metavar='firstfile')
parser.add_argument('file2',metavar='secondfile')
args = parser.parse_args()

def appender(aFile, anotherFile):
	f1 = open(aFile, 'r')
	f2 = open(anotherFile, 'r')
	string1 = f1.read()
	string2 = f2.read()
	f1.close()
	f2.close()
	final = open(aFile,'w')
	final.write(string1+string2)
	final.close()


appender(args.file1,args.file2)

