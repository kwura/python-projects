'''
  Description: Develops several classes that are fundamental in Geometry and tests these classes with various functions.
'''

import math

class Point (object):
  # constructor 
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  def __str__ (self):
    return '(' + str(self.x) + " , " + str(self.y) + ")"

  # test for equality
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  def does_intersect (self, c):
    distance = self.center.dist(c.center)
    return (distance < (self.radius + c.radius))

   
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  def circle_circumscribes (self, r):
    center_x = (r.ul.x + r.lr.x) / 2
    center_y = (r.ul.y + r.lr.y) / 2
    center_new = Point(center_x, center_y)
    radius_new = center_new.dist(r.ul)
    circle_new = Circle(radius_new, center_new.x, center_new.y)
    return circle_new

  # string representation of a circle
  def __str__ (self):
    if(int(self.radius) == self.radius):
      return '(%.1f' % (self.center.x) + ' , %.1f' % (self.center.y) + ') : %.1f' %(self.radius)
    else:
      return '(%.1f' % (self.center.x) + ' , %.1f' % (self.center.y) + ') : %.2f' %(self.radius)
  # test for equality of radius
  def __eq__ (self, other):
    tol = 1.0e-16
    return abs(self.radius - other.radius) < tol 

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  def length (self):
    return self.lr.x - self.ul.x

  # determine width of Rectangle (distance along the y axis)
  def width (self):
    return self.ul.y - self.lr.y 

  # determine the perimeter
  def perimeter (self):
    return 2*self.width() + 2 * self.length()
  # determine the area
  def area (self):
    return self.width() * self.length()

  # determine if a point is strictly inside the Rectangle
  def point_inside (self, p):
    return (self.ul.x < p.x and p.x < self.lr.x) and (self.ul.y > p.y and p.y > self.lr.y ) 

  # determine if another Rectangle is strictly inside this Rectangle
  def rectangle_inside (self, r):
    return (self.ul.x < r.ul.x and r.lr.x < self.lr.x) and (self.ul.y > r.ul.y and r.lr.y > self.lr.y )

  # determine if two Rectangles overlap (non-zero area of overlap)
  def does_intersect (self, other):
    is_above = self.ul.y < other.lr.y 
    is_below = self.lr.y > other.ul.y
    is_left = self.ul.x  > other.lr.x
    is_right = self.lr.x < other.ul.x
    if(is_above or is_below or is_left or is_right):
      return False
    else:
      return True

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  def rect_circumscribe (self, c):
    # set paramaters for new rectangle
    ul_x = c.center.x - c.radius 
    ul_y = c.center.y + c.radius
    lr_x = c.center.x + c.radius
    lr_y = c.center.y - c.radius

    # initialize new rectangle
    new_rec = Rectangle(ul_x, ul_y, lr_x, lr_y)
    return new_rec

  # give string representation of a rectangle
  def __str__ (self):
    return '(%.1f' % (self.ul.x) + ' , %.1f' % (self.ul.y) + ') : (%.1f' % (self.lr.x) + ' , %.1f)' % (self.lr.y)

  # determine if two rectangles have the same length and width
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs(self.width() - other.width()) < tol) and (abs(self.length() -  other.length()))

def main():
  # open the file geom.txt
  in_file = open('geom.txt', 'r')

  # extract the coordinates of P -- the first two elements of the list are of interest
  line = in_file.readline()
  line = line.strip()
  p_data = line.split()
  p_x = float(p_data[0])
  p_y = float(p_data[1])

  # extract the coordinates of Q -- the first two elements of the list are of interest
  line = in_file.readline()
  line = line.strip()
  q_data = line.split()
  q_x = float(q_data[0])
  q_y = float(q_data[1])

  # create Point objects P and Q
  point_p = Point(p_x, p_y)
  point_q = Point(q_x, q_y)

  # print the coordinates of the points P and Q
  print('Coordinates of P:', point_p)
  print('Coordinates of Q:', point_q) 

  # find the distance between the points P and Q
  print('Distance between P and Q: %.2f' % (point_p.dist(point_q)))
 
  # extract the center and radius of C -- the first three elements of the list are of interest
  line = in_file.readline()
  line = line.strip()
  c_data = line.split()
  c_x = float(c_data[0])
  c_y = float(c_data[1])
  c_radius = float(c_data[2])

  # extract the center and radius of C -- the first three elements of the list are of interest
  line = in_file.readline()
  line = line.strip()
  d_data = line.split()
  d_x = float(d_data[0])
  d_y = float(d_data[1])
  d_radius = float(d_data[2])


  # create two Circle objects C and D
  cir_c = Circle(c_radius, c_x, c_y)
  cir_d = Circle(d_radius, d_x, d_y)

  # print C and D
  print('Circle C:', cir_c)
  print('Circle D:', cir_d)

  # compute the circumference of C
  print('Circumference of C: %.2f' % (cir_c.circumference()))

  # compute the area of D
  print('Area of D: %.2f' % (cir_d.area()))

  # determine if P is strictly inside C
  if(cir_c.point_inside(point_p)):
    p_in_c = 'is'
  else:
    p_in_c = 'is not'

  print('P %s inside C' % (p_in_c))

  # determine if C is strictly inside D
  if(cir_d.circle_inside(cir_c)):
    c_in_d = 'is'
  else:
    c_in_d = 'is not'

  print('C %s inside D' % (c_in_d))

  # determine if C and D intersect (non zero area of intersection)
  if(cir_d.does_intersect(cir_c)):
    c_intersect_d = 'does'
  else:
    c_intersect_d = 'does not'

  print('C %s intersect D' % (c_intersect_d))

  # determine if C and D are equal (have the same radius)
  if(cir_c == cir_d):
    c_equal_d = 'is'
  else:
    c_equal_d = 'is not'

  print('C %s equal to D' % (c_equal_d))

  # extract the ul and lr coordinates of rectangle G -- the first four elements of the list are of interest
  line = in_file.readline()
  line = line.strip()
  g_data = line.split()
  g_ulx = float(g_data[0])
  g_uly = float(g_data[1])
  g_lrx = float(g_data[2])
  g_lry = float(g_data[3])

  # extract the ul and lr coordinates of rectangle H -- the first four elements of the list are of interest
  line = in_file.readline()
  line = line.strip()
  h_data = line.split()
  h_ulx = float(h_data[0])
  h_uly = float(h_data[1])
  h_lrx = float(h_data[2])
  h_lry = float(h_data[3])

  # create two rectangle objects G and H
  g_rec = Rectangle(g_ulx, g_uly, g_lrx, g_lry)
  h_rec = Rectangle(h_ulx, h_uly, h_lrx, h_lry)

  # print the two rectangles G and H
  print('Rectangle G:', g_rec)
  print('Rectangle H:', h_rec)

  # determine the length of G (distance along x axis)
  print('Length of G:', g_rec.length())

  # determine the width of H (distance along y axis)
  print('Width of H:', h_rec.width())

  # determine the perimeter of G
  print('Perimeter of G:', g_rec.perimeter())
  # determine the area of H
  print('Area of H:', h_rec.area())

  # determine if point P is strictly inside rectangle G
  if(g_rec.point_inside(point_p)):
    p_in_g = 'is'
  else:
    p_in_g = 'is not'

  print('P %s inside G' % (p_in_g))

  # determine if rectangle G is strictly inside rectangle H
  if(h_rec.rectangle_inside(g_rec)):
    g_in_h = 'is'
  else:
    g_in_h = 'is not'

  print('G %s inside H' % (g_in_h))

  # determine if rectangles G and H overlap (non-zero area of overlap)
  if(h_rec.does_intersect(g_rec)):
    g_intersect_h = 'does'
  else:
    g_intersect_h = 'does not'

  print('G %s overlap H' % (g_intersect_h))

  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  print('Circle that circumscribes G:', Circle.circle_circumscribes(Circle, g_rec))

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  print('Rectangle that circumscribes D:', Rectangle.rect_circumscribe(Rectangle, cir_d))

  # determine if the two rectangles have the same length and width
  if(g_rec == h_rec):
    g_equal_h = 'is'
  else:
    g_equal_h = 'is not'

  print('Rectangle G %s equal to H' % (g_equal_h))

  # close the file geom.txt
  in_file.close()

main()