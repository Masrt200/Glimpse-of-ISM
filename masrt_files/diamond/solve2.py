from pcapfile import savefile
import re

f=open('dump-2.pcap','rb')

capfile = savefile.load_savefile(f, verbose=True)
packets=[bytes.fromhex(str(i)[2:-1]) for i in capfile.packets]

n=bytearray()
for i in packets:
	
	try:
		byte=re.findall(rb'\x00\x00(\d+).iitism.ac.in',i)[0].decode()
		n.append(int(byte))
	except:
		pass

print(n)
open('flag.jpg','wb').write(n)
