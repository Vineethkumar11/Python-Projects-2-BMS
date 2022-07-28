#Project on the bank management system-


print("~"*30)

customerNames =['ashok','visha',"balu"]
customerpins =['2078','4050','5489']
customerBalances=[10000,45000,65000]
depostion=0
withdrawl=0
balance=0
counter_1= 1
counter_2= 5
i=0

while True:
    print('*'*30)
    print('>>>>>>Welcome to VR bank<<<<<<')
    print('^'*30)
    print(">>1.Open account")
    print(">>2.Withdrawl")
    print(">>3.Deposit money")
    print(">>4.Check Customers & Balance")
    print(">>5.Exit/Quit")
    print('='*30)
    
    choicenumber= input("Select your choice number form the above option : ")
    if choicenumber =="1":
        print("choice number 1 is selected by the customer ")

        NOC=eval(input('number of customers :'))

        i=i+NOC

        if i > 5:
            
            print("\n")
            print("Customer registration exceed reached or customer reached or customer registration too low")
            i=i-NOC
        else:

            while counter_1<=i:
                name=input('Input fullname :')
                customerNames.append(name)
                pin=str(input("Please input a pin of choice :"))
                customerpins.append(pin)
                balance=0
                depostion=eval(input("please input a value to deposit to statement :"))
                balance=balance+depostion
                customerBalances.append(balance)
                print("\nName=",end=" ")
                print(customerNames[counter_1])
                print("pin=", end=" ")
                print(customerpins[counter_1])
                print("balance=",end=" ")
                print(customerBalances[counter_1],end=" ")
                print("-/Rs")
                counter_1=counter_1 + 1
                counter_2=counter_2 + 1
                print("\n Your name is successfully added to customer sysytem")
                print("Your pin is successfully added to customer system")
                print("Your balance is added to customer system")
                print('>>Congrats! Your account is created successfully<<')
                print('\n')
                print("Your name is avaliable on the customerl list now : ")
                print(customerNames)
                print('\n')
                print("Note!Dear customer>> Please remember the name and pin<<")
                print("~"*30)
                
            mainmenu=input("Please press any key to go back")
    elif choicenumber=="2":
        j=0
        print("Choice number 2 is selected  by the customer")

        while j<1:
            k = -1
            name =input("please input name : ")
            pin =input("please input pin : ")


            while k<len(customerNames) - 1:
                k=k+1
                if name==customerNames[k]:
                    if pin==customerpins[k]:
                        j=j+1
                        print('Your current balance:',end=" ")
                        print(customerBalances[k],end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])

                        withdrawl=eval(input('input value to withdraw : '))

                        if withdrawl > balance:

                            depostion = eval(input("Please deposit a higher value because your balance mentioned is not enough "))
                            
                            balance = balance + depostion
                            print("Your current balance:", end=" ")
                            print(balance,end=" ")
                            print("-/Rs\n")
                            balance=balance-withdrawl
                            print('-\n')
                            print(">>Your withdrawl is sucessfull!")
                            customerBalances[k]=balance
                            print("Your remaining balance is : ",balance,end=" ")
                            print('-/Rs\n\n')
                        else:

                            balance=balance-withdrawl
                            print('\n')
                            print(">>Your withdrawl is sucessfull!")
                            customerBalances[k]=balance
                            print("Your remaining balance is : ",balance,end=" ")
                            print('-/Rs\n\n')
            if j< 1:

                print("Your name and pin doesnt match!\n")
                break
        mainmenu=input("Please press enter key to go mainmenu")
    elif choicenumber =="3":
        print("Choice number 3 is selected by the customer ")
        n=0

        while n<1:
            k= -1
            name = input("please input name : ")
            pin = input("please input pin : ")

            while k < len(customerNames) -1:
                k=k+1

                if name==customerNames[k]:
                    if pin==customerpins[k]:
                        n=n+1

                        print("Your current balance is : ",end= " ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance=(customerBalances[k])

                        depostion=eval(input("Enter the value you want to deposit :"))
                        balance =balance + depostion
                        customerBalances[k]=balance
                        print("\n")
                        print(">>Deposition your money is successfull!")
                        print("Your balance is : ",balance,end=" ")
                        print("-/Rs\n\n")
            if n<1:
                print("Your name and pin doesnt match!\n")
                break

        mainmenu =input("please press enter key to go back to mainmenu")
    elif choicenumber =="4":
        print("Choice number 4 is selected by the customer")
        k=0
        print("Customer name list and balances are mentiond below : ")
        print("\n")

        while k<=len(customerNames) -1:
            print(">>Customer = ",customerNames[k])
            print(">>Balance = ",customerBalances[k],end=" ")
            print("-\Rs")
            print("\n")
            k=k+1

        mainmenu = input("please press enter key to go back to mainmenu")
    elif choicenumber== "5":

        print("Choice number 5 is selected by the customer")
        print("Thankyou for using our VR bank!")
        print("~"*30)
        print("Visit again! Have a nice day")
        break
    else:
        print("Invalid option is selected ")
        print("Please try again")

        mainmenu=input("please press enter key to go back to the main menu ")














            


