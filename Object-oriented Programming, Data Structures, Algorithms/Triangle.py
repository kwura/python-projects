#  Description: Finds the greatest path sum of a triangle of numbers using several types of algorithms.

import time

# global variable for exhaustive search
exhaustive_greatest_sum = 0

# helper for exhaustive search
def searcher(grid, row, index, sum):
  global exhaustive_greatest_sum
  # base case
  if(row > len(grid) - 1):
    if(sum > exhaustive_greatest_sum):
      exhaustive_greatest_sum = sum
  # recursive method
  else:
    sum += grid[row][index]
    searcher(grid, row + 1, index, sum)
    searcher(grid, row + 1, index +1, sum)

# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
  searcher(grid, 0, 0, 0)
  return exhaustive_greatest_sum

# returns the greatest path sum using greedy approach
def greedy (grid):
  total = grid[0][0]
  row = 1
  idx = 0 
  while(row < len(grid)):
    if(grid[row][idx] >= grid[row][idx + 1]):
      total += grid[row][idx]
      row += 1
    else:
      total += grid[row][idx+1]
      row += 1
      idx += 1

  return total 

# returns the greatest path sum using divide and conquer (recursive) approach
def dc(grid):
  if(len(grid) == 1):
    return grid[0][0]
  else:
    left_triangle = [number[:-1] for number in grid[1:]]
    right_triangle= [number[1:] for number in grid[1:]]
    return grid[0][0] + max(dc(left_triangle), dc((right_triangle)))

def rec_search (grid):
  return dc(grid)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  new = grid[:]
  for i in range(len(new)-2,-1,-1):
    for j in range(len(new[i])):
      sum1 = new[i+1][j] + new[i][j]
      sum2 = new[i+1][j+1] + new[i][j]
      new[i][j] = max(sum1,sum2)

  return new[0][0], new

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # open file for reading
  in_file = open('triangle.txt','r')
  
  # read the first line for the number of rows
  line = in_file.readline()
  line = line.strip()
  num_rows = int(line)

  # create empty 2d list for the triangle
  triangle = []

  # read triangular grid from file
  for i in range(num_rows):
  	line = in_file.readline()
  	line = line.strip()
  	row = line.split()

  	for j in range(len(row)):
  		row[j] = int(row[j])
  	triangle.append(row)

  return triangle 

def main ():
  # read triangular grid from file
  triangle = read_file()

  ti = time.time()
  # output greates path from exhaustive search
  es_ouput = exhaustive_search(triangle)
  tf = time.time()
  del_t = tf - ti

  # print time taken using exhaustive search
  print('The greatest path sum through exhaustive search is %i.' % (es_ouput))
  print('The time taken for exhaustive search is %f seconds' %(del_t))
  print()

  ti = time.time()
  # output greates path from greedy approach
  greedy_ouput= greedy(triangle)
  tf = time.time()
  del_t = tf - ti

  # print time taken using greedy approach
  print('The greatest path sum through greedy search is %i.' % (greedy_ouput))
  print('The time taken for greedy approach is %f seconds' %(del_t))
  print()

  ti = time.time()
  # output greates path from divide-and-conquer approach
  d_and_c_ouput = rec_search(triangle)
  tf = time.time()
  del_t = tf - ti

  # print time taken using divide-and-conquer approach
  print('The greatest path sum through recursive search is %i.' % (d_and_c_ouput))
  print('The time taken for recursive search is %f seconds' %(del_t))
  print()

  ti = time.time()
  # output greates path from dynamic programming
  dynamic_output, new_triangle = dynamic_prog(triangle) 
  tf = time.time()
  del_t = tf - ti

  # print time taken using dynamic programming
  print('The greatest path sum through dynamic programming is %i.' % (dynamic_output))
  print('The time taken for dynamic programming is %f seconds' %(del_t))
  print()

if __name__ == "__main__":
  main()

