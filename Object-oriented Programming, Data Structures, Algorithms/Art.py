import os
import turtle
import math

# neon blue #00e5ff
# neon pink #ff21ec
# aqua green #82ffbe
# draw something recursively

def drawRec(ttl,level,x,y):

  ttl.speed(10)
  if(level >= 1):
    ttl.color('#00e5ff')
    ttl.dot()
    ttl.goto(x,y)
    for i in range(2):
      ttl.forward(level * 30)
      ttl.left(90)
      ttl.dot()
      ttl.forward(level/2) 
      ttl.color('#ff21ec')

    ttl.setposition(x, y)
    dot_distance = level+5
    width = level+2
    height = level+3
  
    ttl.penup()
    ttl.color('#82ffbe')
 
    for y in range(height):
      for i in range(width):
        ttl.dot()
        ttl.forward(dot_distance + 3)
        ttl.color('#82ffbe')
      ttl.backward(dot_distance * width)
      ttl.right(45)
      ttl.color('#ff21ec')
      ttl.forward(dot_distance)
      ttl.left(45)

    ttl.penup()
    ttl.setposition(0, 0)
    ttl.pendown()
    drawRec(ttl,level-1, x+100, y+100)
    ttl.penup()
    ttl.goto(y,x)
    ttl.pendown()
    ttl.color ('black')
    ttl.circle(20,steps = 3)
    drawRec(ttl,level -1, x, y -100)
    drawRec(ttl,level -1, x-100, y)

  
def main():
  # Print the header
  print("Recursive Art")
  print()

  # Prompt the user for level of recursion
  level = int(input("Enter a level of recursion between 1 and 6: "))
  while(level < 1 or level > 6):
    level = int(input("Enter a level of recursion between 1 and 6: "))

  # turtle.tracer(10000)

  # put label on top of page
  turtle.title ("Bersatu Dengan Alam")
  
  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create Turtle object
  ttl = turtle.Turtle()
  # ttl.speed(10)
  
  # Draw it
  drawRec(ttl,level, 0, 0)
  turtle.done()

  # Final lines
  # outName = os.path.basename(__file__)[:-2]+'eps'
  # turtScrn = turtle.getscreen()
  # turtScrn.getcanvas().postscript(file=outName)

main()