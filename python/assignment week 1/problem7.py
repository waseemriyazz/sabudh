
# PROBLEM  7

# Write a program to Use a loop to display elements from a given list present at odd index position

 

# Test Case 1:

# Input: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

# Output: [20, 40, 60, 80, 100]

 

# Test Case 2:

# Input: 23, 46, 69, 92, 115

# Output: [46, 92] 

inputstring = input("Enter numbers seperated by space: ")

number_strings = inputstring.split(" ")

numbers = [int(num)for num in number_strings]

result=[]

for i in range (len(numbers)):
    if i % 2==0:
        continue
    result.append(i)
