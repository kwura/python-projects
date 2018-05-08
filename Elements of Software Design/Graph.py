#  Description: Tests several functions and algorithms for the Graph class

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

  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()
    labels = []

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    labels.append(self.Vertices[v].label)
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
        labels.append(self.Vertices[u].label)
        theStack.push(u)
    # the stack is empty let us reset the falgs
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    return labels

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
    

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    for i in range(len(self.Vertices)):
      a = self.Vertices[i].label
      if(a == fromVertexLabel):
        start = i 
        break

    for i in range(len(self.Vertices)):
      a = self.Vertices[i].label
      if(a == toVertexLabel):
        finish = i 
        break
    
    if(start == -1 or finish == -1):
      return -1 

    weight = self.adjMat[start][finish]
    if(weight == 0):
      return -1

    return weight

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    l = []
    
    for i in range(len(self.Vertices)):
      a = self.Vertices[i].label
      if(a == vertexLabel):
        index = i 
        break

    for j in range(len(self.adjMat[index])):
      if(self.adjMat[index][j] != 0):
        l.append(j)


    return l

  # get a copy of the list of vertices
  def getVertices (self):
    copy = []
    for i in (self.Vertices):
      copy.append(i.label)
    return copy

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    for i in range(len(self.Vertices)):
      a = self.Vertices[i].label
      if(a == fromVertexLabel):
        start = i 
        break

    for i in range(len(self.Vertices)):
      a = self.Vertices[i].label
      if(a == toVertexLabel):
        finish = i 
        break

    self.adjMat[start][finish] = 0
    self.adjMat[finish][start] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    for i in range(len(self.Vertices)):
      a = self.Vertices[i].label
      if(a == vertexLabel):
        index = i 
        break
    
    self.Vertices.pop(index)

    for j in range(len(self.adjMat[index])):
      self.adjMat[index][j] = 0
      self.adjMat[j][index] = 0


def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  inFile = open ("./graph.txt", "r")

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
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.addDirectedEdge (start, finish, weight)

  # print the adjacency matrix
  print ("\nAdjacency Matric")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()

  # read the starting vertex for dfs and bfs
  startVertex = (inFile.readline()).strip()
  print (startVertex)
  # close file
  inFile.close()

  # get the index of the start Vertex
  startIndex = cities.getIndex (startVertex)
  print (startIndex)

  print("\n ---------------Sanity check test cases below --------------- \n \n")
  # test depth first search
  print ("\nDepth First Search from " + startVertex)
  a = cities.dfs (startIndex)[:]
  print("\n ---------Check--------")
  for i in a:
    print(i)
  print()

  # test breadth first search
  print ("\nBreadth First Search from " + startVertex)
  b = cities.bfs (startIndex)[:]
  print("\n ---------Check--------")
  for i in b:
    print(i)
  print()

  # Test GetEdgeWeight
  print("\n Test get edge weight from Houston to Atlanta")
  print(cities.getEdgeWeight("Houston", "Atlanta"))

  print("\n Test get edge weight from Houston to Los Angeles")
  print(cities.getEdgeWeight("Houston", "Los Angeles"))

  # test get neighbors
  print ("\n get neighbors of" + startVertex)
  c = cities.getNeighbors("Houston")[:]
  print("\n ---------Check--------")
  for i in c:
    print(i)
  print()


  # test get vertices
  print ("\n get vertices test")
  d = cities.getVertices()[:]
  print("\n ---------Check--------")
  for i in d:
    print(i)
  print()

  # test deletion of an edge
  print ("\n delete an edge test")
  cities.deleteEdge("Seattle", "San Francisco")
  print("\n ---------Check--------")
  # print the adjacency matrix
  print ("\nAdjacency Matric")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()


  # test deletion of a vertex
  print ("\n delete a vertex test")
  cities.deleteVertex("Houston")
  print("\n ---------Check--------")
  # print the adjacency matrix
  print ("\nAdjacency Matric")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()

  # print city labels
  print ("\n get vertices test")
  h = cities.getVertices()[:]
  print("\n ---------Check--------")
  for i in h:
    print(i)
  print()
   
if __name__ == "__main__":
  main()
