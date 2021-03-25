from secret import flag,binary_password

password=input("Input the binary's password to get flag: ")
try:
	assert password==binary_password
	print("\033[32mpassed\033[0m")
	print("-"*24)
	print("\033[32m"+flag+"\033[0m")
except AssertionError:
	print("\033[93mPushpa, I hate unintended!\033[0m")
	exit()