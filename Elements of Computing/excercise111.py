def main ():
  
  start = 312032486
  
  days = 365
  
  seconds = 31536000
  
  birth = seconds // 7
  
  death = seconds // 13
  
  immigrant = seconds // 45
  
  cycle = birth - death + immigrant
  
  year_1 = start + cycle  
  
  year_2 = start + 2*seconds//7 + 2 * seconds // 45 - 2 * seconds // 13
  
  year_3 = start + 3*seconds//7 + 3 * seconds // 45 - 3 * seconds // 13
  
  year_4 = start + 4*seconds//7 + 4 * seconds // 45 - 4 * seconds // 13
  
  year_5 = start + 5*seconds//7 + 5 * seconds // 45 - 5 * seconds // 13
  
  print(year_1, year_2, year_3, year_4, year_5)

  
main()
