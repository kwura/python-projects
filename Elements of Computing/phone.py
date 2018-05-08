def isPhoneNumber(text):
  # Check if phone number is correct length
  if( len(text) != 12 ):
    return False
  
  # Check for hyphens and numeric digits
  for i in range(3):
    if( text[i].isdigit() == False ):
      return False
	  
  if(text[3] != "-"):
    return False
  
  for i in range(4,7):
    if( text[i].isdigit() == False ):
    return False
  
  if( text[7] != "-"):
    return False
  
  for i in range(8, 12):
    if( text[i].isdigit() == False ):
    return False
  
  return True

message = "Hi my name is lillian co you can contact me at 512-555-3434 or call my secretary at 712-555-3432

detectNum = False

def main():
  for i in range len(message):
    clump = message[i:i+12]
    if isPhoneNumber(clump):
      detectNum = True
      print("Phone number found:", clump)
	  
  if detectNum = False:
    print("No phone number could be found!") 
  
  