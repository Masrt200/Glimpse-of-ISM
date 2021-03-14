import random
from functools import reduce
from secret import flag,password


def make_chessboard(init):
	
	board="-"*33+"\n"
	for i in range(8):
		board+="|"
		for j in range(8):
			if init[i*8+j]:
				board+=" H "
			else:
				board+=" T "
			board+="|"

		board+="\n"+"-"*33+"\n"
	return board


def me_n_warden(init):

	warden_key=random.randint(0, 63)

	current_state=reduce(lambda x,y: x^y, [i for i,bit in enumerate(init) if bit])
	
	my_flip=current_state^warden_key
	init[my_flip]^=1

	return warden_key,init

win=True

title=b"          _  _  _      __  _  _ ____ _ _ \n\\    //\\ |_)| \\|_|\\ |/(_  / \\|_|_ | / |_ \n \\/\\//--\\| \\|_/|_| \\| __) \\_/| | _|_\\_|_ \n                                         \n"
print(title.decode())

messages=[b"Here's your chessboard, find the Key\n\n",b"\nApparently, the warden knows about the BF approach.\n Four more doors await you\n\n",b"\nTime is of the essence, 3 to go\n\n",b"\nPENULTIMATE DOOR\n\n",b"\nI see freedom!? Shinzou Sasaageo!!!\n\n"]
FAIL=["RIP Weroix","I hope you live to tell this story","Better find a broken window on the 3rd floor","Warden ka lathi ka sound kabhi suna hai?","Best Wishes, Prof. Rajiv Shekhar"]

for i in range(5):
	print(messages[i].decode())

	premise=[random.randint(0,1) for i in range(64)]
	key_location,premise=me_n_warden(premise)

	print(make_chessboard(premise))
	try:
		your_guess=input("key's at: ")
	except:
		win=False
		break

	try:
		your_guess=int(your_guess)
	except:
		win=False
		break

	if your_guess==key_location:
		print("Impressed")
	else:
		win=False
		print("\n"+random.choice(FAIL))
		break

if win:
	print("\nThe Warden hopes you enjoy your date, Until next time")
	print("oh take this-->",flag)
	print("password:",password)


