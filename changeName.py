#!/usr/bin/env python
import subprocess

def changeName(oldName,newNameBase):
	temp = oldName.split('.')
	newName = newNameBase + '.' + temp[1] + '.' + temp[2]
	subprocess.call(["mv",oldName,newName])

oldName = "test.1.png"
newNameBase = "new"

changeName(oldName,newNameBase)
