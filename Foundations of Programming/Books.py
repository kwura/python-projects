#  Description: Examine the representative works of two authors and determine which author's vocabulary is more extensive.

# Create word dictionary from the comprehensive word list
word_dict = {}
def create_word_dict():

  # Open file for reading
  in_file = open("./words.txt", "r")
  
  # Populate the dictionary
  for line in in_file:
    line = line.strip()
    word_dict[line] = 1

  # Close the file
  in_file.close()


# Removes punctuation marks from a string
def parseString (st):
  # Create blank new string 
  new = ""
  
  # Replace punctuation marks with spaces
  punc_list = ['!', '.', ',', '[', ']', '(', ')', '"', '/', '?', ':', ';','-', "'s"] 
  for i in punc_list:
    st = st.replace(i, " ")
  
  # Accept only letters, spaces, and special cases
  for i in range (len(st)):
    if( st[i] == "'" ):
      if( st[i+1].isalpha() ):
        new += st[i]
      else:
        continue	  
    if( st[i].isalpha() or st[i].isspace() ):
      new += st[i]
  
  # Return the new string
  return new 
      

  

# Returns a dictionary of words and their frequencies
def getWordFreq (file):
  # Create an empty dictionary
  freqDic = {}
  
  # Open the file for reading and read line by line through the file
  in_file = open(file, "r", encoding = "utf-8")
  for line in in_file:
    line = line.strip()
    line = parseString(line)
    words_inLine = line.split()
    
    # Add initial entries into the frequency dictionary
    for word in words_inLine:
      if(word in freqDic):
        freqDic[word] += 1
      else:
        freqDic[word] = 1
  
  # Close the file
  in_file.close()
  
  # Remove all words that start with a capital letter
  capital_list = []
  key_list = list(freqDic.keys())
  for word in key_list:
    if( word[0] == word[0].upper() ):
      capital_list.append(word)

  # Check if lowercase version of words are in frequency dictionary or word list
  for word in capital_list:
    if( word.lower() in freqDic ):
      freqDic[word.lower()] += freqDic[word]
    elif( word.lower() in word_dict ):
      freqDic[word.lower()] = freqDic[word]
    del freqDic[word]

  # Return the word frequency dictionary
  return freqDic
  
  
# Compares the distinct words in two dictionaries
def wordComparison (freq1, freq2):
  set1 = set(freq1.keys())
  set2 = set(freq2.keys())
  
  # Determine the unique set of words used by author 1 but not used by author 2
  unique1 = set1 - set2 
  unique2 = set2 - set1
  
  total_1 = 0
  total_2 = 0
  
  # Determine total frequencies of these unique words
  for i in unique1:
    total_1 += freq1[i]
  for i in unique2:
    total_2 += freq2[i]
  
  # Return the statistics of the unique words 
  return len(unique1), len(unique2), total_1, total_2 
  
  

def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic format
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()
  
  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print()
  
  # Get the frequency of words used by the two authors 
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)
  
  # Sum total number of words from frequency dictionary
  sum_1 = 0
  for word in wordFreq1:
    sum_1 += wordFreq1[word]
	
  sum_2 = 0
  for word in wordFreq2:
    sum_2 += wordFreq2[word]
	
  
  # Compare the relative frequency of uncommnon words used by the two authors
  total_dis1, total_dis2, unique_freq_total_1, unique_freq_total_2 = wordComparison (wordFreq1, wordFreq2)
  
  # Print the output
  print(author1)
  print("Total distinct words =", len(wordFreq1))
  print("Total words (including duplicates) =", sum_1)
  print("Ratio (% of total distinct words to total words) =", (len(wordFreq1) / sum_1) * 100)
  
  print()
  print(author2)
  print("Total distinct words =", len(wordFreq2))
  print("Total words (including duplicates) =", sum_2)
  print("Ratio (% of total distinct words to total words) =", (len(wordFreq2) / sum_2) * 100)
  
  print()
  print(author1, "used", total_dis1, "words that", author2, "did not use.")
  print("Relative frequency of words used by", author1, "not in common with", author2, "=", (unique_freq_total_1 / sum_1) * 100)
  
  print()
  print(author2, "used", total_dis2, "words that", author1, "did not use.")
  print("Relative frequency of words used by", author2, "not in common with", author1, "=", (unique_freq_total_2 / sum_2) * 100)
  
   
main()
