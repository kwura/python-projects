#File: Simple Input and Output

def main ():
#prompt the user for name
  name = input ("Enter your name:")
  
#greet the person
  print ("What's up", name, "!" , "How many calories did you eat today?")

#prompt the user for radius
  
  calories = eval (input("Enter number of calories:"))
  
#compute the area
  if (calories >= 1500):
  
  
#print the result
    print ("no no no! That's too many calories", name, "!")
  
  else:
    print ("Nice job. Proud of you", name, "!", "That's a good amount. Keep it up")
main ()
  