#  Description: Illustrates a train using math functions and the turtle graphics package.


import turtle, math

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

# draw the wheels
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

# draw semicircles above wheels
def draw_semi_circles(ttl):
  ttl.color("blue")
  ttl.penup()
  ttl.goto(-316, -90)
  ttl.setheading(90)
  ttl.pendown()
  ttl.circle(-93, extent = 180 )

  ttl.penup()
  ttl.goto(-97.5, -90)
  ttl.setheading(90)
  ttl.pendown()
  ttl.circle(-92, extent = 180)

  ttl.penup()
  ttl.goto(108, -90)
  ttl.setheading(90)
  ttl.pendown()
  ttl.circle(-92, extent = 180)

# Connect the semi circles
def connect_semi_circles(ttl):
  ttl.color("blue")
  # left to right
  drawLine(ttl, -316, -90,-336, -90)
  drawLine(ttl, -130, -90,-97.5, -90)
  drawLine(ttl, 86.5, -90, 108, -90)
  drawLine(ttl, 292, -90, 315, -90)

# Draw left hand side of train
def left_box(ttl):
  # Left wall
  drawLine(ttl, -336, -90, -336, 210)

  # close the top
  drawLine(ttl, -336, 210, -110, 210)

  # right wall
  drawLine(ttl, -110, 210, -110, -90)

  # draw the windows
  ttl.penup()
  # left window
  ttl.goto (-326, 200)
  ttl.pendown()
  ttl.begin_fill()
  ttl.color ('grey')
  grey = True
  for i in range (2):
    drawLine(ttl,-316, 180, -233,180)
    drawLine(ttl,-233,180, -233,100)
    drawLine(ttl,-233,100, -316,100)
    drawLine(ttl,-316,100, -316, 180)
    if(grey):
      ttl.end_fill()
      grey = False
    ttl.color('blue')

  ttl.penup()
  # right window
  ttl.goto (-203, 180)
  ttl.pendown()
  ttl.begin_fill()
  ttl.color ('grey')
  grey = True
  for i in range (2):
    drawLine(ttl,-203, 180, -120,180)
    drawLine(ttl,-120,180, -120,100)
    drawLine(ttl,-120,100, -203,100)
    drawLine(ttl,-203,100, -203, 180)
    if(grey):
      ttl.end_fill()
      grey = False
    ttl.color('blue')

  # top rectangle
  drawLine(ttl, -336, 210,-351, 210)
  drawLine(ttl, -351, 210,-351, 230)
  drawLine(ttl, -351, 230,-95, 230)
  drawLine(ttl, -95, 230,-95, 210)
  drawLine(ttl, -95, 210,-110, 210)

def right_side(ttl):
  # draw roof
  drawLine(ttl, -110, 180, 315,180)

  # close the right side
  drawLine(ttl, 315,180, 315, -150 )

  # bottom right trapezoid
  drawLine(ttl, 315, -150, 370, -150)
  drawLine(ttl, 370, -150, 340, -60)
  drawLine(ttl, 340, -60, 315, -60)

  # two rectangles to the right
  drawLine(ttl, 315, -45, 325, -45)
  drawLine(ttl, 325, -45, 325, 165)
  drawLine(ttl, 325, 165, 315, 165)
  drawLine(ttl, 325, 40, 330, 40)
  drawLine(ttl, 330, 40, 330, 80)
  drawLine(ttl, 330, 80, 325, 80)

def top_side(ttl):
  # chimneys
  drawLine(ttl, -10, 180, -10, 205)
  drawLine(ttl, -10, 205, 30, 205)
  drawLine(ttl, 30, 205, 30, 180)
  drawLine(ttl, 0, 205, 0, 215)
  drawLine(ttl, 0, 215, 20, 215)
  drawLine(ttl, 20, 215, 20, 205)

  drawLine(ttl, 100, 180, 75, 240)
  drawLine(ttl, 75, 240, 150, 240)
  drawLine(ttl, 150, 240, 125, 180)
  drawLine(ttl, 75, 240, 101.5, 260)
  drawLine(ttl, 101.5, 260, 123.5, 260)
  drawLine(ttl, 123.5, 260, 150, 240)

def dotted_stuff(ttl):
  # horizontal
  drawLine(ttl, -110, 75, 315,75)
  drawLine(ttl, -110, 55, 315,55)
  
  # Filled in dots
  i = 1
  while(i < 410):
    ttl.penup()
    ttl.goto (-112 + i , 65)
    ttl.pendown()
    ttl.begin_fill()
    ttl.color ('black')
    ttl.circle (4)
    ttl.end_fill()
    i += 15

  # vertical
  drawLine(ttl, -70, 180, -70, 75)
  drawLine(ttl, -50, 180, -50, 75)
  drawLine(ttl, 115, 180, 115, 75)
  drawLine(ttl, 135, 180, 135, 75)

  # Filled in dots
  i = 1
  while(i < 99):
    ttl.penup()
    ttl.goto (-62 , 85 + i)
    ttl.pendown()
    ttl.begin_fill()
    ttl.color ('black')
    ttl.circle (4)
    ttl.end_fill()
    i += 15
  i = 1
  while(i < 99):
    ttl.penup()
    ttl.goto (120 , 85 + i)
    ttl.pendown()
    ttl.begin_fill()
    ttl.color ('black')
    ttl.circle (4)
    ttl.end_fill()
    i += 15

def draw_tracks(ttl):
  ttl.color("black")
  drawLine(ttl, -400, -215, 400, -215)
  drawLine(ttl, -400, -240, 400, -240)
  
  counter = 0
  while(counter <800):
    drawLine(ttl, -350 + counter, -240, -350 + counter, -260)
    drawLine(ttl, -350 + counter, -260, -315 + counter, -260)
    drawLine(ttl, -315 + counter, -260, -315 + counter, -240)
    counter += 75



  

def main():
  # put label on top of page
  # turtle: name of default object
  turtle.title ('Train Choo Choo')

  # setup screen size
  # 800px x 800px
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()
  ttl.speed(10000)
  ttl.pensize(3)

  # Draw the semicircles above the wheels
  draw_semi_circles(ttl)

  # Connect the semi circles
  connect_semi_circles(ttl)

  # Draw left hand side of train
  left_box(ttl)

  # Draw right hand side of train
  right_side(ttl)

  # Draw top side of train
  top_side(ttl)

  # Draw the dotted lines
  dotted_stuff(ttl)

  # Draw the tracks
  draw_tracks(ttl)

  # draw the left wheel, the middle wheel, and the right wheel
  drawWheel(ttl, -225, -215 , 87.65625, 15.33984375)
  drawWheel(ttl, 0, -215 ,75, 13.125)
  drawWheel(ttl, 200, -215, 75, 13.125)

  
  
  # persist the drawing otherwise it vanishes
  turtle.done()


main()