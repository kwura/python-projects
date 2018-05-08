#  Description: Verifies Benford's law by examining the population frequency from a data set.

def main():
  # Create an empty dictionary
  pop_freq = {}
  
  # Initialize the dictionary
  for i in range(1, 10):
    pop_freq[str(i)] = 0
  
  # Open file for reading  
  in_file = open("./Census_2009.txt", "r")
  
  
  # Read header and ignore
  header = in_file.readline()
  
  # Read subsequent lines of data
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    
	# Get the last element that is the population number
    pop_num = pop_data[-1]
    
    # Make entries in the dictionary
    for i in range (1, 10):
      if( pop_num[0] == str(i)):
        pop_freq[str(i)] += 1
  
  # Close the file
  in_file.close()
  
  # Sum the total
  total = 0
  for i in range (1,10):
    total += pop_freq[str(i)]
  
  # Print the output
  print()
  
  print("Digit	Count	%")
  
  for i in range (1,10):
    print(i, "     ", pop_freq[str(i)], "	%.1f" % (float(pop_freq[str(i)]*100/total)))

  
main()
  
