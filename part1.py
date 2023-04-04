#taking input
m=int(input("Enter the month in the numeric form:"))
d=int(input("Enter the day in numeric form:"))
y=int(input("Enter the year as two numerical digits: "))

f=1

if (m>=1 and m<=12):
  f=1
  
else:
  f=0
  print("Month:Error: Invalid Month Input")
if (d>=1 and d<=31):
  f=1
else:
  f=0
  print("Day: Error: Invalid Day Input")
if (y>0 and y<99):
  f=1

else:
  f=0
  print("Year: Error: Invalid Year Input")
#showing output
if(f==0):
  print("error")
  
else:
  print("The date is "m,"/", d,"/",y)
  print("Success: Congratulations! you entered the correct date")



