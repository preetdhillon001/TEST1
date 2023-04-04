#varity of colours
RED="red"
BLUE="blue"
YELLOW="yellow"
#taking input
col1=input("choose 1st colour in lower case:")
col2=input("choose 2nd colour in lower case:")


if (col1 !=RED) :
  print( "Error: Invalid Color1" )
if (col2 != BLUE):
    print("Error: Invalid Color2" )

  
if (col1==col2):
  print("Error: The two colors you entered are same")
if (col1=="red"):
  if(col2=="blue"):
    print("RED+BLUE=PURPLE")
  elif(col2=="yellow"):
    print("RED+YELLOW=ORANGE")
if (col1=="blue"):
  if(col2=="red"):
     print("BLUE+RED=PURPLE")
  elif(col2=="yellow"):
    print("BLUE+YELLOW=GREEN")  
if (col1=="yellow"):
  if(col2=="red"):
     print("YELLOW+RED=ORANGE")
  elif(col2=="blue"):
     print("YELLOW+BLUE=GREEN")   
else:
  print("invalid")
