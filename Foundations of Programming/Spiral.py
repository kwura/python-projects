#  Description: Creates a spiral with a specific dimension and outputs the neighboring numbers of a target number in three lines.



def make_spiral(dims):
# create 2-D list with zeros
  a = []
  for i in range (dims):
    b = []
    for j in range(dims):
      b.append(0)
    a.append(b)
  
  reference = dims ** 2
  for limit in range (dims//2):  
  # Start at top right corner and go left
    index = len(a[0]) - 1 - limit 
    while( index >= limit):
      a[limit][index] = reference
      index -= 1
      reference -= 1
  
  # Go down first column
    index = limit + 1
    while(index  < len(a) - limit):
      a[index][limit] = reference
      index += 1
      reference -= 1
  
  # Go through bottom row left to right
    index = limit + 1
    while(index < (len(a[0]) - limit)):
      a[len(a) - 1 - limit][index] = reference
      index += 1
      reference -= 1
	
  # Go up last column
    index = len(a) -2 - limit
    while(index > limit):
      a[index][len(a[0])-1 - limit] = reference
      index -= 1
      reference -= 1
  
  # Fill in the center of the spiral 
  a[dims//2][dims//2] = 1
  
  # Return the spiral 
  return a 
  
def is_onEdge(number, list):
  # Check if number is on vertical sides of perimeter
  for i in range (len(list)):
    if(list[i][0]== number or list[i][len(list) -1]==number):
      return True
	  
  # Check if number is on horizontal sides of perimeter
  if( number in list[0] or number in list[len(list)-1]):
    return True
  
  return False
  

def find_target(number, list):
  # Find location of target number and return the index of the row and column
  for i in range(1, len(list) -1):
    if( number in list[i]):
      row = i 
      column = list[i].index(number)
      return row, column
 

def main():

  # Prompt the user for number of dimensions
  dims = input("Enter dimension: ")
  while( dims.isdigit() == False ):
    dims = input("Enter dimension: ")
  dims = int(dims)
  if( dims % 2 == 0 ):
    dims += 1
  
  # Prompt the user for number in spiral
  target = input("Enter number in spiral: ")
  while( target.isdigit() == False ):
    target = input("Enter number in spiral: ")
  target = int(target)
  if( target < 1 or target > dims**2 ):
    print()
    print("Number not in Range")
    return
	
  # Create the spiral
  spiral = make_spiral(dims)
  
  # Check if second number is on perimeter
  if(is_onEdge(target,spiral)):
    print()
    print("Number on Outer Edge")
    return
  
  # Find the target
  row, column = find_target(target, spiral)

  # Print the output
  print()
  
  print(spiral[row-1][column-1], spiral[row-1][column], spiral[row-1][column+1])
  
  print(spiral[row][column-1], spiral[row][column], spiral[row][column+1])
  
  print(spiral[row+1][column-1], spiral[row+1][column], spiral[row+1][column+1])


main()