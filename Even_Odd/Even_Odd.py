#Even/Odd: Determines if a number is even or odd.
n = int(input("Enter a number: "))
# modulo "%" operator is used to check if the number is divisible by 2
if n % 2 == 0:
    print(f"{n} is even.")
else:
    print(f"{n} is odd.")