def fix_teen(n):
  if n ==13 or n == 14 or n == 17 or n ==18 or n ==19:
    n = 0
  return n 
def no_teen_sum(a, b, c):
  a = fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)
  return a + b +c

import math, random

def count_double(st):
  index = 0
  count = 0
  switch = True
  while(index < (len(st) - 1)):
    if(switch == True and st[index] == st[index +1]):
      count += 1
      index += 1
      switch = False
      continue
    elif(switch == False):
      switch = True
      index += 1
    else:
      index += 1
  return count 	  
def main():
  string = input("enter number combination: ")
  print("The number of double numbers is:", count_double(string), end = ".")
main()