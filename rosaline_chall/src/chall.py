import subprocess

print("enter an command to run!!!")

while True:
	print("> ",end="")
	data=input()
	p=subprocess.Popen(data, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	out,err=p.communicate()
	rc=p.returncode
	print(rc)
