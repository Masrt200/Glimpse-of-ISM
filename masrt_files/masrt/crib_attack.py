data=open("message.txt","r").read().split("\n")[:-1]

def xor_all(check):

	for i in data:
		block=bytes.fromhex(i)
		plain=bytearray()
		for j,k in zip(check,block):
			plain.append(j^k)
		print(plain)
		print(plain.hex())
		print("\n\n")


check=b'\xf7{W'

xor_all(check)

