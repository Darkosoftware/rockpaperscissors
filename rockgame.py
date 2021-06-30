import os
import random

print("Hi there I am a rock paper scissors playing bot, what is your name?")
name = input("Name: ")
print("It is very nice to meet you ",name,". Would you like to play rock paper scissors? :)")
answer = str(input("Y/N: "))
computer_player = ['rock', 'paper', 'scissors']
if (answer == 'N' or answer == 'n'):
	print("Oh ok, well maybe next time. Bye-bye :)")
if (answer == 'Y' or answer == 'y'):
	print("Awesome you go first!!!!")
	playerinput = str(input("type 'rock', 'paper', or 'scissors': "))
	computer_choice = str(random.choice(computer_player))
	print("I choose", computer_choice,"!!")
	if (computer_choice == 'rock' and playerinput == 'rock'):
		print("It's a tie!!")
	elif (computer_choice == 'rock' and playerinput == 'paper'):
		print("Congrats! You win!")
	elif (computer_choice == 'rock' and playerinput == 'scissors'):
		print("Sorry, you lose this time!")
	elif (computer_choice == 'paper' and playerinput == 'paper'):
		print("It's a tie!!")
	elif (computer_choice == 'paper' and playerinput == 'scissors'):
		print("Congrats! You win!")
	elif (computer_choice == 'paper' and playerinput == 'rock'):
		print("Sorry, you lose this time!")
	elif (computer_choice == 'scissors' and playerinput == 'scissors'):
		print("It's a tie!!")
	elif (computer_choice == 'scissors' and playerinput == 'rock'):
		print("Congrats! You win!")
	elif (computer_choice == 'scissors' and playerinput == 'paper'):
		print("Sorry, you lose this time!")
	else:
		print("Sorry, I didnt understand")
print("Well,",name,", would you like to play again?")
answer2 = str(input("Y/N: "))
if (answer2 == 'N' or answer2 == 'n'):
	print("Oh ok, well maybe next time. Bye-bye :)")
if (answer2 == 'Y' or answer2 == 'y'):
	print("Awesome you go first!!!!")
	playerinput2 = str(input("type 'rock', 'paper', or 'scissors': "))
	computer_choice2 = str(random.choice(computer_player))
	print("I choose", computer_choice2,"!!")
	if (computer_choice2 == 'rock' and playerinput2 == 'rock'):
		print("It's a tie!!")
	elif (computer_choice2 == 'rock' and playerinput2 == 'paper'):
		print("Congrats! You win!")
	elif (computer_choice2 == 'rock' and playerinput2 == 'scissors'):
		print("Sorry, you lose this time!")
	elif (computer_choice2 == 'paper' and playerinput2 == 'paper'):
		print("It's a tie!!")
	elif (computer_choice2 == 'paper' and playerinput2 == 'scissors'):
		print("Congrats! You win!")
	elif (computer_choice2 == 'paper' and playerinput2 == 'rock'):
		print("Sorry, you lose this time!")
	elif (computer_choice2 == 'scissors' and playerinput2 == 'scissors'):
		print("It's a tie!!")
	elif (computer_choice2 == 'scissors' and playerinput2 == 'rock'):
		print("Congrats! You win!")
	elif (computer_choice2 == 'scissors' and playerinput2 == 'paper'):
		print("Sorry, you lose this time!")
	else:
		print("Sorry, I didnt understand")
print("I've had alot of fun playing with you, but I need to rest my computer brain. Hope to see you again soon! Bye-bye :)")
