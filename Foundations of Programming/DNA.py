#  Description: Reads a .txt file and determines the longest common DNA sequence(s)


def main():
  # open file for reading
  in_file = open("./dna.txt", "r")
  
  # read the number of pairs
  num_pairs = in_file.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int(num_pairs)
  
  # Formating
  print()
  print("Longest Common Sequences")
  print()
  
  # read each pair of dna strands
  for i in range (num_pairs):
    st1 = in_file.readline()
    st2 = in_file.readline()
	
    st1 = st1.strip()
    st2 = st2.strip()
	
    st1 = st1.upper()
    st2 = st2.upper()
    
    # order the strands by size
    if (len(st1) > len(st2)):
      dna1 = st1
      dna2 = st2 
    else:
      dna1 = st2
      dna2 = st1 
	
	# get all substrands of dna1
    wnd = len(dna1)
    dna1_list =[]
    while(wnd > 1):
      start_idx = 0
      while ((start_idx + wnd) <= len(dna1)):
        sub_strand = dna1[start_idx: start_idx + wnd]
        dna1_list.append(sub_strand)
		# move the window by one
        start_idx += 1
      # decrease the window size
      wnd = wnd - 1
	  
	# get all substrands of dna2
    wnd = len(dna2)
    dna2_list =[]
    while(wnd > 1):
      start_idx = 0
      while ((start_idx + wnd) <= len(dna2)):
        sub_strand = dna2[start_idx: start_idx + wnd]
        dna2_list.append(sub_strand)
		# move the window by one
        start_idx += 1
      # decrease the window size
      wnd = wnd - 1

    # determine the longest common sequence(s) for the two strings
    longest_seq = 0
    lcs_list = []	
    for ss_1 in (dna1_list):
      for ss_2 in (dna2_list):
        if (ss_1 == ss_2):
          if (len(ss_1) > longest_seq):
            longest_seq = len(ss_1)
            lcs_list = []
            lcs_list.append(ss_1)
          elif (len(ss_1) == longest_seq):
            lcs_list.append(ss_1)

    # Bonus. If there are two or more largest DNA sub-strands that are identical, then output only one.
    lcs_bonus = lcs_list
    index = 0
    for item in (lcs_list):
      repeats = lcs_list.count(item)
      if(repeats > 1 and (lcs_list.index(item) < index)):
        lcs_bonus.remove(item)
      index +=1


    # Print the outcome
    pair_str = "Pair " + str(i+1) + ":"
    if (lcs_list == []):
      print(pair_str, "No Common Sequence Found")
    for lcs in (lcs_list):
      if(lcs_list.index(lcs) == 0):
        print(pair_str, "%-80s" % (lcs))
      else:
        print("       ", "%-80s" % (lcs))
    
    if(i < (num_pairs -1)):
      print()
	  
  # close the file  
  in_file.close()
  
main()
