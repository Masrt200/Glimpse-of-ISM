#!/usr/bin/env python3
import random
from secret import FLAG,current_password

m=int.from_bytes(FLAG.encode(),'big')

primes=open("primes.txt").read().strip().split('\n')
primes=[int(i) for i in primes]

def keygen():
	p=random.choice(primes)
	q=p
	while q==p:
		q=random.choice(primes)

	n=p*q
	e=65537
	c=pow(m,e,n)

	return n,e,c

password=input("Sanity Check! input this level's password: ")
try:
	assert password==current_password
	print("\033[32mpassed\033[0m")
	print("-"*24)
except AssertionError:
	print("\033[93mI see that you are dirty!\033[0m")
	exit()


print("flag server 3.14")
print("all messages sent here are encrypted\n")
n,e,c=keygen()
print(f"n: {n}")
print(f"e: {e}")
print(f"c: {c}")
