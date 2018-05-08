# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

def special_add(first, other):
    if(first == None):
      value1 = 0
    else:
      value1 = first.data
    if(other == None):
      value2 = 0
    else:
      value2 = other.data

    return value1 + value2

def special_mul(first, other):
    if(first == None):
      value1 = 0
    else:
      value1 = first.data
    if(other == None):
      value2 = 0
    else:
      value2 = other.data

    return value1 * value2

class Link (object):
  def __init__ (self, col = 0, data = 0, next = None):
    self.col = col
    self.data = data
    self.next = next

  # return a String representation of a Link (col, data)
  def __str__ (self):
    s = ''
    s += "(%i, " % (self.col) + "%i)" % (self.data)
    return s

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # Search in an ordered list, return None if not found
  def find_ordered (self, col): 
    current = self.first

    if (current == None or current.col > col):
      return None

    while (current.col != col):
      if (current.next == None or current.next.col > col):
        return None
      else:
        current = current.next

    return current 

  def insert_link (self, col, item): 
    new_link = Link(col, item)
    current = self.first

    if (current == None):
      self.first = new_link
      return
    
    elif(current.col > new_link.col):
      new_link.next = self.first
      self.first = new_link
      return

    while(True):
      if(current.next != None):
        if(current.next.col > new_link.col):
          new_link.next = current.next
          current.next = new_link
          return  
        current = current.next
      else:
        current.next = new_link
        return

  def insert_last (self, col, data):
    new_link = Link (col, data)
    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, col):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.col != col):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next
    
    return current

  # return a String representation of a LinkedList
  def __str__ (self):
    s = ''
    current = self.first
    if(self.first != None):
      s += str(current)
      current = current.next
      
      if(current != None):
        s += ", "
      else:
        s += " "

      while(current != None):
        if(current.next != None):
          s += str(current) + ", "
          current = current.next
        else:
          s += str(current)
          current = current.next

    return s

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = []

  # perform assignment operation: matrix[row][col] = data
  def set_element (self, row, col, data):
    focus = self.matrix[row]
    # Scenario 1: value to insert is 0
    if(data == 0):
      focus.delete_link(col)

    # Scenario 2: If element does not exist, create link and insert in place
    elif(focus.find_ordered(col) == None):
      focus.insert_link(col, data)

    # Scenario 3: If value already exists, replace.
    elif(focus.find_ordered(col).data != None):
      focus.find_ordered(col,data).data = data

    return

  # add two sparse matrices
  def __add__ (self, other):
    if ((self.row != other.row) or (self.col != other.col)):
      return None

    mat = Matrix(self.row, self.col)
    for i in range(self.row):
      new_row = LinkedList()
      for j in range(self.col):
        first = self.matrix[i].find_ordered(j)
        second = other.matrix[i].find_ordered(j)
        
        solution = special_add(first, second)
        if(solution != 0):
          new_row.insert_link(j,solution)

      mat.matrix.append(new_row)

    return mat

  # multiply two sparse matrices
  def __mul__ (self, other):
    if (self.col != other.row):
      return None
    
    mat = Matrix(self.row, other.col)
    for i in range(self.row):
      new_row = LinkedList()
      for j in range (other.col):
        sum_mult = 0
        for k in range (other.row):
          first = self.matrix[i].find_ordered(k)
          second = other.matrix[k].find_ordered(j)
          sum_mult += special_mul(first, second)
        if(sum_mult != 0):
          new_row.insert_link(j, sum_mult)
      mat.matrix.append(new_row)
    
    return mat

  # return a list representing a row with the zero elements inserted
  def get_row (self, n):
    if(n >= self.row):
      return None

    rep = []
    ref = self.matrix[n]
    for i in range(self.col):
      search = ref.find_ordered(i)
      if(search == None):
        rep.append(0)
      else:
        rep.append(search.data)

    return rep

  # return a list representing a column with the zero elements inserted
  def get_col (self, n):
    if(n >= self.col):
      return None

    rep = []
    for i in range(self.row):
      ref = self.matrix[i]
      search = ref.find_ordered(n)
      if(search == None):
        rep.append(0)
      else:
        rep.append(search.data)

    return rep

  # return a String representation of a matrix
  def __str__ (self):
    s = ''
    for i in range(self.row):
      ref = self.matrix[i]
      for j in range(self.col):
        search = ref.find_ordered(j)
        if(search == None):
          s += "%i " % (0)
        else:
          s += "%i " % (search.data)
      s += "\n"

    return s

def read_matrix (in_file):
  line = in_file.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)

  for i in range (row):
    line = in_file.readline().rstrip("\n").split()
    new_row = LinkedList()
    for j in range (col):
      elt = int (line[j])
      if (elt != 0):
        new_row.insert_last(j, elt)
    mat.matrix.append (new_row)
  line = in_file.readline()

  return mat

def main():
  in_file = open ("./matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = read_matrix (in_file)
  print (matA)
  matB = read_matrix (in_file)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = read_matrix (in_file)
  print (matP)
  matQ = read_matrix (in_file)
  print (matQ)

  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.set_element (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Elements to a Zero Value")
  matB.set_element (1, 1, 0)
  print (matB)

  print ("\nTest Getting a Row")
  row = matP.get_row(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.get_col(0)
  print (col)
  in_file.close()

main()