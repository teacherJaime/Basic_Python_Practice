#ATM: Simulates an automated teller machine
print("Welcome to the ATM")

    # Initial information
balance = int(1000)
daily_limit = int(500)
    
    # Ask for password
password = input("Please enter your password: ")
attempts = 3
access = False
    #Performs security check for password and allows user to access ATM operations if correct password is entered.
while attempts > 0 and not access:
    if password == "1234":  # Replace "1234" with the actual password
            access = True
    else:
        attempts -= 1
        print(f"Invalid password. You have {attempts} attempts left.")
        password = input("Please enter your password: ")

    if not access:
        print("Too many failed attempts. Access denied.")
        raise SystemExit
    
    # ATM Operations
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

while True:
        choice = input("Please select an option (1-4): ")
        if choice == '1':
            print(f"Your current balance is: ${balance}")
        elif choice == '2':
            deposit_amount = float(input("Enter amount to deposit: "))
            balance += deposit_amount
            print(f"${deposit_amount} deposited. New balance: ${balance}")
        elif choice == '3':
            withdraw_amount = float(input("Enter amount to withdraw: "))
            if withdraw_amount > balance:
                print("Insufficient funds.")
            elif withdraw_amount > daily_limit:
                print(f"Withdrawal amount exceeds daily limit of ${daily_limit}.")
            else:
                balance -= withdraw_amount
                print(f"${withdraw_amount} withdrawn. New balance: ${balance}")
        elif choice == '4':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            again = input("Would you like to perform another transaction? (yes/no): ").lower()