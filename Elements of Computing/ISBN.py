#  Description: Verifies the correctness of ISBNs and writes a new .txt file


# Function to check whether input is valid
def is_valid(n):
  if((n.endswith("X")== False and  n[-1].isdigit() == False) or (n[0:-1].isdigit() == False) or (len(n) != 10)): 
    return False
  else:
    return True

# Main Function
def main():
  # open file for reading
  in_file = open("./isbn.txt", "r")

  # open output file
  out_file = open("./isbnOut.txt", "w")
  
  # read each isbn 
  for line in in_file:
    og_str = line.strip()
    str = og_str
    str = str.replace("-", "")
    str = str.upper()
	
    # check if isbn is invalid
    if(is_valid(str) == False):
      out_file.write(og_str + "  invalid \n")
      continue
    
    # Store the digits and the character "X" into a list
    s1 = []
    s2 = []
    isbn_list = []
    for index in range (len(str)):
      if((str[index] == "X")):
        isbn_list.append(10)
      else:
        isbn_list.append(int(str[index]))
    
	# compute the partial sums for s1
    sum_count = 0
    for digit in isbn_list:
      sum_count += digit
      s1.append(sum_count)
    
    # compute the partial sums for s2	
    sum_count = 0
    for digit in s1:
      sum_count += digit
      s2.append(sum_count)
    
    # final validity check and output	
    if (s2[-1]%11 != 0):
      out_file.write(og_str + "  invalid \n")
    else:
      out_file.write(og_str + "  valid \n")

  # close the files
  in_file.close()
  out_file.close()
	

main()