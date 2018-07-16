def left_triangle(grid):
  new = []
  for i in range(len(grid)-1):
    new.append(grid[i+1][:-1])
  return new

def right_triangle(grid):
  new = []
  for i in range(len(grid)-1):
    new.append(grid[i+1][1:])
  return new

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

def main():
  triangle = read_file()
  print(right_triangle(triangle))
  print(left_triangle(triangle))

main()