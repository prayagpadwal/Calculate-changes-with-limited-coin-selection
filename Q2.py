dollar = float(input("Please input a dollar amount between 0.21 and 0.99 : " ))

while(dollar >0.99 or dollar < 0.21):
    print("The input must be between 0.21 and 0.99")
    dollar = float(input("Please input a dollar amount between 0.21 and 0.99 : " ))
dollar = dollar *100
quarter = 25
dimes = 10
nickels = 5
pennies = 1
ans = 0

result=[0] *4
if dollar > 25:
        ans = quarter
        result[0]+=1

else:
    ans= 0

while(ans < dollar):
    if (dollar-ans) >= dimes:
        ans+=dimes
       
        result[1]+=1
        
    elif (dollar-ans) >= nickels and (dollar-ans) < dimes:
       ans+=nickels
       result[2]+=1
       
    elif (dollar-ans) < nickels and (dollar-ans) < dimes and (dollar-ans) >= pennies:
        ans+=pennies
        result[3]+=1
        
print("Your change is:",result[0],"quarter, ",result[1],"dimes, ",result[2],"nickels, and ",result[3],"Pennies.")



    
            