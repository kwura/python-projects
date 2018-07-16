def main():
  investmentAmount = int(input("Enter investment amount:"))
  annual = eval(input("Enter annual interest rate:"))
  years = int(input("Enter number of years:"))
  
  print("Accumlated value is %-.2f" %(investmentAmount *((1 + (annual/1200))**(years*12))))
 





main()