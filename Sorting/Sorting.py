#SORTING IN PYTHON
#V contains the list of numbers to be sorted
v = [5, 2, 7, 1, 8, 3, 6, 4]
#i is the index variable used to transit the list
i = 0
#while loop is used to iterate through the list until the end of the list is reached
#len function is used to get the length of the list
while i < len(v):
#if statement is used to check if the current element is greater than or equal to the previous element
    if i == 0 or v[i] >= v[i - 1]:
        i += 1
    else:
#if the current element is less than the previous element, swap the two elements and decrement the index variable
        v[i], v[i - 1] = v[i - 1], v[i]
        i -= 1
#print the sorted list
print(v)