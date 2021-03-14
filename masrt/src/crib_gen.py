import os
from functools import reduce

def xor(a,b):
    c=bytearray()
    for i,j in zip(a,b):
        c.append(i^j)

    return c

msg1="did you expect another rsa? sorry"
msg2=" to disappoint you. What you see is a bad use "
msg3="of the otp in encryption. It literally says one"
msg4=" and not multi time. masrt{think_out_of_the_box_yeager}"
msg5="well done solving me, but are you done?"
msg6="This attack is called a crib drag or known-plaintext attack"


messages=[msg1,msg2,msg3,msg4,msg5,msg6]
L=reduce(max,[len(i) for i in messages] )

key=os.urandom(L)

open("key.txt","a").write(key.hex()+"\n")

with open("message.txt","w") as f:
    for msg in messages:
        f.write(xor(msg.encode(),key).hex()+"\n")
    f.close()
