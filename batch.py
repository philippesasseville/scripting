#!/usr/bin/env python
import subprocess
import argparse
import re

parser = argparse.ArgumentParser(description='Batch change filenames')
parser.add_argument('inputFileName',metavar='baseNameIn')
parser.add_argument('outputFileName',metavar='baseNameOut')
args = parser.parse_args()

def runBash(cmd):
	p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
	out = p.stdout.read().strip()
	return out.split('\n')

def changeName(oldName,newNameBase):
	temp = re.split('([0-9]+)',oldName)
	newName = newNameBase + temp[1] + temp[2]
	subprocess.call(["mv",oldName,newName])

def changeAllNames(oldNameBase,newNameBase):
	files = runBash("ls")

	for afile in files:
		temp = re.split('([0-9]+)',afile)
		if temp[0] == oldNameBase:
			changeName(afile,newNameBase)

changeAllNames(args.inputFileName,args.outputFileName)

