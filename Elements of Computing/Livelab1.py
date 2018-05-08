def main ():
  monthly = eval(input("Enter the monthly saving amount:"))
  
  consistent = monthly
  
  iter = 1
  
  while (iter <=6):
    
    if (iter == 1):
      monthly = (monthly + consistent*0) * (1 + 0.00417) 
    
    else:
      monthly = (monthly + consistent) * (1 + 0.00417)
	
    iter = iter + 1
    
  
  print("After the sixth month, the account value is", monthly)	
  
  


main ()