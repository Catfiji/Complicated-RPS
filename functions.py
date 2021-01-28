
import random

from os import system

class choice:
	def __init__(self, ID, name, beatenby):
		self.name = name  
		self.ID = ID  
		self.bb = beatenby

rock = choice(0, "Rock", [1])
paper = choice(1, "paper", [2])
scissors = choice(2, "scissors", [0])

choices = [rock,paper,scissors]

player_wins = 0

ai_wins = 0

def get_user_input():
	user_input = input("[1] Rock\n[2]Paper\n[3]Scissors")
	user_input = int(user_input)
	user_input -= 1
	user_input = choices[user_input]
	
	return user_input # 0,1,2

def ai():

	ai = random.choice(choices)

	return ai	 

def check():
	global player_wins
	global ai_wins
	system('clear')
	print(f"Score:\nplayer:{player_wins}\nAi:{ai_wins}")
	user_input = get_user_input()
	ai_input = ai()

	print("AI Chose:",ai_input.name)
	print("You Chose:", user_input.name)
	if user_input.ID in ai_input.bb and ai_input.ID != user_input.bb:
		print("User win")
		player_wins += 1
	
	elif ai_input.ID in user_input.bb and ai_input.ID != user_input.bb:
		print("Ai wins")
		ai_wins += 1
	
	elif ai_input.ID == user_input.ID:
	
		print("tie")

def win():
	system('clear')
	print(f"Final scores:\n Player: {player_wins}\n Ai: {ai_wins}")
	if player_wins > ai_wins:
		return "\nWinner!"
	else:
		return "\nYou lost!"
