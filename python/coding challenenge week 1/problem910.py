
# PROBLEM 10

# Define a function which counts vowels and consonants in a word.

#     Test case 1

# Input : pythonlobby

 

# Output :  

# vowel : 2 

# Consonants: 9

 

# Test case:2

# Input : sabudhfoundation


# Output : 

# vowel : 7

# Constants: 9 

inputString = input("ENter a string : ")

vowel = 0
cons = 0
vows = "aeiou"
for char in inputString:
    if char in vows:
        vowel += 1
        continue
    cons +=1
print(vowel)
print(cons)
    
    