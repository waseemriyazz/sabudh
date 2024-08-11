
# PROBLEM 6

# Write a program to Reverse below given numbers without slicing

 

# Test Case 1:

# Input: 745633

# Output: 336547

 

# Test Case 2:

# Input: 65346

# Output: 64356


def reverse_number(n):
    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10
    return reversed_number


input1 = int(input())
output1 = reverse_number(input1)
print(output1)  

