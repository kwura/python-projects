#  Description: Guesses a number that the user has chosen between 1 and 100


def high_guess(prev_guess, lo):
  hi = prev_guess - 1
  mid = (hi + lo) // 2
  return mid, hi 

def low_guess(prev_guess, hi):
  lo = prev_guess + 1
  mid = (hi + lo) // 2
  return mid, lo 

def main():
  print()
  print("Guessing Game")
  print()
  print("Think of a number between 1 and 100 inclusive.")
  print("And I will guess what it is in 7 tries or less.")
  print()
  
  # Prompt user whether to go through with series of guesses
  readiness = input("Are you ready? (y/n): ")
  print()
  while(readiness != "n" and readiness != "y"):
    readiness = input("Are you ready? (y/n): ")
    print()

  if (readiness == "n"):
    print()
    print("Bye")
    print()
    return 
  else:
    lo = 1
    hi = 100
    guess = (lo + hi) // 2
    
    for i in range (1,8):
      # Print the guess
      print("Guess", i, ":  The number you thought was", guess)
	  
      # Prompt the user response and play the game
      feedback = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
      print()
      while(feedback != "0" and feedback != "1" and feedback != "-1"):
        feedback = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
        print()
      if(i == 7 and (feedback == "1" or feedback == "-1")):
        print("Either you guessed a number out of range or you had an incorrect entry.")
        return 
      elif(feedback == "0"): 
        print("Thank you for playing the Guessing Game.")
        return
      elif(feedback == "1"):
        guess, hi = high_guess(guess, lo)
      else:
        guess, lo = low_guess(guess, hi)

main()
        
    
 
 
 
 
 
 
 
 
 
 