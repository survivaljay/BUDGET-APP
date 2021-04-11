budgetDict = [{
    "category": "food", 
    "amount": 0,   
},{
    "category": "cloths", 
    "amount": 0,
},{
    "category": "entertainment", 
    "amount": 0,
}]

class BUDGETAPP:
    
    def __init__(self):
        pass
    
    def deposit(self):
        print('\n******* WELCOME TO SURVIVAL BUDGET APP *******\n')
        print("THESE ARE THE BUDGET OPTION AVAILABLE : \n")
        print(" 1. FOOD")
        print(" 2. CLOTH")
        print(" 3. ENTERTAINMENT")
        print(" 4. EXIT\n")

        SelectedBudget = int(input("SELECT YOUR BUDGET : \n"))
        
        if (SelectedBudget == 1):
            print("FOOD BALANCE: #",budgetDict[0]["amount"])
            
            dq = int(input("Do you want to Deposit to Food Balance ?\n 1. YES\n 2. NO \n"))
            
            if (dq == 1):
                deposit = int(input("Enter Amount : \n#"))
                
                deposit1 = budgetDict[0]["amount"] + deposit
                
                budgetDict[0]["amount"] = budgetDict[0]["amount"] + deposit
                
                print("NEW BALANCE: #",budgetDict[0]["amount"])
                
                wq = int(input("What do you want to do ?\n 1. TRANSFER\n 2. WITHDRAW\n 3. QUIT\n"))
                
                if (wq == 1):
                    self.transfer()
                    
                elif (wq == 2):
                    self.withdrawfromBudget()
                
                elif (wq == 3):
                    exit()
                else:
                    print("HAVE A NICE DAY !!!")
                    
            else:
                print("Invalid Selection\nPLEASE, SELECT A VALID OPTION")
                self.deposit()
                
                
                
                                
        elif (SelectedBudget == 2):
            print("CLOTH BALANCE: #",budgetDict[1]["amount"])
            
            dq = int(input("Do you want to Deposit to Cloth Balance ?\n 1. YES\n 2. NO \n"))
            
            if (dq == 1):
                deposit = int(input("Enter Amount : \n#"))
                
                deposit1 = budgetDict[1]["amount"] + deposit
                
                budgetDict[1]["amount"] = budgetDict[1]["amount"] + deposit
                
                print("NEW BALANCE: #",budgetDict[1]["amount"])
                
                wq = int(input("What do you want to do ?\n 1. TRANSFER\n 2. WITHDRAW\n 3. QUIT\n"))
                
                if (wq == 1):
                    self.transfer()
                    
                elif (wq == 2):
                    self.withdrawfromBudget()
                
                elif (wq == 3):
                    exit()
                
                else:
                    print("HAVE A NICE DAY !!!")
                    

            else:
                print("Invalid Selection\nSELECT A VALID OPTION : \n")
                self.deposit()
                
                
                
        elif (SelectedBudget == 3):
            print("ENTERTAINMENT BALANCE: #",budgetDict[2]["amount"])
            
            dq = int(input("Do you want to Deposit to ENTERTAINMENT Balance ?\n 1. YES\n 2. NO\n"))
            
            if (dq == 1):
                deposit = int(input("Enter Amount : \n#"))
                
                deposit1 = budgetDict[2]["amount"] + deposit
                
                budgetDict[2]["amount"] = budgetDict[1]["amount"] + deposit
                
                print("NEW BALANCE: #",budgetDict[2]["amount"])
                
                wq = int(input("What do you want to do : \n 1. TRANSFER\n 2. WITHDRAW\n 3. QUIT\n"))
                
                if (wq == 1):
                    self.transfer()
                    
                elif (wq == 2):
                    self.withdrawfromBudget()
                
                elif (wq == 3):
                    exit()
                
                else:
                    print("HAVE A NICE DAY !!!")
                    

            else:
                print("Invalid Selection \nSELECT A VALID OPTION : \n")
                self.deposit()
                    
        elif (SelectedBudget == 4):
            print("HAVE A NICE DAY !!!!")
            exit()
                    

        else:
            print("HAVE A NICE DAY !!!")
                
                    
    def withdrawfromBudget(self):
        print(budgetDict)
        print("WITHDRAWAL OPTIONS : ")
        print(" 1. FOOD ")
        print(" 2. CLOTH ")
        print(" 3. ENTERTAINMENT ")
        print(" 4. EXIT \n")
        
        selectedbudgetOption = int(input("SELECT WITHDRWAL OPTION : \n"))
        
        if (selectedbudgetOption == 1):
            print("FOOD BALANCE: #",budgetDict[0]["amount"])
            
            withdraw = int(input("Enter Amount You Want To Withdraw : \n#"))
            
            if (withdraw > budgetDict[0]["amount"]):
                print("INSUFFICIENT FUNDS ")
                
                wq = int(input("Would you like to return home ?\n 1. YES\n 2. NO\n"))
                
                if (wq == 1):
                    self.deposit()
                else:
                    print("HAVE A NICE DAY !!!")
                    exit()
            
            else:
                withdraw1 = budgetDict[0]["amount"] - withdraw
                
                budgetDict[0]["amount"] = budgetDict[0]["amount"] - withdraw
                
                print("WITHDRAWAL SUCCESSFUL")
                
                print("FOOD NEW BALANCE: #",budgetDict[0]["amount"])
                
                wq = int(input("Would you like to return Home ?\n 1. YES\n 2. NO"))
                
                if (wq == 1):
                    self.deposit()
                
                else:
                    print("HAVE A NICE DAY !!!")
                    exit()
                
        elif (selectedbudgetOption == 2):
            print("CLOTH BALANCE: #",budgetDict[1]["amount"])
            
            withdraw = int(input("Enter Amount You Want To Withdraw : \n#"))
            
            if (withdraw > budgetDict[1]["amount"]):
                print("INSUFFICIENT FUNDS \n")
                
                wq = int(input("Would you like to Return Home ?\n 1. YES\n 2. NO"))
                
                if (wq == 1):
                    self.deposit()
                
                else:
                    print("HAVE A NICE DAY !!!")
                    exit()
            
            else:
                withdraw1 = budgetDict[1]["amount"] - withdraw
                
                budgetDict[1]["amount"] = budgetDict[1]["amount"] - withdraw
                
                print("WITHDRAWAL SUCCESSFUL ")
                
                print("CLOTH NEW BALANCE: #",budgetDict[1]["amount"])
                
                wq = int(input("Would you like to return home ?\n 1. YES\n 2. NO"))
                
                if (wq == 1):
                    self.deposit()
                
                else:
                    print("HAVE A NICE DAY !!!")
                    exit()
                
        elif (selectedbudgetOption == 3):
            print("ENTERTAINMENT BALANCE: #",budgetDict[2]["amount"])
            
            withdraw = int(input("Enter Amount You Want To Withdraw : \n#"))
            
            if withdraw > budgetDict[2]["amount"]:
                print("INSUFFICIENT FUNDS \n")
                
                wq = int(input("Would you like to Return Home ?\n 1. YES\n 2. NO\n"))
                
                if (wq == 1):
                    self.deposit()
                
                else:
                    print("HAVE A NICE DAY !!!")
                    exit()
            
            else:
                withdraw1 = budgetDict[2]["amount"] - withdraw
                
                budgetDict[2]["amount"] = budgetDict[2]["amount"] - withdraw
                
                print("WITHDRAWAL SUCCESFUL")
                
                print("ENTERTAINMENT NEW BALANCE: #",budgetDict[2]["amount"])
                
                wq = int(input("Would you like to Return Home ?\n 1. YES\n 2. NO"))
                
                if (wq == 1):
                    self.deposit()
                
                else:
                    print("HAVE A NICE DAY !!!")
                    exit()
                    
        elif (selectedbudgetOption == 4):
            print("HAVE A NICE DAY !!!")
            exit()
            
        else:
            print("Invalid Selection\nSELECT A VALID OPTION : \n")
            self.deposit()
            
            
            
    def transfer(self):
        
        print(budgetDict)
        print("TRANSFER OPTIONS : ")
        print(" 1. From  FOOD ")
        print(" 2. From CLOTH ")
        print(" 3. From ENTERTAINMENT ")
        print(" 4. EXIT ")
        selectTFoption = int(input("SELECT DESTINATION : \n"))
        
        if selectTFoption == 1:
            print("FOOD BALANCE: #",budgetDict[0]["amount"])
            
            tf = int(input(" 1. TRANSFER TO CLOTH \n 2. TRANSFER TO ENTERTAINMENT\n"))
            
            if (tf == 1):
                tfamount = int(input("Enter Amount : \n#"))
                
                if (tfamount <= budgetDict[0]["amount"]):
                    tfamount1 = budgetDict[0]["amount"] - tfamount
                    
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] - tfamount
                    
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] + tfamount
                    
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    
                    print("TRANSFER SUCESSFUL !!!")
                    print("NEW FOOD BALANCE: #",budgetDict[0]["amount"])
                    print("NEW CLOTH BALANCE: #",budgetDict[1]["amount"])
                    
                    aq = int(input("Do you want to TRANSFER again ?\n 1. YES\n 2. NO\n"))
                    
                    if (aq == 1):
                        self.transfer()
                    
                    else:
                        print("HAVE A NICE DAY !!!")
                        exit()
                
                else:
                    print("INSUFFICIENT FUNDS \n")
                    print("FOOD BALANCE: #",budgetDict[0]["amount"])
                    self.deposit()
                    
            elif (tf ==2):
                tfamount = int(input("Enter Amount : \n#"))
                
                if (tfamount <= budgetDict[0]["amount"]):
                    tfamount1 = budgetDict[0]["amount"] - tfamount
                    
                    tfamount2 = budgetDict[2]["amount"] + tfamount
                    
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] - tfamount
                    
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] + tfamount
                    
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    
                    print("TRANSFER SUCESSFUL !!!")
                    print("NEW FOOD BALANCE: #",budgetDict[0]["amount"])
                    print("NEW ENTERTAINMENT BALANCE: #",budgetDict[2]["amount"])
                    
                    aq = int(input("Do you want to TRANSFER again ?\n 1. YES \n 2. NO\n"))
                    
                    if (aq == 1):
                        self.transfer()
                    
                    else:
                        print("HAVE A NICE DAY !!!")
                        exit()
                    
                else:
                    print("INSUFFICIENT FUNDS \n")
                    print("FOOD BALANCE: #",budgetDict[0]["amount"])
                    self.deposit()
                    
        elif (selectTFoption ==2):
            print("CLOTH BALANCE: #",budgetDict[1]["amount"])
            
            tf = int(input(" 1. TRANSFER TO ENTERTAINMENT\n 2. TRANSFER TO FOOD\n"))
            
            if (tf == 1):
                tfamount = int(input("Enter Amount : \n#"))
                
                if tfamount <= budgetDict[1]["amount"]:
                    tfamount1 = budgetDict[1]["amount"] - tfamount
                    
                    tfamount2 = budgetDict[2]["amount"] + tfamount
                    
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] - tfamount
                    
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] + tfamount
                    
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    
                    print("TRANSFER SUCCESSFUL !!!")
                    print("NEW CLOTH BALANCE: #",budgetDict[1]["amount"])
                    print("NEW ENTERTAINMENT BALANCE: #",budgetDict[2]["amount"])
                    
                    aq = int(input("Do you want to TRANSFER again ?\n 1. YES\n 2 . NO\n"))
                    
                    if (aq == 1):
                        self.transfer()
                        
                    else:
                        print("HAVE A NICE DAY !!!")
                        exit()
                
                else:
                    print("INSUFICIENT FUNDS \n")
                    print("FOOD BALANCE: #",budgetDict[0]["amount"])
                    self.deposit()
                    
            elif (tf ==2):
                tfamount = int(input("Enter Amount : \n#"))
                
                if tfamount <= budgetDict[1]["amount"]:
                    tfamount1 = budgetDict[1]["amount"] - tfamount
                    
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] - tfamount
                    
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] + tfamount
                    
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    
                    print("TRANSFER SUCESSFUL !!!")
                    print("NEW CLOTH BALANCE: #",budgetDict[1]["amount"])
                    print("NEW FOOD BALANCE: #",budgetDict[0]["amount"])
                    
                    aq = int(input("Do you want to TRANSFER again ?\n 1. YES\n 2. NO\n"))
                    
                    if (aq == 1):
                        self.transfer()
                    
                    else:
                        print("HAVE A NICE DAY !!!")
                        exit()
                    
                else:
                    print("INSUFFICIENT FUNDS \n")
                    print("CLOTH BALANCE: #",budgetDict[1]["amount"])
                    self.deposit()
                    
        elif (selectTFoption ==3):
            print("ENTERTAINMENT BALANCE: #",budgetDict[2]["amount"])
            
            tf = int(input(" 1. TRANSFER TO CLOTH\n 2. TRANSFER TO FOOD\n"))
            
            if (tf == 1):
                tfamount = int(input("Enter Amount : \n#"))
                
                if tfamount <= budgetDict[2]["amount"]:
                    tfamount1 = budgetDict[2]["amount"] - tfamount
                    
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] - tfamount
                    
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] + tfamount
                    
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    
                    print("TRANSFER SUCESSFUL !!!")
                    print("NEW ENTERTAINMENT BALANCE: #",budgetDict[2]["amount"])
                    print("NEW CLOTH BALANCE: #",budgetDict[1]["amount"])
                    
                    aq = int(input("Do you want to TRANSFER again ?\n 1. YES\n 2. NO\n"))
                    
                    if (aq == 1):
                        self.transfer()
                    
                    else:
                        print("HAVE A NICE DAY !!!")
                        exit()
                    
                else:
                    print("INSUFFICIENT FUNDS \n")
                    print("FOOD BALANCE: #",budgetDict[0]["amount"])
                    self.deposit()
                    
            elif (tf ==2):
                tfamount = int(input("Enter Amount : \n#"))
                
                if (tfamount <= budgetDict[2]["amount"]):
                    tfamount1 = budgetDict[2]["amount"] - tfamount
                    
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] - tfamount
                    
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] + tfamount
                    
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    
                    print("TRANSFER SUCESSFUL !!!")
                    print("NEW ENTERTAINMENT BALANCE: #",budgetDict[2]["amount"])
                    print("NEW FOOD BALANCE: #",budgetDict[0]["amount"])
                    
                    aq = int(input("Do you want to TRANSFER again ?\n 1. YES\n 2. NO\n"))
                    
                    if (aq == 1):
                        self.transfer()
                    
                    else:
                        print("HAVE A NICE DAY !!!")
                        exit()
                    
                else:
                    print("INSUFFICIENT FUNDS \n")
                    print("CLOTH BALANCE: #",budgetDict[1]["amount"])
                    self.deposit()
                    
        elif (selectTFoption ==4):
            print("HAVE A NICE DAY !!!")
            exit()
            
        else:
            print("HAVE A NICE DAY !!!")
          
    
transaction = BUDGETAPP()       
transaction.deposit()