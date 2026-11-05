# This program performs basic arithmetic operations on two numbers provided by the user.
print("=========BASIC CALCULATOR=========")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
#define a function to check if the user wants to perform another operation
def again():
    response = input("Do you want to perform another operation? (yes/no): ").strip().lower()
    return response
while True:
    # Display the menu of operations
    option = input("Select an option:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Power\n6. Exit\n")
    # Check if both numbers are zero and exit the program if they are
    if first_number == 0 and second_number == 0:
        print("Both numbers are zero. Exiting program.")
        exit()
    # Perform the selected operation
    if option == "1":
        print(f"The sum of {first_number} and {second_number} is: {first_number + second_number}")
    elif option == "2":
            print(f"The difference of {first_number} and {second_number} is: {first_number - second_number}")
    elif option == "3":
            print(f"The product of {first_number} and {second_number} is: {first_number * second_number}")
    elif option == "4":
        if second_number != 0:
                print(f"The quotient of {first_number} and {second_number} is: {first_number / second_number}")
        else:
                print("Error: Division by zero is undefined.")
    elif option == "5":
            print(f"{first_number} raised to the power of {second_number} is: {first_number ** second_number}")
    elif option == "6":
            print("Exiting program.")
            break
    else:
            print("Invalid option. Please try again.")
            continue
    # Ask the user if they want to perform another operation
    response = again()
    if response != "yes":
        print("Exiting program.")
        break