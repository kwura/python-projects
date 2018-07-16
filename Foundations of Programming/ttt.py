#! python3

# Allows the user to play a game of tic tac toe!!
import random
# Checks for game-winner!
def check(a):
  for i in range (3):
    if(a[i][0] == a[i][1] and a[i][1] == a[i][2]):
      return True
    if(a[0][i] == a[1][i] and a[1][i] == a[2][i]):
      return True
  if(a[0][0] == a[1][1] and a[1][1] == a[2][2]):
    return True
  if(a[0][2] == a[1][1] and a[1][1] == a[2][0]):
    return True
  return False
    
# Function that draws out the board
def draw_board(d):
  print(d["top-L"] + "|" + d["top-M"] + "|" + d["top-R"])
  print("-----")
  print(d["mid-L"] + "|" + d["mid-M"] + "|" + d["mid-R"])
  print("-----")
  print(d["low-L"] + "|" + d["low-M"] + "|" + d["low-R"])
  



def main():
  decide = "yes"
  while(decide == "yes"):
  # Establish the gameboard dictionary
    theBoard = {"top-L": " ", "top-M": " ", "top-R": " ", "mid-L": " ", "mid-M": " ", "mid-R": " ","low-L": " ", "low-M": " ", "low-R": " "}
  
  # Start the game and decide the players
    print()
    print("Welcome to Tic Tac Toe!")
    print("Do you want to be X or O?")
    playerChoice = input().upper()
    print("The computer will go first")
    print()
    if(playerChoice == "X"):
      comp = "O"
    else:
      comp = "X"
  
    counter = [["top-L","top-M","top-R"],["mid-L","mid-M","mid-R"],["low-L","low-M","low-R"]]
  
  # Create the "physical" board after each play!
    comp_move = random.choice(list(theBoard.keys()))
    theBoard[comp_move] = comp
    draw_board(theBoard)
    for i in range(3):
      if comp_move in counter[i]:
        position = counter[i].index(comp_move)
        counter[i][position] = comp 
	  
    for i in range(4):
    # Player's Turn
      print()
      print("What is your move?  Type: (top-, mid-, low-) Position: (L, M, R)")
      p_move = input()
      while(p_move not in theBoard):
        p_move = input()
      theBoard[p_move] = playerChoice
      draw_board(theBoard)
      for j in range(3):
        if p_move in counter[j]:
          position = counter[j].index(p_move)
          counter[j][position] = playerChoice
		  
	# Check if the player wins
      if(check(counter) == True):
        print()
        print("Nice one, yo! You win!")
        return
	
	# Computer's turn
      print("The computer will go next")
      comp_move = random.choice(list(theBoard.keys()))
      while(theBoard[comp_move] == "X" or theBoard[comp_move] == "O"):
        comp_move = random.choice(list(theBoard.keys()))
      theBoard[comp_move] = comp
      draw_board(theBoard)
      for j in range(3):
        if comp_move in counter[j]:
          position = counter[j].index(comp_move)
          counter[j][position] = comp
    # Check if the computer wins
      if(check(counter) == True):
        print()
        print("LMAO!!!! The computer beat you! You loser!")	
        return
  
  # No winners
    print("No winners this time!")
    print("Do you want to play again? (Yes or No)")
    decide = input().lower()
  	  
    
   
    
  
	
  
  
  
  
main()