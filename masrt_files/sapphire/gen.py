from Crypto.Util.number import *
import random

with open("primes.txt","a") as f:
	for i in range(200):
		prime=getPrime(512)
		f.write(str(prime)+'\n')