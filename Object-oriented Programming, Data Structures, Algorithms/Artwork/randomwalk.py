# Description: Draws a grid and exhibits a random walk

import turtle, random

def main():
  # put label on top of page
  turtle.title ('Random Walk')

  # setup screen size
  turtle.setup (1000, 1000, 0, 0)

  # set turtle speed
  #turtle.speed (1)

  # draw 16 x 16 lattice
  turtle.color ('gray')
  
  # draw horizontal lines
  x = -80
  for y in range (-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto (x, y)
    turtle.pendown()
    turtle.forward (160)

  # draw vertical lines
  y = 80
  turtle.right (90)
  for x in range (-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto (x, y)
    turtle.pendown()
    turtle.forward (160)

  # start random walk
  turtle.pensize(3)
  turtle.color ('red')
 
  turtle.penup()
  turtle.goto(0, 0)
  turtle.pendown()

  x = y = 0
  while (abs(x) < 80 and abs(y) < 80):
    r = random.randint(0, 3)
    if r == 0:
      x += 10
      turtle.setheading(0)
      turtle.forward(10)    
    elif r == 1:
      y -= 10
      turtle.setheading(270)
      turtle.forward(10)    
    elif r == 2:
      x -= 10
      turtle.setheading(180)
      turtle.forward(10)    
    elif r == 3:
      y += 10
      turtle.setheading(90)
      turtle.forward(10)    

  # persist drawing
  turtle.done()

main()