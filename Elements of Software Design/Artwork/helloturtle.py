# Description: This program writes out Hello World

import turtle


def main():
  # put label on top of page
  # turtle: name of default object
  turtle.title ('Hello World')

  # setup screen size
  # 1000px x 1000px
  turtle.setup (1000, 1000, 0, 0)
 
  # move turtle to origin
  # turtle go to (0,0)
  turtle.penup()
  turtle.goto (0, 0)

  # set the color to navy
  # hexidecimal
  # turtle.color ('navy')
  turtle.color ('#c91885')

  # write the message
  turtle.write ('Hello World!', font = ('Times New Roman', 36, 'bold'))

  # hide the turtle
  turtle.hideturtle()

  # persist the drawing otherwise it vanishes
  turtle.done()

main()
