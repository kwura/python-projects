def main():

  itemsPerLine = 0
  
  for i in range(100, 201):
    if ((i % 5 == 0) or (i % 6 == 0)) and not ((i % 5 == 0) and (i % 6 == 0)):
      print(i, end = ' ')
      itemsPerLine += 1
      if itemsPerLine >= 10:
        print()
        itemsPerLine = 0
		
main()