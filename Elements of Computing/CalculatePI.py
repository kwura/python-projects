#  Description: Determines the value of pi through computation

import math
import random

# function that computes pi based on number of throws using random numbers
def computePI ( numThrows ):
  inside = 0
  throw = 0 
  while (throw < numThrows):
    xPos = random.uniform (-1.0, 1.0)
    yPos = random.uniform (-1.0, 1.0)
    distance = math.hypot (xPos, yPos)
    if (distance < 1):
      inside += 1
    throw += 1
  return (inside/numThrows)*4
  

def main ():
  print()
  print("Computation of PI using Random Numbers")
  print()
  
# prints the Computation of PI for varying number of throws  
  space = 6
  for i in range (2,8):
    num = 10**(i) 
    pi_compute = computePI(num)
    difference = pi_compute - math.pi
    print("num = %0-d" % (num), (space)*(" "), "Calculated PI = %.6f" % (pi_compute), "  Difference = %+.6f" % (difference))
    if (space >0):
      space -=1
 
  print()
  print("Difference = Calculated PI - math.pi")
main ()