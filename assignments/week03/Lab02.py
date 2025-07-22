# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print("Current balance:", balance)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdraw successful")
            else:
                print("Insufficient funds")
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("Deposit successful")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

else:
    print("Invalid PIN")