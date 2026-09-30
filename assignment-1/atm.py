Balance = 1000
correctpin = "6767"
print("Welcome To The ATM System")
correctpin = False
while correctpin == False:
    enteredpin = int(input("Please enter your 4-Digit code : "))
    if enteredpin == correctpin :
        print("\nPIN accepted!")
    correctpin = True
else:
        print("Wrong PIN. Please try again.\n")
running = True
while running == True:
    print("\n===ATM MENU===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. EXIT")

    choice = int(input("choose an option (1-4) : "))
    if choice == 1:
        print("your balance is : ", Balance)

    elif choice == 2:
        amount = int(input("how much amount to deposit : "))
        Balance = Balance + amount
        print("Amount deposited successfully")
        print("Current Balance: $", Balance)
    elif choice == 3:
        amount = int(input("How much amount to withdraw : "))
        if amount > Balance:
            print("You do not have enough Balance!")
        else:
            Balance = Balance - amount
            print("Amount withdrew successfully")
            print("Current Balance: $", Balance)
    elif choice == 4:
        print("Thank you for using the ATM")
        running = False
    else:
        print("Invalid choice. try again.\n")
