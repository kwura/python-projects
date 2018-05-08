import io
def parseString (st):
  # Create blank new string 
  new = ""
  
  # Replace punctuation marks with spaces
  punc_list = ['!', '.', ',', '[', ']', '(', ')', '"', '/', '?', ':', ';', '-', "'s"] 
  for i in punc_list:
    st.replace(i, " ")
  
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
  return print(new) 
      

def main():
  new = ""
  st = "the other way--in short, the period was so far like the present"
  punc_list = ['!', '.', ',', '[', ']', '(', ')', '"', '/', '?', ':', ';','-', "'s"] 
  for i in punc_list:
    print(i)
    st = st.replace(i, " ")
    
  for i in range (len(st)):
    if( st[i] == "'" ):
      if( st[i+1].isalpha() ):
        new += st[i]
      else:
        continue	  
    if( st[i].isalpha() or st[i].isspace() ):
      new += st[i]
  
  print(new)
	 
  
 
main()