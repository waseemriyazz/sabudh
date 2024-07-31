
# PROBLEM 9

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# Test case 1

# input = 4

# output = 24

 

# Test case 2

# input = 2

# output = 2

 
inputNumber = int(input())
factorial = 1
for i in range (1, inputNumber+1):
    factorial = factorial * i
print(factorial)