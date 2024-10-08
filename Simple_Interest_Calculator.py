# giving inputs value for principle amount, interest rate and time periods in months
principle_amount=int(input("Enter Principle amount in Rupees = "))

rate_of_interest=int(input("Enter interest rate = "))

Time_period =int(input("Enter time period in months = "))

# if user inputs value is in negative or equals to zero , code will tell user to give positive interger or more than zero values

if principle_amount<=0 or rate_of_interest<=0 or Time_period<=0 :
 print("Please input only positive interger inputs values")

else:
# and this is the formula for calculating simple interest
 Simple_Interest_amount=(principle_amount*rate_of_interest*Time_period)/100


#Printing final result for interest rate and simple interset amount
 print("For interest rate = ",rate_of_interest)
 print("Total amount In Rupees = ",Simple_Interest_amount+principle_amount)
