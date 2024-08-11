
# PROBLEM 3

# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
 

# Test Case 1:

# Input : 12, 75, 150, 180, 145, 525, 50

# Output : [75, 150, 145]

 

# Test Case 2:

# Input : 14, 85, 625, 75

# Output : [85]

inputstring = input("Enter numbers seperated by space: ")

number_strings = inputstring.split(" ")

numbers = [int(num)for num in number_strings]

result= []

for number in numbers :
    if number >500:
        break
    if number > 150:
        continue
    if number%5==0:
        result.append(number)
        
print(result)

 