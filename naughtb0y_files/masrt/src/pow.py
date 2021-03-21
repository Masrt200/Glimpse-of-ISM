from hashlib import sha256
import os
from secret import current_password

password=input("Sanity Check! input this level's password: ")
try:
	assert password==current_password
	print("\033[32mpassed\033[0m")
	print("-"*24)
except AssertionError:
	print("\033[93mGoto a Doctor\033[0m")
	exit()


message="enter a string whose sha256 hash in hex satisfies, sha256(string[-6:]) ="

def hash_gen():
	HASH=sha256(os.urandom(16)).hexdigest()[-6:]

	return HASH

HASH=hash_gen()
print(message,HASH)

string=input("> ")
check=sha256(string.encode()).hexdigest()[-6:]

if check!= HASH:
	print("fail")
	exit()
else:
	print("verified\n")
	print("here is your message:")
	os.system("python3 crib_gen.py")
	with open("message.txt",'r') as f:
		print(f.read())