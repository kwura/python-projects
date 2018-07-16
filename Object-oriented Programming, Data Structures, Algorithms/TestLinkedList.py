#  Description: Tests several helper methods for the LinkedList class


class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  # initialize
  def __init__ (self):
    self.last = None

  # get number of links 
  def get_num_links (self):
    current = self.first  
    counter = 0
    if (current == None):
      return counter
    
    counter += 1

    while(current.next != None):
      current = current.next
      counter += 1
    
    return counter
    
  # add an item at the beginning of the list
  def insert_first (self, item):
    new_link = Link (item)

    new_link.next = self.first
    self.first = new_link 

  # add an item at the end of a list
  def insert_last (self, item): 
    new_link = Link (item)

    current = self.first
    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

  # add an item in an ordered list in ascending order
  def insert_in_order (self, item): 
    new_link = Link(item)
    current = self.first

    if (current == None):
      self.first = new_link
      return
    
    elif(current.data > new_link.data):
      new_link.next = self.first
      self.first = new_link
      return

    while(True):
      if(current.next != None):
        if(current.next.data > new_link.data):
          new_link.next = current.next
          current.next = new_link
          return  
        current = current.next
      else:
        current.next = new_link
        return
  
  # search in an unordered list, return None if not found
  def find_unordered (self, item):
    current = self.first

    if (current == None):
      return None

    while (current.data != item):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current 

  # Search in an ordered list, return None if not found
  def find_ordered (self, item): 
    current = self.first

    if (current == None or current.data > item):
      return None

    while (current.data != item):
      if (current.next == None or current.next.data > item):
        return None
      else:
        current = current.next

    return current 

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, item):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != item):
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

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    s = ""
    current = self.first

    if(current == None):
      return s
    
    counter = 0
    while(current != None):

      if(counter == 10):
        s += "\n"
        counter = 0

      s += str(current.data) + "  "
      counter += 1
      current = current.next

    return s


  # Copy the contents of a list and return new list
  def copy_list (self):
    new = LinkedList()
    current = self.first
    if(current == None):
      return new

    new.insert_first(current.data)
    while(current.next != None):
      current = current.next
      new.insert_last(current.data)

    return new

  # Reverse the contents of a list and return new list
  def reverse_list (self): 
    new = LinkedList()
    current = self.first
    if(current == None):
      return new

    new.insert_first(current.data)
    while(current.next != None):
      current = current.next
      new.insert_first(current.data)

    return new

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self): 
    new = LinkedList()
    current = self.first
    if(current == None):
      return new

    new.insert_first(current.data)
    while(current.next != None):
      if(current.data > current.next.data):
        new.insert_first(current.next.data)
      else:
        new.insert_last(current.next.data)
      current = current.next

    return new    

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first
    answer = True
    if(current == None or current.next == None):
      return answer

    while(current.next != None):
      if(current.data > current.next.data):
        return False

      current = current.next

    return answer    

  # Return True if a list is empty or False otherwise
  def is_empty (self):
    return self.first == None 

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other):
    new = self.copy_list()
    current = other.first

    while(current != None):
      new.insert_in_order(current.data)
      current = current.next
    return new   

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    track1 = self.first
    track2 = other.first
    if(self.is_empty() and other.is_empty()):
      return True
    elif(self.is_empty() != other.is_empty()):
      return False
    
    tracker = True
    while(track1 != None and track2 != None):
      tracker = tracker and (track1.data == track2.data)
      track1 = track1.next
      track2 = track2.next

    if(track1 != None or track2 != None):
      return False

    return tracker
      
  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
    a = set()
    new = LinkedList()

    current = self.first
    while(current != None):
      if(current.data not in a):
        a.add(current.data)
        new.insert_last(current.data)
      current = current.next
    
    return new

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  test = LinkedList()
  items = int(input("Enter number of links to test string: "))
  print()
  print("|||| insert_first and __str__ test ||||")
  for i in range(items):
    test.insert_first(i)

  print(test)
  print()
  print()
  test = LinkedList()
  thing = int(input("Enter item to insert first: "))
  test.insert_first(thing)
  print()
  print(test)
  print("||||                               ||||")
  print("\n \n")
    
  # Test method insert_last()
  thing = int(input("Enter data to insert last: "))
  print("|||| insert_last and __str__ test ||||")
  test.insert_last(thing)
  print(test)
  print("||||                               ||||")
  print("\n \n")

  # Test method insert_in_order()
  thing = int(input("Enter data to insert in order: "))
  print("|||| insert order test ||||")
  test.insert_in_order(thing)
  print(test)
  print("||||                               ||||")
  print("\n \n")

  # Test method get_num_links()
  print("|||| get num links ||||")
  print(test.get_num_links())
  print()
  print()
  thing = int(input("Enter number of links to see if the same number pops out"))
  test = LinkedList()
  for i in range(thing):
    test.insert_first(i)
  print()
  print("LinkList: ", test, " ", test.get_num_links(), " links")
  print("||||                               ||||")
  print("\n \n")

  # Test method find_unordered() 
  # Consider two cases - item is there, item is not there
  print("From this Linked List what item do you want to look for?", test)
  print()
  item = int(input("Enter data: ")) 
  print("|||| find_unordered test ||||")
  if(test.find_unordered(item) == None):
    print("Sorry bruh couldn't it")
  else:
    print("Yo found it!!!!")
  print("||||                               ||||")
  print("\n \n")

  # Test method find_ordered() 
  # Consider two cases - item is there, item is not there 
  test = LinkedList()
  items = int(input("Enter number of links to test string: "))
  print()
  print("|||| find_unordered test ||||")
  for i in range(items):
    test.insert_in_order(i)
  print(test)
  print("What to find?")
  thing = int(input("Enter data: "))
  if(test.find_ordered(thing) == None):
    print("Sorry bruh couldn't it")
  else:
    print("Yo found it!!!!")
  print("||||                               ||||")
  print("\n \n")

  # Test method delete_link()
  # Consider two cases - item is there, item is not there 
  print("Test to delete")
  print(test)
  thing = int(input("What do you want to delete?"))
  test.delete_link(thing)
  print(test)
  print("\n \n")
  # Test method copy_list()
  print("Copied list")
  copy = test.copy_list()
  print("Test to delete")
  print(test)
  thing = int(input("What do you want to delete?"))
  test.delete_link(thing)
  print(test, "This was test")
  print(copy, "This was copy, is everything working?")

  # Test method reverse_list()
  print("\n \n \n")
  print("This is og test", test)
  print("This is supposed the reversed version, did it work?", test.reverse_list())
  # Test method sort_list()
  print("\n \n \n")
  print("This is the og test", test.reverse_list())
  print("This is supposed the sorted version, did it work?", test.reverse_list().sort_list())

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print("\n \n \n")
  print("This is the og test", test.reverse_list())
  print("is sorted? Test says ", test.reverse_list().is_sorted(), " did it work?")
  print("This is supposed the sorted version, did it work?", test.reverse_list().sort_list(), " test says ", test.reverse_list().sort_list().is_sorted() )
  # Test method is_empty()
  print("\n \n \n")
  empty = LinkedList()
  print("This should be an empty list", empty.is_empty(), "Did it work?")
  print("This should not be empty", test.is_empty(), "Did it work?")
  # Test method merge_list()
  print("This is list 1 ", test)
  print("This is list 2 ", copy.reverse_list())
  print("This is merge. Did it work?", test.merge_list(copy.reverse_list()))

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print("\n \n \n")
  one = LinkedList()
  two = LinkedList()
  print("LL first: ", one)
  print("LL second:", two)
  print("Test 1: Two empty lists. Test results: ", one.is_equal(two))
  print("\n \n \n")
  two.insert_in_order(23)
  print("LL first: ", one)
  print("LL second: ", two)
  print("Test 2: 1 empty list and 1 non empty list. Test results:", one.is_equal(two))
  print("\n \n \n")
  one.insert_in_order(23)
  two.insert_in_order(245)
  one.insert_in_order(245)
  two.insert_in_order(512)
  print("LL first: ", one)
  print("LL second: ", two)
  print("Test 3: 1 list shorter than the other but equal up to that point. Test results:", one.is_equal(two))
  
  three = LinkedList()
  three.insert_first(4)
  three.insert_first(5)
  print("\n \n \n")
  print("LL first: ", one)
  print("LL second: ", three)
  print("Test 4: 1 completely different list. Test results: ", one.is_equal(three))
  print("\n \n \n")
  one.insert_in_order(512)
  print("LL first: ", one)
  print("LL second: ", two)
  print("Last test: two equal lists. Test results: ", one.is_equal(two))  
  # Test remove_duplicates()
  blah = LinkedList()
  print("\n \n \n")
  print(blah)
  print("Case1: empty list", blah.remove_duplicates())
  print("\n \n \n")
  print("OG list: ", one)
  print("Case2: non empty list", one.remove_duplicates())
  print("\n \n \n")
  print("OG list: ", one.merge_list(two))
  print("Case3: non empty list with lots of stuff", one.merge_list(two).remove_duplicates())


if __name__ == "__main__":
  main()