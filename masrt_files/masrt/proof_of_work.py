#from pwn import *
import re
import hashlib
from string import *
from itertools import product
import sys

'''
r=remote('05.cr.yp.toc.tf',33371)
data=r.recvline().decode()
algo=re.findall(r'that (.*?)\[-6:]', data)[0][:-3]
calc=re.findall(r'= (.*) and', data)[0]
length=int(data[-3:-1])'''

#print(algo,length,calc)
#"#'#re.findall(r'\) == (.*?)\n',data)[0]

char_set=ascii_uppercase+ascii_lowercase+digits
#print(known,hashh)

comb=product(char_set,repeat=7)

hashes={"md5":hashlib.md5,"sha224":hashlib.sha224,"sha256":hashlib.sha256,"sha1":hashlib.sha1,"sha512":hashlib.sha512,"sha384":hashlib.sha384}

'''
for i in hashes:
	if algo==i:
		algo=hashes[i]'''

algo=hashlib.sha256
calc="492504"
c=0
for i in comb:
	string=''.join(i)
	hashh=algo(string.encode()).hexdigest()
	if hashh[-6:]==calc:
		print(string)
		break

#r.sendline(string)
#r.interactive()
