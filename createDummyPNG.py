#!/usr/bin/env python
import subprocess

for i in range (0,99):
	subprocess.Popen("touch test"+ str(i) +".png",shell=True)
	
