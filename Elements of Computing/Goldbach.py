#  Description: Verifies Goldbach's conjecture in a user defined range. 


# determine if a number is prime 
def is_prime (n):
  if (n == 1):
    return False
  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

  
def main():
# Prompt the user to enter the range.
  lower_limit = eval(input("Enter the lower limit: "))
  
  upper_limit = eval(input("Enter the upper limit: "))	

# If there is an input error, prompt the user to enter both the limits repeatedly.  
  while (lower_limit < 4 or lower_limit % 2 != 0 or upper_limit < lower_limit or upper_limit % 2 != 0):
    lower_limit = eval(input("Enter the lower limit: "))
    upper_limit = eval(input("Enter the upper limit: "))

# Compute and print all possible unique pairs of prime numbers for all even numbers in the range. 
  for even_number in range (lower_limit, upper_limit + 1, 2):	
    final_string = str(even_number)
    for a in range(even_number):
      if is_prime(a): 
        for b in range (a, even_number):
          if (b >= a and is_prime(b) and a + b == even_number):
            final_string += " = " + str(a) + " + " + str(b)
    
    print(final_string)
	
            
main()