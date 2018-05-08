#  Description: Encrypts and decrypts simple strings using a binary search tree

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None
    # Populate the tree
    key = encrypt_str.lower()
    for i in key:
      if(i == " " or i.isalpha() ):
        self.insert(i)


  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    new_node = Node (ch)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if(ch == current.data):
          return

        elif (ch < current.data):
          current = current.lchild

        else:
          current = current.rchild

      if (ch < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    encoded_ch = ""

    current = self.root

    if(current.data == ch):
      encoded_ch += "*"
      return encoded_ch
    
    while (current != None) and (current.data != ch):
      if (ch < current.data):
        encoded_ch += "<"
        current = current.lchild
      else:
        encoded_ch += ">"
        current = current.rchild

    return encoded_ch

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current = self.root
    if(current == None):
      return ""

    if(st == "*"):
      return current.data

    for i in st:
      if( i == "<"):
        current = current.lchild

      elif( i == ">"):
        current = current.rchild

      if(current == None):
        return ""

    return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    new = st.lower()
    output = ""

    for i in new:
      if(i == " " or i.isalpha()):
        output += self.search(i) 
        output += "!"

    return output[:-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    new = st.split("!")
    output = ""
    for i in new:
      output += self.traverse(i)
      
    return output

def main():
  # Prompt user to enter encryption key
  key = input("Enter encryption key: ")
  print()

  # Create a binarysearchtree object
  key_tree = Tree(key)

  # Prompt user to enter string to be encrypted 
  encrypt_input = input("Enter string to be encrypted: ")

  # Return and print the encrypted string
  print("Encrypted string: " + key_tree.encrypt(encrypt_input))
  print()

  # Prompt user to enter string to be decrypted:
  decrypt_input = input("Enter string to be decrypted: ")
  print("Decrypted string: " + key_tree.decrypt(decrypt_input))

main()
  