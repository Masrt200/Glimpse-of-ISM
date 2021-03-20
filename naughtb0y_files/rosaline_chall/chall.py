import subprocess
from secret import current_password

password=input("Sanity Check! input this level's password: ")
try:
	assert password==current_password
	print("\033[32mpassed\033[0m")
	print("-"*24)
except AssertionError:
	print("\033[93mnot all roses are red\033[0m")
	exit()

print("enter an command to run!!!")

while True:
	print("> ",end="")
	data=input()
	p=subprocess.Popen(data, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	out,err=p.communicate()
	rc=p.returncode
	print(rc)