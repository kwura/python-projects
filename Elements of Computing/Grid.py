#  Description: Determines the greatest product of four adjacent numbers in the same direction in a grid of positive numbers.


def max_prod(list, dimensions):

  # Greatest product counter
  greatest_prod = 0
  
  # read and multiply in blocks of four along rows
  for row in list:
    largest_in_row_prod = 0
    for start_num in range (dimensions - 3):
      prod = 1	  
      for col in range (start_num, start_num + 4):
        prod = prod * row[col]
      if( prod > largest_in_row_prod):
        largest_in_row_prod = prod
    if(largest_in_row_prod > greatest_prod):
      greatest_prod = largest_in_row_prod
  
  # read and multiply in blocks of four along columns
  for col in range(dimensions):
    largest_in_col_prod = 0
    for start_num in range (dimensions - 3):
      prod = 1 
      for row in range (start_num, start_num + 4):
        prod = prod * list[row][col]
      if(prod > largest_in_col_prod):
        largest_in_col_prod = prod
    if(largest_in_col_prod > greatest_prod):
      greatest_prod = largest_in_col_prod
  
  # go along all diagonals L to R in blocks of 4
  for row in range (dimensions - 3):
    largest_lr = 0
    for col in range (dimensions - 3):
      prod = 1 
      for k in range (4):
        prod = prod * list[row + k][col + k]
      if(prod > largest_lr):
        largest_lr = prod
    if(largest_lr > greatest_prod):
      greatest_prod = largest_lr

  # go along all diagonals R to L in blocks of 4
  for row in range (dimensions - 3):
    largest_rl = 0
    for col in range(3, dimensions):
      prod = 1
      for k in range (4):
        prod = prod * list[row + k][col - k]
      if(prod > largest_rl):
        largest_rl = prod
    if(largest_rl > greatest_prod):
      greatest_prod = largest_rl
  
  return greatest_prod

def main():
  # open file for reading
  in_file = open("./grid.txt", "r")
  
  # read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int(dim)
  
  # create an empty grid
  grid = []
  
  # populate the grid. n x n matrix
  for n in range (dim):
    line = in_file.readline()
    line = line.strip()
    row = line.split()
    for str in range (dim):
      row[str] = int(row[str])
    grid.append(row)
  
  # close the file
  in_file.close()

      
  # print output
  print()
  print("The greatest product is", max_prod(grid,dim), end = ".")
  print()

main()