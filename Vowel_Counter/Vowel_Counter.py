#Program that counts the number of vowels in a word
word = input("Write a word: ")
vowels = 0
for letter in word.lower():
    if letter in "aeiou":
        vowels += 1
print(f"There are {vowels} vowels in the word '{word}'")