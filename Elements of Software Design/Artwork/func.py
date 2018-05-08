# Description: Draws users defined functions

import math, turtle

# draw a line from (x1, y1) to (x2, y2)
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# write label at location x, y
def labelPoint (ttl, x, y, label):
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  ttl.write (label)
  ttl.penup()

def drawGridMark (ttl, x, y, isVertical):
  if isVertical :
    drawLine (ttl, x, y + 5, x, y - 5)
  else:
    # if not vertical must be horizontal
    drawLine (ttl, x - 5, y, x + 5, y)

def labelGridPoint (ttl, x, y, isVertical, text):
  if isVertical:
    labelPoint (ttl, x - 20, y - 20, text)
  else:
    labelPoint (ttl, x + 20, y, text)

def drawGridScaled (ttl):  # passes in the turtle object
  # draw the axes
  # instead of a 400 it should be passed as a parameter
  drawLine (ttl, -400, 0, 400, 0) # starts at (-400, 0) Ends at  (400m0)
  drawLine (ttl, 0, 400, 0, -400) # Same interpretation

  # label the x axis
  for x in [-300, -200, -100, 100, 200, 300]:
    # draws tick marks
    drawGridMark (ttl, x, 0, True)
    # draws number
    labelGridPoint (ttl, x, 0, True, (x/100, 0))

  # label the y axis
  for y in [-300, -200, -100, 100, 200, 300]:
    drawGridMark (ttl, 0, y, False)
    labelGridPoint (ttl, 0, y, False, (0, y/100))

# Power of python: can pass in a function as a parameter
# name of function.
def drawFnScaled (ttl, fn, lower, upper, step):
def drawWheel(ttl, x, y, larger_r, smaller_r):
  inc = turtle.Turtle()
  inc.speed(0)
  inc.penup()
  inc.goto(x, y + larger_r - smaller_r)

  inc.color('red')
  ttl.color('red')
  
  ttl.penup()
  ttl.setheading(0)
  
  ttl.goto(x, y)
  ttl.pendown()
  ttl.circle(larger_r, steps = 10000)
  ttl.penup()

  spoke_angle = 5
  for r in range(2):
    for q in range(9):
      inc.goto(x, y + larger_r - smaller_r)
      inc.pendown()
      inc.circle(smaller_r, q * 45, steps = 1000)
      ttl.goto(x, y + smaller_r)
      ttl.pendown()
      ttl.circle(larger_r - smaller_r, spoke_angle, steps = 1000)
      ttl.goto(inc.position())
      inc.penup()
      ttl.penup()
      spoke_angle += 45
      inc.setheading(0)
      ttl.setheading(0)
    spoke_angle = -5

  inc.ht()
  ttl.ht()


def  main():
  # put label on top of page
  turtle.title ('Graphs of Functions')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # draw the grid
  drawGridScaled (ttl)

  # # draw sine finction
  # ttl.pencolor ('red')                            # this is step size
  # drawFnScaled (ttl, math.sin, -math.pi, math.pi, 0.1)

  # # draw cosine function
  # ttl.pencolor ('blue')
  # drawFnScaled (ttl, math.cos, -math.pi, math.pi, 0.1)

  # draw my function
  ttl.pencolor ('purple')
  drawFnScaled (ttl,  myFunc, -math.pi, math.pi, 0.1)
  drawFnScaled (ttl,  myFunc2, -math.pi, math.pi, 0.1)

  # persist drawing
  turtle.done()


main()