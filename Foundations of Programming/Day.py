#  Description: Prints the day of the week for a specific date


def main ():
# prompt user for year
  year = int(input( "Enter year:"))
  
  while(year < 1900 or year > 2100):
    year = int(input("Enter year:"))
  
# prompt user for month
  month = int(input("Enter month:"))
  
  while(month < 1 or month > 12):
    month = int(input("Enter month:"))
  
# prompt user for day
  day = int(input("Enter day:"))
  
  if(month== 1 or month == 3 or month == 5 or month == 7 or month ==8 or month == 10 or month == 12):
    while(day >31 or day < 1):
      day = int(input("Enter day:"))
  
  if(month== 4 or month == 6 or month == 9 or month == 11):
    while(day>30 or day <1):
      day = int(input("Enter day:"))
  
  if( year % 400 == 0 or year % 100 != 0 and year % 4 == 0):
    while(month == 2 and day > 29 or day <1):
      day = int(input("Enter day:"))
  else:
    while(month == 2 and day > 28 or day <1):
      day = int(input("Enter day:"))
  
# variable a when year begins in March
  if( month == 2):
    a = 12
  else:
    a = (month + 10)%12
	
# variable b for day of the month
  b = day 
    
# variable c to make adjustment for year of the century
  if (month>0 and month <3):
    year -= 1 
  if (year % 100 == 0):
    c = 100
  else: 
    c = year % 100
  
# variable d for unconventional century 
  if( year <= 1900):
    d = 18
  if( year >= 1901 and year <=2000):
    d = 19
  if( year >= 2001 and year <=2100):
    d = 20
	
# algorithm developed by Rev. Zeller

  w = (13*a - 1) // 5
  
  x = c // 4
  
  y = d // 4
  
  z = w + x + y + b + c - 2*d  
  
  r = z % 7
  
  r = (r +7) % 7

# r gives the day of the week   
  if (r == 0):
    r = "Sunday"
  if (r == 1):
    r = "Monday"
  if (r == 2):
    r = "Tuesday"
  if (r == 3):
    r = "Wednesday"
  if (r == 4):
    r = "Thursday"
  if (r == 5):
    r = "Friday"
  if (r == 6):
    r = "Saturday"

# print the day of the week
  print()
  print("The day is", r, end = ".")
  
  
  
main ()