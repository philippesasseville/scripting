import subprocess

cmd1 =  "echo A listing of the directory:"
cmd2 =  "ls -l"

cmds = [cmd1,cmd2]


for cmd in cmds:
	subprocess.call(cmd,shell=True)







