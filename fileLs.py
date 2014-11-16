import subprocess

file_object = open("lslog.txt",'w')
subprocess.call("ls -l",stdout=file_object,shell=True)
