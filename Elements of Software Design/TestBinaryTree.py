#  Description: Adds additional fundfctionality to the binary tree class


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # determine the size of the queue
  def size (self):
    return (len (self.queue))

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))


class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # search for a node with a key
  def search (self, key):
    current = self.root
    while (current != None) and (current.data != key):
      if (key < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current

  # insert a node in a tree
  def insert (self, val):
    new_node = Node (val)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (val < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order(aNode.rchild)

  # pre order traversal - center, left, right
  def pre_order (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.pre_order (aNode.lchild)
      self.pre_order (aNode.rchild)

  # post order traversal - left, right, center
  def post_order (self, aNode):
    if (aNode != None):
      self.post_order (aNode.lchild)
      self.post_order (aNode.rchild)
      print (aNode.data)

  # return the node with minimum value
  def min_node (self):
    current = self.root

    if (current == None):
      return None

    while (current.lchild != None):
      current = current.lchild

    return current



  # return the node with maximum value
  def max_node (self):
    current = self.root
    
    return current
      

  # delete a node with a given key
  def delete (self, key):
    delete_node = self.root
    parent = self.root
    is_left = False

    # if empty tree
    if (delete_node == None):
      return None

    # find the delete node
    while (delete_node != None) and (delete_node.data != key):
      parent = delete_node
      if (key < delete_node.data):
        delete_node = delete_node.lchild
        is_left = True
      else:
        delete_node = delete_node.rchild
        is_left = False

    # if node not found
    if (delete_node == None):
      return None

    # check if delete node is a leaf node
    if (delete_node.lchild == None) and (delete_node.rchild == None):
       if (delete_node == self.root):
         self.root = None
       elif (is_left):
         parent.lchild = None
       else: 
         parent.rchild = None

    # delete node is a node with only a left child
    elif (delete_node.rchild == None):
      if (delete_node == self.root):
        self.root = delete_node.lchild
      elif (is_left):
        parent.lchild = delete_node.lchild
      else:
        parent.rchild = delete_node.lchild

    # delete node has both left and right children
    else:
      # find delete node's successor and the successor's parent node
      successor = delete_node.rchild
      successor_parent = delete_node

      while (successor.lchild != None):
        successor_parent = successor
        successor = successor.lchild

      # successor node is right child of delete node
      if (delete_node == self.root):
        self.root = successor
      elif (is_left):
        parent.lchild = successor
      else:
        parent.rchild = successor

      # connect delete node's left child to be the successor's left child
      successor.lchild = delete_node.lchild

      # successor node left descendant of delete node
      if (successor != delete_node.rchild):
        successor_parent.lchild = successor.rchild
        successor.rchild = delete_node.rchild

      return delete_node

# Below are the additional methods

  # Returns true if two binary trees are similar
  def is_similar_assistant(self, aNode, bNode):
    # base case bruh
    if(aNode == None and bNode == None):
 
      return True
    
    # If one exists and the other doesn't
    elif(aNode != None and bNode == None):
      return False

    elif(aNode == None and bNode != None):
      return False

    # If one is a leaf and the other isn't
    elif(aNode.rchild == None and aNode.lchild == None):
      if(bNode.rchild != None or bNode.lchild != None):
 
        return False

    elif(bNode.rchild == None and bNode.lchild == None):
      if(aNode.rchild != None or aNode.lchild != None):
        return False    

    # If their data doesn't match up
    elif(aNode.data!= bNode.data):
      return False
    
    return (self.is_similar_assistant(aNode.lchild, bNode.lchild) and (self.is_similar_assistant(aNode.rchild, bNode.rchild) and aNode.data == bNode.data))

  def is_similar (self, pNode):
    return self.is_similar_assistant(self.root, pNode.root)

  # Prints out all nodes at the given level
  # Breadth first search
  def print_level (self, level):
    s = ""
    current = self.root
    # tree is empty
    if(current == None):
      print(s)
      return
    
    # level 1
    if(level == 1):
      s += str(current.data) + " "
      print(s)
      return
    
    theQ = Queue()

    if(current.lchild != None):
      theQ.enqueue(current.lchild)
    if(current.rchild != None):
      theQ.enqueue(current.rchild)
    
    # level 2
    if(level == 2):
      track_q_size = theQ.size()
      for i in range(track_q_size):
        current = theQ.dequeue()
        s += str(current.data) + " "
      print(s)
      return
    
    # levels greater than 2
    else:
      # add the target nodes into the queue
      for i in range(level - 2):
        track_q_size = theQ.size()
        for j in range(track_q_size):
          current = theQ.dequeue()
          if(current.lchild != None):
            theQ.enqueue(current.lchild)
          if(current.rchild != None):
            theQ.enqueue(current.rchild)

      # print the target nodes
      while(theQ.is_empty() == False):
        s += str(theQ.dequeue().data) + " "

      print(s)

  # Returns the height of the tree
  def get_height_assistant(self, aNode, height, counter):
    if(aNode == None or (aNode.lchild == None and aNode.rchild == None)):
      if(height > counter[0]):
        counter[0] = height
    else:
      self.get_height_assistant(aNode.lchild, height + 1, counter) 
      self.get_height_assistant(aNode.rchild,height + 1, counter)

  def get_height (self):
    counter = [0]
    self.get_height_assistant(self.root, 0, counter)

    return counter[0]

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes_assistant(self, aNode):
    if(aNode == None):
      return 0
    else:
      return 1 + self.num_nodes_assistant(aNode.lchild) + self.num_nodes_assistant(aNode.rchild)

  def num_nodes (self):
    return self.num_nodes_assistant(self.root)


def main():
  # Create three trees - two are the same and the third is different
  atree = Tree()
  btree = Tree()
  ctree = Tree()
  g = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
  for j in g:
    atree.insert(j)
    btree.insert(j)

  for i in range(7):
    ctree.insert(i + 17)
    ctree.insert(i + 2)

  # Test your method is_similar()
  print("\n \n")
  print("Tree A and Tree B should be similar. Test result: ", atree.is_similar(btree))
  print("Tree A and Tree C should not be similar. Test result: ", atree.is_similar(ctree))
  print("Tree B and Tree C should not be similar. Test result: ", btree.is_similar(ctree))

  # Print the various levels of two of the trees that are different
  print("\n \n Tree A")
  print("___Level 1___ : ", end = " ")
  atree.print_level(1)
  print("\n \n")
  print("___Level 2___ : ", end = " ")
  atree.print_level(2)
  print("\n \n")
  print("___Level 3___ : ", end = " ")
  atree.print_level(3)
  print("\n \n")
  print("___Level 4___ : ", end = " ")
  btree.print_level(4)
  print("\n \n")

  print("\n \n Tree B")
  print("___Level 1___ : ", end = " ")
  btree.print_level(1)
  print("\n \n")
  print("___Level 2___ : ", end = " ")
  btree.print_level(2)
  print("\n \n")
  print("___Level 3___ : ", end = " ")
  btree.print_level(3)
  print("\n \n")
  print("___Level 4___ : ", end = " ")
  btree.print_level(4)
  print("\n \n")

  print("\n \n Tree c")
  print("___Level 1___ : ", end = " ")
  ctree.print_level(1)
  print("\n \n")
  print("___Level 2___ : ", end = " ")
  ctree.print_level(2)
  print("\n \n")
  print("___Level 3___ : ", end = " ")
  ctree.print_level(3)
  print("\n \n")


  # Get the height of the two trees that are different
  print("\n \n Tree A")
  print("height: ", end = " ")
  print(atree.get_height())
  print("\n \n") 

  print("\n \n Tree B")
  print("height: ", end = " ")
  print(btree.get_height())
  print("\n \n") 

  print("\n \n Tree C")
  print("height: ", end = " ")
  print(ctree.get_height())
  print("\n \n") 

  # Get the total number of nodes a binary search tree
  print("\n \n Tree A")
  print("numnodes: ", end = " ")
  print(atree.num_nodes())
  print("\n \n") 

  print("\n \n Tree b")
  print("numnodes: ", end = " ")
  print(btree.num_nodes())
  print("\n \n") 

  print("\n \n Tree c")
  print("numnodes: ", end = " ")
  print(ctree.num_nodes())
  print("\n \n") 

main()