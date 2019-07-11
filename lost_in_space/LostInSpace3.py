import random
import os


#Bilding the Grid.

Cells = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
		 (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
		 (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
		 (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
		 (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
		 (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5),
		 (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)]


def get_locations():
	return random.sample(Cells, 7)


#cls

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


def move_player(player, move):
	x, y = player
	if move == "A":
		x = x-1
	if move == "W":
		y = y-1
	if move == "D":
		x = x+1
	if move == "S":
		y = y+1
	return x, y


def get_moves(player):
	moves = ["A", "S", "D", "W"]
	x, y = player 
	if y == 0:
		moves.remove("W")
	if y == 6:
		moves.remove("S")
	if x == 0:
		moves.remove("A")
	if x == 6:
		moves.remove("D")
	return moves


def draw_map(player):
	print(" _"*7)
	tile = "|{}"

	for cell in Cells:
		x, y = cell
		if x < 6 :
			line_end = ""
			if cell == player:
				output = tile.format("X")
			else:
				output = tile.format("_")
		else:
			line_end = "\n"
			if cell == player:
				output = tile.format("X|")
			else:
				output = tile.format("_|")
		print(output, end = line_end)

def game_loop():
	hole1, hole2, hole3, elien1, elien2, earth, player = get_locations()
	intialplayer = player
	playing = True
	while playing:
		clear_screen()
		draw_map(player)
		valid_moves = get_moves(player)
		print("you are in room {} ".format(player))
		#print("you can move {}".format(', '.join(valid_moves)))

		move = input("> ")
		move = move.upper()

		if move == "Q":
			break
		if move in valid_moves :
			player = move_player(player, move)

			if player == hole1:
				print("\n ** OH! BLACK HOLE **")
				player = hole2
				input()
				continue
			if player == hole2:
				print("\n ** OH! BLACK HOLE **")
				player = hole3
				input()
				continue
			if player == hole3:
				print("\n ** OH! BLACK HOLE **")
				player = hole1
				input()
				continue
			if player == elien1:
				print("\n Elien got ya")
				print("\n HIT 'E' to escape")
				#if input().upper() == 'E':
				print("OOh you scape watch that place")
				player = intialplayer
				#else:
				#	print("Hurry !!")
			if player == elien2:
				print("\n Elien got ya")
				print("\n HIT 'E' to escape")
				#if input().upper() == 'E':
				print("OOh you scape watch that place")
				player = intialplayer
				#else:
				#	print("Hurry !!")
				
			if player == earth :
				print("\n ** YAY! Welcome home")
				playing = False


		else:
			input("\n OUTCH !! seems like the 2-D space has edges \n")
	else:
		
		if input ("play again ? [Y/N] ").lower() != 'n':
			game_loop()
		

clear_screen()
print("welcome! \nHit ENTER to play.")
input()
clear_screen()
print("Game Script : You wake up in morning and found your self LostInSpace.")
print("	Don't panic it is just 2-D space so you have 4 ways to go")
print("	Use 'S' to go DOWN, 'A' to LEFT, 'D' to RIGHT and 'W' to UP. ")
print("	Keep going throw all the BLACK HOLES you may met untill you get EARTH")
print("	BE carefull the 2-D space may be inhabitant !! ")
print("ENTER to get lost")
print("Hit Q to quit")
input()
clear_screen()
game_loop()
