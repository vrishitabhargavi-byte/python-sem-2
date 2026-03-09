an=input("enter name:")
age=int(input("enter age:"))
m=int(input("enter monthly income:"))
c=int(input("enter credit score:"))
if age<=60 and age>=21:
  if m>=25000:
    if c>=700:
      print("Loan approved")
    elif c>=650 and c<=699:
      print("Loan approved with conditions")
    else:
      print("Loan Rejected")
else:
  print("Sorry your age is not eligible")