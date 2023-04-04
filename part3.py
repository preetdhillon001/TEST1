sal=(float(input("enter salary")))
cntry=input("enter country")
def consalary():
 if(cntry=="Canada"):
    finalsalary=sal*1.55
    if(finalsalary>64000 and cntry=="Canada"):
     print("you have enough money",finalsalary,"CAD" )
    else:
     print("you don't have enough money",finalsalary,"CAD" )
      
 elif(cntry=="US"):
    finalsalary=sal*2.5
    if(finalsalary>56516 and cntry=="us"):
     print("you have enough money",finalsalary,"US Dollars" )
    else:
     print("you don't have enough money",finalsalary,"US Dollars")

 elif(cntry=="Cabodia"):
    finalsalary=sal*4555
    if(finalsalary>5649856 and cntry=="cabodia"):
     print("you have enough money",finalsalary,"Cambodian Riel" )
    else:
     print("you don't have enough money",finalsalary,"Cambodian Riel" )
    
 elif(cntry=="United Kingdom"):
    finalsalary=sal*1.2
    if(finalsalary>35423 and cntry=="united kingdom"):
     print("you have enough money",finalsalary,"Pound Sterling" )
    else:
     print("you don't have enough money",finalsalary,"Pound Sterling" )
 else:
    print("invalid")

consalary()

 