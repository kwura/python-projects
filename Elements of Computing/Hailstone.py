#  Description: Computes the number of cycles in a Hailstone Sequence


def main ():

# Prompt the user to enter the starting number of the range and the ending number.
  a = int(input("Enter starting number of the range: "))
  print()
  
  b = int(input("Enter ending number of the range: "))
  print()  
  
  while(a < 1 or b < 1):
    a = int(input("Enter starting number of the range: "))
    print()
	
    b = int(input("Enter ending number of the range: "))
    print()
  
  while(b <= a):
    a = int(input("Enter starting number of the range: "))
    print()
    b = int(input("Enter ending number of the range: "))
    print()
	
# Determine the number in the range with the largest cycle length.
  number_max = 0
  cycle = 0 
  cycle_max = 0
  
  for i in range(a, b + 1):
    n = i	
    while (n > 1):
      if (n % 2 ==0):
        n = n // 2
      else:
        n = 3*n + 1
      cycle += 1
      if (cycle >= cycle_max):
        cycle_max = cycle 
        number_max = i
      if (n == 1):
        cycle = 0 
		
# Print the number that has the largest cycle length along with its cycle length.  
  print("The number", number_max, "has the longest cycle length of", cycle_max, end=".")
  
  print()
	  

main()