current_balance=100000# assigned a value to global variable

def Banking_Project():# defined fucntion here
    global current_balance #declaring global variable to reuse in multiple function

   
while True:#loop repeats untill we break
    
    try:#except handling 
        print("Welcome to VIJAY'S ATM machine")
        print("Choose the operation to perform:")
        print("1.Balance Enquiry")
        print("2.Withdraw Amount")
        print("3.Deposit Amount")
        choice_input=int(input("choose a operation listed above"))#taking input from user to choose operation for 1,2,3
        
        if choice_input==1:
            #current_balance
            
            print("Current_Balance is: ",current_balance)
            
        elif choice_input==2:# for knowing current amount after withdrawn operation
            
            try:
                withdrawn_amount=int(input("enter amount to be withdrawn from current balance"))
                if withdrawn_amount<0 or withdrawn_amount>current_balance:
                    print("entered amount is not valid, please enter valid amount")
                else:
                    
                    current_balance=current_balance-withdrawn_amount
                    print(f"Current_Balance : {current_balance}after withdrawn amount of {withdrawn_amount}")
                    
            except Exception as e:
                print(e)
        elif  choice_input==3: #for knowing curret amount after deposting amount
            
            
            try:
                Amount_to_deposit=int(input("enter amount to deposit"))
                if Amount_to_deposit<0:
                    print("invalid amount!")
                else:
                    current_balance=current_balance+Amount_to_deposit
                    print(f"Current_Balance : {current_balance}after deposit of {Amount_to_deposit}")
                    
            except Exception as e:
                print(e)
        else:
            print("enter an invalid operation choice")
    except Exception as e:
        print(e)
        #here asking to user whether to exit from operation or to continue for next operation, i used strip and upper method 
    another_transaction=input("enter ABC for another transaction/  DEF to exist").strip().upper()
    if another_transaction!="ABC":
        break
        

Banking_Project()# calling function to run program





print(" iam mmaking changges here")