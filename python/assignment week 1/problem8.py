
# PROBLEM 8

# Write a Python program to find the median of three values.

# Test case 1

#  Input: 

# Input first number: 15

# Input second number: 26

# Input third number: 29

 

# Output : 26

 

# Test case 2

#  Input: 

# Input first number: 10

# Input second number: 20

# Input third number: 5

 

# Output : 10

input1 = int(input())
input2 = int(input())
input3 = int(input())

llist = [ input1, input2, input3]
llist.sort()
print(llist[1])