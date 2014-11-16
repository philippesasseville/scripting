#!/usr/bin/env python
import subprocess

def runBash(cmd):
	p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
	out = p.stdout.read().strip()
	return out.split('\n')

def changeName(oldName,newNameBase):
	temp = oldName.split('.')
	newName = newNameBase + '.' + temp[1] + '.' + temp[2]
	subprocess.call(["mv",oldName,newName])

def changeAllNames(oldNameBase,newNameBase):
	files = runBash("ls")

	for afile in files:
		if afile.split('.')[0] == oldNameBase:
			changeName(afile,newNameBase)

changeAllNames("test","new")
