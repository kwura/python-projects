#  Description: Creates and tests methods for Circular Linked Lists


class Link(object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
  
  def __str__ (self):
    return str(self.data)

class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.last = None
    self.first = None

  # Insert an element (value) in the list
  def insert ( self, item ):
    new_link = Link(item)

    current = self.last
    if(self.first == None):
      self.first = new_link
      return

    elif(current == None):
      self.last = new_link
      self.first.next = self.last
      self.last.next = self.first
      return
    
    new_link.next = current.next
    current.next = new_link
    self.last = new_link


  # Find the link with the given key (value)
  def find ( self, key ):
    current = self.first
    if (current == None):
      return None
    
    elif(current.data == key):
      return current

    elif(current.next == None):
      return None

    current = current.next

    while (current != self.first):
      if (current.data == key):
        return current
      current = current.next

    return None

  # Delete a link with a given key (value)
  def delete ( self, key ):
    previous = self.last
    current = self.first
    
    # empty LL
    if (current == None):
      return None
    
    # If the first link was the link
    elif(current.data == key):
      if(current.next != previous):
        previous.next = current.next
        self.first = previous.next
        return current
      else:
        self.first = previous
        self.first.next = None
        self.last = None
        return current
    
    elif(current.next == None ):
      return None

    previous = current
    current = current.next

    while (current != self.first):
      if (current.data == key):
        previous.next = current.next
        if(current == self.last):
          self.last = previous
        return current
      else:
        previous = current
        current = current.next

    return None

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
    for i in range(n - 1):
      start = start.next
    new = start.next
    self.delete(start.data)
    return new

  # Return a string representation of a Circular List
  def __str__ ( self ):
    s = ""
    current = self.first

    if(current == None):
      return s
    
    counter = 0

    s += str(current.data) + " "
    counter += 1
    current = current.next

    while(current != self.first):
      if(current == None):
        break
      
      elif(counter == 10):
        s += "\n"
        counter = 0

      s += str(current.data) + "  "
      counter += 1
      current = current.next

    return s

def main():
  
  # Open the file and extract information
  in_file = open("josephus.txt", "r")

  # Number of soldiers
  num = int(in_file.readline().strip())

  # Starting soldier
  start = int(in_file.readline().strip())

  # elimination number
  step = int(in_file.readline().strip())
  
  # Solve Josephus problem
  game = CircularList()

  for i in range(1, num +1 ):
    game.insert(i)

  
  # Solve Josephus's problem
  current = game.find(start)
  for i in range(num - 1):
    to_delete = current
    for j in range(step -1 ):
      to_delete = to_delete.next
    current = game.delete_after(current, step)
    print(to_delete.data)

  print(game)

  # close file
  in_file.close()
  
main()