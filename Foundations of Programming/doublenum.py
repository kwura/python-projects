#def is_prime (n):
 # if (n == 1):
  #  return False
  #limit = int (n ** 0.5) + 1
  #div = 2
  #while (div < limit):
  #  if (n % div == 0):
  #    return False
  #  div += 1
  #return True
import math, random


def double_num(n):
  index = 0
  count = 0 
  switch = True
  
  while( index < len(n) - 1):
    if(switch == True and (n[index] == n[index+1])):
      count += 1 
      index += 1
      switch = False
    elif(switch == False):
      index += 1
      switch = True 
    else:
      index += 1
  return count 




def main():
  a = str(input("Enter list of numbers: "))
  
  count = double_num(a)
  if (count == 0):
    print("There are no double numbers")
  else:
    print("There are", count, "double numbers.")
    
main()


