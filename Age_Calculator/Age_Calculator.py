#Calculates the age of a person based on the current year and their birth year.
current_year = int(input("Please enter the current year: "))
birth_year = int(input("Please enter your birth year: "))
age = current_year - birth_year
print(f"You are {age} years old.")