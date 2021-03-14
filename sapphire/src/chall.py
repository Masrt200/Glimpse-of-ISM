#!/usr/bin/env python3
import random
from secret import FLAG

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


print("flag server 3.14")
print("all messages sent here are encrypted\n")
n,e,c=keygen()
print(f"n: {n}")
print(f"e: {e}")
print(f"c: {c}")
