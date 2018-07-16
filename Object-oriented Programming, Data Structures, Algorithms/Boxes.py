#  Description: Applies the concepts of recursion in determining the largest subset of nesting boxes



# create a list that will hold the nested boxes
nested_boxes = []
  
# create a variable for the size of the nested boxes
largest_size = [0]

def does_fit(box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

# get all subsets of boxes
def subsets (a, b, lo):
  hi = len(a)
  if (lo == hi):
  	# for each subset check if they all fit
    stuff = True
    for i in range(len(b)-1):
      stuff = stuff and does_fit(b[i], b[i+1])
    if(stuff and (len(b) >= largest_size[0])):
      largest_size[0] = len(b)
      nested_boxes.append(b)
    return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, b, lo + 1)
    subsets (a, c, lo + 1)

# make sure all subsets have same size
def filter(b):
  a = []
  for i in range(len(b)):
    if(len(b[i]) == largest_size[0]):
      a.append(b[i])
  return a

def main():
  # open file for reading
  in_file = open('boxes.txt', 'r')

  # read number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)

  # create empth list of boxes
  box_list = []

  # read the list of boxes from the file
  for i in range(num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()

    for j in range(len(box)):
      box[j] = int(box[j])
    box.sort()
    box_list.append(box)

  # close the file
  in_file.close()

  # sort the box list
  box_list.sort()

  # get all subsets of boxes
  b = []
  subsets(box_list, b, 0)
  
  # print output
  filtered_boxes = filter(nested_boxes)
  if(largest_size[0] < 2):
    print("No Nesting Boxes")
  else:
    print("Largest Subset of Nesting Boxes")
    for i in range (len(filtered_boxes)):
      for j in range(len(filtered_boxes[i])):
        print(filtered_boxes[i][j])
      print()
main()




