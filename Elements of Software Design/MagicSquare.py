'''
  Description: Implements an algorithm to construct the magic n-by-n squares.
'''



# Populate a 2-D list with numbers from 1 to n2
def make_square ( n ):
  # Create a 2-D list with zeros
  square = []
  for row in range(n):
    sub = []
    for col in range(n):
      sub.append(0)
    square.append(sub)
  
  # Place a 1 in the middle bottom row
  square[n - 1][n // 2] = 1
  position = [ n-1 , n // 2]

  # Algorithm
  for i in range(n * n - 1):
    value = i + 2
    position[0] += 1
    position[1] += 1

    if(position[0] > n - 1 and position[1] > n - 1):
      square[n-2][n-1] = value
      position[0] = n - 2
      position[1] = n - 1
      continue

    elif(position[0] > n - 1):
      square[0][position[1]] = value
      position[0] = 0
      continue

    elif(position[1] > n - 1):
      square[position[0]][0] = value
      position[1] = 0
      continue

    elif(square[position[0]][position[1]] == 0):
      square[position[0]][position[1]] = value
      continue

    else:
      position[0] -= 2
      position[1] -= 1
      square[position[0]][position[1]] = value

  return square


# Print the magic square in a neat format where the numbers
# are right justified
def print_square ( magic_square ):
  print('Here is a 5 x 5 magic square:')
  print()
  for i in range(len(magic_square)):
    for j in range(len(magic_square)):

      if(j == len(magic_square) - 1):
        print("%3d" %(magic_square[i][j]))

      else:
        print("%3d" %(magic_square[i][j]), end = " ")

# Check that the 2-D list generated is indeed a magic square
def check_square ( magic_square ):
  n = len(magic_square)
  unique_sum = (n * (n * n + 1)) / 2

  # Check sum of each row
  row_standard = 0
  for i in range(n):
    counter = 0
    for j in range(n):
      counter += magic_square[i][j]
    if(i == 0):
      row_standard = counter
      continue
    elif(row_standard != counter):
      row_standard = counter
      break
  
  print()
  print('Sum of row =', row_standard)

  # Check sum of each column
  col_standard = 0
  for j in range(n):
    counter = 0
    for i in range(n):
      counter += magic_square[i][j]
    if(j == 0):
      col_standard = counter
      continue
    elif(col_standard != counter):
      col_standard = counter
      break

  print('Sum of column =', col_standard)

  # Check sum of each main diagonal
  diagonal_1 = 0
  for i in range(n):
    diagonal_1 += magic_square[i][i]

  print('Sum diagonal (UL to LR) =', diagonal_1)

  diagonal_2 = 0
  for i in range(n):
    diagonal_2 += magic_square[i][n-i-1]

  print('Sum diagonal (UR to LL) =', diagonal_2)


def main():
  # Prompt the user to enter an odd number 3 or greater
  print()
  dim = input('Please enter an odd number: ')

  # Check the user input
  while( dim.isdigit() == False or (int(dim) % 2 == 0 or int(dim) < 3) ):
    dim = input('Please enter an odd number: ')
  dim = int(dim)

  # Create the magic square
  magic_square = make_square(dim)
  
  # Print the magic square
  print()
  print_square(magic_square)

  # Verify that it is a magic square
  check_square(magic_square)

main()