#  Description: Creates an expression tree and methods to evaluate and represent the tree

ops = ["+", "-", "*", "/"]

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  def createTree (self, expr):
    # Create the stack
    theStack = Stack()
    expr = expr.split()
    
    # Create first node
    current = Node(None)
    self.root = current

    for token in expr:
      if(token == "("):
        # Add new node as left child
        new = Node(None)
        current.lChild = new

        # Push current node on stack
        theStack.push(current)

        # Make current node the left child
        current = current.lChild

      elif(token in ops):
        # set current node's data as operator
        current.data = token

        # push current node on stack
        theStack.push(current)

        # Add new node as right child
        new = Node(None)
        current.rChild = new

        # Make current node the right child
        current = current.rChild

      elif(token == ")"):
        if(theStack.isEmpty() == False):
          current = theStack.pop()

      else:
        current.data = token
        current = theStack.pop()

  def evaluate (self, aNode):
    if(aNode != None and aNode.data in ops):
      oper = aNode.data
      if(oper == "+"):
        return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)

      elif(oper == "-"):
        return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)

      elif(oper == "*"):
        return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)

      elif(oper == "/"):
        return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
    else:
      return eval(aNode.data)
    

  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data, end = " ")
      self.preOrder (aNode.lChild)
      self.preOrder (aNode.rChild)
  
  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lChild)
      self.postOrder (aNode.rChild)
      print (aNode.data, end = " ")

def main():
  in_file = open("expression.txt", "r")
  exp = in_file.readline()
  exp = exp.strip()

  exTree = Tree()
  exTree.createTree(exp)
  
  solution =  exTree.evaluate(exTree.root)
  print(exp + " = " + str(solution))

  print()
  print("Prefix Expression:", end = " ")
  exTree.preOrder(exTree.root)

  print()
  print()
  print("Postfix Expression:", end = " ")
  exTree.postOrder(exTree.root)

 
  in_file.close()

main()