#Palindrome Checker
p = input("word: ").lower()
if p == p[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")