#  Description: Creates a graph topologically


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

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
      
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  def getAdjUnvisitedVertex2 (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert, -1, -1):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)
    # the stack is empty let us reset the falgs
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False


  def dfs2 (self, v):
    edge_help = []
    for i in range(len(self.adjMat)):
      thing = []
      for j in range(len(self.adjMat[i])):
        thing.append(self.adjMat[i][j])
      edge_help.append(thing)
    
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        if(1 in edge_help[theStack.peek()]):
          nVert = len (self.Vertices)
          for i in range (nVert):
            (self.Vertices[i]).visited = False
          return True 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        edge_help[theStack.peek()][u] = "visited"
        theStack.push(u)

    # the stack is empty let us reset the falgs
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    return False


  # do breadth first search in a graph
  def bfs (self, v):
    current = v
    labels = []
    # create a Queue
    theQueue = Queue ()

    # Select a starting vertex. Make it current and mark it visited
    (self.Vertices[v]).visited = True
    print(self.Vertices[v])
    labels.append(self.Vertices[v].label)
    
    # Visit the next unvisited adjacent vertex (in order). 
    # Mark visited and insert into the queue
    u = self.getAdjUnvisitedVertex(v)
    if(u != -1):
      (self.Vertices[u]).visited = True
      print(self.Vertices[u])
      labels.append(self.Vertices[u].label)
      theQueue.enqueue(u)

    # If you cannot carry out step 1, because
    # there are no more unvisited vertices, remove
    # a vertex from the queue (if possible) and
    # make it the current vertex and repeat step 1.
    while(theQueue.isEmpty() == False):
      u = self.getAdjUnvisitedVertex(current)
      if(u != -1):
        (self.Vertices[u]).visited = True
        print(self.Vertices[u])
        labels.append(self.Vertices[u].label)
        theQueue.enqueue(u)
      else:
        if(theQueue.isEmpty() == False):
          current = theQueue.dequeue()

    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    # When the Queue is empty then you are done
    return labels

  # determine if a directed graph has a cycle
  def hasCycle (self):
    good = True
    for i in range(len(self.Vertices)):
      good = good and self.dfs2(i)

    return good

  # return a list of vertices after a topological sort
  def toposort (self):
    if(self.hasCycle() == True):
      return None

    edge_help = []
    for i in range(len(self.adjMat)):
      thing = []
      for j in range(len(self.adjMat[i])):
        thing.append(self.adjMat[i][j])
      edge_help.append(thing)

    topo = []

    while(len(topo) != len(self.Vertices)):
      box = self.topo_help(edge_help)[:]
      topo = box + topo
      if(len(topo) == len(self.Vertices)):
        break

    return topo

  def topo_help(self, edge_help):

    last = []
    for i in range(len(edge_help)):
      zero = True
      for j in range(len(edge_help[i])):
        zero = zero and (edge_help[i][j] == 0)
        if(zero == False):
          break
      if(zero == True):
        last.append(self.Vertices[i].label)
    for h in last:
      idx = self.getIndex(h)
      for k in range(len(edge_help[idx])):
        edge_help[idx][k] = "Done"
        if(edge_help[k][idx]!= "Done"):
          edge_help[k][idx] = 0


    return last


def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  inFile = open ("./topotopo4.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())
  print (numVertices)

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    print (city)
    cities.addVertex (city)

  # read the edges
  numEdges = int ((inFile.readline()).strip())
  print (numEdges)

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    print (edge)
    edge = edge.split()
    start = cities.getIndex(edge[0])
    finish = cities.getIndex(edge[1])
    weight = 1

    cities.addDirectedEdge (start, finish, weight)

  # print the adjacency matrix
  print ("\nAdjacency Matric")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()  


  # close file
  inFile.close()


# -------------------------Testing Below --------------------------------

  # test if a directed graph has a cycle
  print("Is there a cycle:", cities.hasCycle())
  

  # test topological sort
  for i in cities.toposort():
    print(i, end=" ")

  


main()
