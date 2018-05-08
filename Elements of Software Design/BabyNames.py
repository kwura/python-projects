#  Description: Allows a user to query a data base of the 1000 most popular baby names (US) for the past 11 decades 


import urllib.request
# Decades
decade = [1900, 1910, 1920, 1930, 1940,1950, 1960, 1970, 1980, 1990, 2000]

# Create and fill a dictionary with the baby names
baby_dict = {}

def create_baby_dict():
  # Open file for reading
  try:
    baby_file = urllib.request.urlopen("http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt")
  except Exception:
    print('Sorry buddy we encountered an error when trying to open the url. Goodbye.')
    return

  # Populate the dictionary
  for line in baby_file:
    line = line.strip()
    line = str(line, encoding = 'utf8')
    line = line.replace(' 0', ' 1001')
    record = line.split()
    name = record[0]
    rankings = record[1:]
    for i in range (len(rankings)):
      rankings[i] = int(rankings[i])
    baby_dict[name] = rankings[:] 

  # Close the file
  baby_file.close()

# Display menu choices
def queries():
  print()
  print('Options:')
  print('Enter 1 to search for names.')
  print('Enter 2 to display data for one name.')
  print('Enter 3 to display all names that appear in only one decade.')
  print('Enter 4 to display all names that appear in all decades.')
  print('Enter 5 to display all names that are more popular in every decade.')
  print('Enter 6 to display all names that are less popular in every decade.')
  print('Enter 7 to quit.')
  print()

def query_1(name):
  if(name in baby_dict):
  	print('The matches with their highest ranking decade are: ')
  	ranks = baby_dict[name]
  	max_rank = min(ranks)
  	index = ranks.index(max_rank)
  	if(ranks.count(max_rank) > 1):
  	  for i in range(index, len(ranks)):
  	    if(ranks[i] == max_rank):
  	      print(name + ' ' + str(decade[i]))
  	else:
  		print(name + ' ' + str(decade[index]))
  else:
  	print(name + " does not appear in any decade.")

def query_2(name):
  if(name in baby_dict):
    record = name + ':'
    for i in range(len(baby_dict[name])):
      record += ' ' + str(baby_dict[name][i])
    print(record)

    for i in range(len(baby_dict[name])):
      print(str(decade[i]) + ': ' + str(baby_dict[name][i]))
  else:
  	print(name + " does not appear in any decade.")

def query_3(decade_input):
  index = decade.index(decade_input)
  print('The names are in order of rank:')
  rank_dict = {}
  for name in baby_dict:
    if(baby_dict[name][index] != 1001):
      rank = baby_dict[name][index]
      if rank in rank_dict:
        rank_dict[rank].append(name)
        rank_dict[rank].sort()
      else:
        new_entry = []
        new_entry.append(name)
        rank_dict[rank] = new_entry
  
  # print according to rank
  rank_ordered = list(rank_dict.keys())
  rank_ordered.sort()
  for rank_o in rank_ordered:
    for i in range(len(rank_dict[rank_o])):
      print(rank_dict[rank_o][i] + ': ' + str(rank_o))

def query_4():
	# empty list to store names
  all_decade = []

  # Find all names that appear in all decades and sort
  for i in baby_dict:
    if(1001 not in baby_dict[i]):
      all_decade.append(i)
  all_decade.sort()

  # Print the names
  print("%i names appear in every decade. The names are:" % (len(all_decade)) )
  for i in all_decade:
    print(i)

def query_5():
  # display all namese that became incrasingly popular for every decade
  names = []
  for i in baby_dict:
    increasing = True and (1001 not in baby_dict[i])
    if(increasing == False):
      continue
    for j in range(len(baby_dict[i]) - 1):
      increasing = increasing and ( baby_dict[i][j] > baby_dict[i][j+1] )
    if(increasing == True):
      names.append(i)

  # Print the ouput
  print('%i names are more popular in every decade.' % len(names))
  for i in names:
    print(i)

def query_6():
  # display all namese that became incrasingly popular for every decade
  names = []
  for i in baby_dict:
    increasing = True and (1001 not in baby_dict[i])
    if(increasing == False):
      continue
    for j in range(len(baby_dict[i]) - 1):
      increasing = increasing and ( baby_dict[i][j] < baby_dict[i][j+1] )
    if(increasing == True):
      names.append(i)

  # Print the ouput
  print('%i names are less popular in every decade.' % len(names))
  for i in names:
    print(i)
  
# Interact with the user
def user_interact():
  # store value for user input
  user_input = 1
  while(user_input > 0 and user_input < 7):
  	# Print the menu choices
    queries()
    
    # Prompt user for input
    user_input = int(input('Enter choice: '))
    
    # Run through the queries
    if(user_input == 1):
      name = input('Enter a name: ')
      print()
      query_1(name)

    elif(user_input == 2):
      name = input('Enter a name: ')
      print()
      query_2(name)

    elif(user_input == 3):
      decade_input = int(input('Enter decade: '))
      while(decade_input not in decade):
        decade_input = int(input('Enter decade: '))
      query_3(decade_input)

    elif(user_input == 4):
      query_4()

    elif(user_input == 5):
      query_5()

    elif(user_input == 6):
    	query_6()

  print()
  print()
  print()
  print('Goodbye.')
  
def main():
  # Fill the baby dictionary
  create_baby_dict()

  # Start the application
  user_interact()

main()

