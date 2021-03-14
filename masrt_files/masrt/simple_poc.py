from hashlib import sha256
import os
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