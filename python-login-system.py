#Write a program for login system with 3 attempts.
from getpass import getpass
pwd="Sairam"
attempts=0

while True:
	print("Login:")
	password=input("Enter the password:")
	if password==pwd:
		print("Succesfully logged in!!")
		break
	else:
		print("Login failed try again!!")
		attempts+=1
		if attempts==3:
			print("Login blocked,Due to many wrong attempts!!")
			print("Try after 20 seconds.!!")
			import time
			time.sleep(20)
