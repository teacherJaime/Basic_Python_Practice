#Greater than: Determines which number is greater.
num1 = int(input("Insert the first number: "))
num2 = int(input("Insert the second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal.")