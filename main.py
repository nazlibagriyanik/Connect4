import numpy as np
#from termcolor import colored
# The main menu for game
 
menu = "\n                               Connect 4 Game"
print(menu, "\n", "*"*81, sep="")
print("To play the game select the number of the column where you want to drop your disc")
print("Player 1 = X  Player 2 = W")

def menu():
 print("\n\n   Menu\n------------")
 print("1- New Game")
 print("2- Exit")


def menu_choice():
 a=input("Choose one of them: ")
 return a


def main_menu():
 while True:
  menu()
  a=menu_choice()


  if a == "1":
   with open("hamle.txt", "w") as f:
        f.write("")
   with open("tahta.txt", "w") as f2:
        f2.write("")
   
  
   player_letters = {1: "X", 2: "W"}
   
   #Connect 4 game board matrix
   board = np.zeros((9,9), dtype=int)
   
   #Creating an empty string to save moves and board
   moves = ""
   board_str = ""

   #The game
   player = 1
   game_over = False

   print("\n")
   labels = [" 0 ", " 1 ", "  2 ", "  3 ", "  4 ", "  5 ", "  6 ", "  7 ", "  8 "]
   print(" ".join(labels))
   
   for row in reversed(board):
    row_str = "  | ".join([player_letters[symbol] if symbol != 0 else " " for symbol in row])
    print(row_str)
    print("-"*43)

   while not game_over:
    
    col = int(input("Player {} choose column (0-8) or press -1 for continue or press -2 for menu: ".format(player)))
    print("\n")

    if col == -1:
      continue
    elif col == -2:
      main_menu()
      
    if 0 in board[:,col]:
     row = np.argmax(board[:,col] == 0)
     board[row,col] = player
    else:
     print("Column is full! Try again.") 
     continue

    board_str = ""
    for row in reversed(board):
     
     row_str = "  | ".join([player_letters[symbol] if symbol != 0 else " " for symbol in row])
     board_str += row_str + "\n"
     print(row_str)
     print("-"*43)
    #f.write(board_str)
    moves += str(player) + "'s column selection : " + str(col) + "\n"

    for r in range(9):
     for c in range(9):
      if c < 4 and board[r,c] == player and board[r,c+1] == player and board[r,c+2] == player and board[r,c+3] == player:
        game_over = True
      if r < 3 and board[r,c] == player and board[r+1,c] == player and board[r+2,c] == player and board[r+3,c] == player:
        game_over = True
      if r < 3 and c < 4 and board[r,c] == player and board[r+1,c+1] == player and board[r+2,c+2] == player and board[r+3,c+3] == player:
        game_over = True
      if r < 3 and c > 2 and board[r,c] == player and board[r+1,c-1] == player and board[r+2,c-2] == player and board[r+3,c-3] == player:
        game_over = True
  
    if game_over:
     print("Player {} wins!".format(player))
     moves += "Player {} wins!".format(player)
    elif 0 not in board:
     print("It's a tie!")
     moves += "It's a tie!"
     game_over

    player = 3 - player

    with open("hamle.txt", "w") as f:
     f.write(moves)

    with open("tahta.txt", "w") as f2:
     f2.write(board_str)
    

  elif a == "2":
   with open("hamle.txt", "w") as f:
    f.write("")
   with open("tahta.txt", "w") as f2:
    f2.write("")
   exit()

  else:
   print("\nInvalid choice!")

if __name__ == "__main__":
    main_menu()
