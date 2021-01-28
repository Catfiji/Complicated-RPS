
import functions as func 

from os import system

def main():
	menu = input("[1] Best of 3\n[2] Best of 5\n[3] Best of unlimited")
	if menu == "1":

		amt_of_turns = 3

	elif menu == "2":
		amt_of_turns = 5
	else:

		amt_of_turns = 666*666*666*666

	while amt_of_turns > 0:
		print("Turn:",amt_of_turns)
		func.check()

		amt_of_turns -= 1
	
	x = func.win()

	print(x)

main()
