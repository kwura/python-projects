# Description: Simulates the Let's Make a Deal game and computes probabilites of winning for two strategies

import math, random

def main ():
  print()
  # prompt the user to enter the number of times he or she wants to play this game.
  num_games = eval(input("Enter number of times you want to play: "))
  while (num_games / math.floor(num_games)!= 1 or num_games <= 0):
    num_games = eval(input("Enter number of times you want to play: "))
  print ()
  
  print("  Prize      Guess       View    New Guess")
  
  # variable to keep track of the number of times the contestant wins by switching
  switch_wins = 0
  for i in range (1, num_games+1):
    doors = [1, 2, 3]
	# door that conceals the prize
    prize = random.randint(1,3)
    print_string = "    " + str(prize) + "          "
	# contestant guesses a door
    guess = random.randint(1,3)
    print_string += str(guess) + "          "
	# contestant views an empty door 
    if (prize == guess):
      doors.remove(prize)
      if (prize == 2):
        view = doors[1]
      else: 
        view = doors[0]
    else:
      doors.remove(prize)
      doors.remove(guess)
      view = doors[0]	
    print_string += str(view) + "          "
    # contestant switches doors
    new_doors = [1, 2, 3]
    new_doors.remove(guess)
    new_doors.remove(view)
    new_Guess = new_doors[0]
    print_string += str(new_Guess)
    # determine whether the contestant chooses the prize door
    if (new_Guess == prize):
      switch_wins += 1
    # Print the outputs of each game 
    print(print_string)
  print()
  # Probability of winning when switching
  switch_prob = round(switch_wins / num_games, 2)
  # Probability of winning when not switching
  stay_prob = round(1 - switch_prob, 2)
  
  print("Probability of winning if you switch = %.2f" %(switch_prob))
  print("Probability of winning if you do not switch = %.2f" %(stay_prob))

  
  
  
  

  
main()
