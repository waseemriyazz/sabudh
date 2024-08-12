"""
Task 1.  LISTS

Write a Python program to multiply all the items in a list.
Write a Python program to get the largest number from a list.
Write a Python program to get the smallest number from a list.
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Write a Python program to remove duplicates from a list.
Write a Python program to check if a list is empty or not.
Write a Python program to count the lowercase letters in a given list of word
Write a Python program to extract specified number of elements from a given list, which follows each other continuously.
○ Original list:  [1, 1, 3, 4, 4, 5, 6, 7]

○ Extract 2 number of elements from the said list which follows each other continuously: [1, 4]

○ Original list: [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]

○ Extract 4 number of elements from the said list which follows each other continuously: [4]

9.  Write a Python program to find the largest odd number in a given list of integers.

○ Sample Data:  ([0, 9, 2, 4, 5, 6]) -> 9

                           ([-4, 0, 6, 1, 0, 2]) -> 1

                          ([1, 2, 3]) -> 3

                           ([-4, 0, 5, 1, 0, 1]) -> 5

10. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

○ Sample List : [A, B, C, D, E, F]

○ Expected Output : [A, B, F]

 """


def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

my_list = [2, 3, 4]
print(multiply_list(my_list))  


def largest_in_list(items):
    return max(items)

my_list = [1, 9, 8, 7]
print(largest_in_list(my_list))  


def smallest_in_list(items):
    return min(items)

my_list = [1, 9, 8, 7]
print(smallest_in_list(my_list))  


def sort_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])

my_list = [(2, 5), (1, 2), (4, 4), (2, 3)]
print(sort_last(my_list)) 

def remove_duplicates(items):
    return list(set(items))

my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_list))  

def is_empty(items):
    return len(items) == 0

my_list = []
print(is_empty(my_list)) 

def count_lowercase(words):
    return sum(c.islower() for word in words for c in word)

my_list = ['Hello', 'world']
print(count_lowercase(my_list))  


def extract_elements(lst, n):
    return [lst[i] for i in range(len(lst) - 1) if lst[i] == lst[i+1] and lst[i:i+n] == [lst[i]]*n]

print(extract_elements([1, 1, 3, 4, 4, 5, 6, 7], 2))  


def largest_odd(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return max(odd_numbers) if odd_numbers else None

print(largest_odd([0, 9, 2, 4, 5, 6]))  


def remove_elements(lst):
    return [item for i, item in enumerate(lst) if i not in [0, 4, 5]]

sample_list = ['A', 'B', 'C', 'D', 'E', 'F']
print(remove_elements(sample_list))  


"""
Task 2. TUPLES

 

 Write a Python program to create a tuple with different data types.
Write a Python program to create a tuple of numbers and print one item.
 Write a Python program to add an item to a tuple.
Write a Python program to get the 4th element from the last element of a Tuple.
Write a Python program to convert a tuple to a dictionary.
Write a Python program to replace the last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

"""

my_tuple = (1, "hello", 3.14, True)
print(my_tuple)  

my_tuple = (1, 2, 3, 4)
print(my_tuple[1])  


my_tuple = (1, 2, 3)
my_tuple += (4,)
print(my_tuple)  


my_tuple = (1, 2, 3, 4, 5, 6, 7)
print(my_tuple[-4])  

my_tuple = (('a', 1), ('b', 2))
my_dict = dict(my_tuple)
print(my_dict)  

def replace_last(tuples, value):
    return [t[:-1] + (value,) for t in tuples]

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(replace_last(sample_list, 100))  


"""
Task 3. DICTIONARY:

1  Write a Python script to sort (ascending and descending) a dictionary by value.

2. Write a Python program to iterate over dictionaries using for loops.

3. Write a Python script to merge two Python dictionaries.

4. Write a Python program to sum all the items in a dictionary.

5. Write a Python program to multiply all the items in a dictionary.

6. Write a Python program to sort a given dictionary by key.

7. Write a Python program to remove duplicates from the dictionary."""



my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
sorted_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print(sorted_asc)  # 


my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict) 


my_dict = {'a': 1, 'b': 2, 'c': 3}
total = sum(my_dict.values())
print(total)  


my_dict = {'a': 1, 'b': 2, 'c': 3}
result = 1
for value in my_dict.values():
    result *= value
print(result)  


my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)  


my_dict = {'a': 1, 'b': 2, 'c': 1}
unique_dict = {v: k for k, v in my_dict.items()}
print(unique_dict)  


"""
Task 4. Numpy

 

1: Numpy array creation and manipulation

 

Create a 1D Numpy array “a” containing 10 random integers between 0 and 99.
Create a 2D Numpy array “b” of shape (3, 4) containing random integers between -10 and 10.
Reshape “b” into a 1D Numpy array “b_flat”.
Create a copy of “a” called “a_copy”, and set the first element of “a_copy” to -1.
Create a 1D Numpy array “c” containing every second element of “a”.
 

2: Numpy array indexing and slicing

 

Print the third element of “a”.
Print the last element of “b”.
Print the first two rows and last two columns of “b”.
Assign the second row of “b” to a variable called “b_row”.
Assign the first column of “b” to a variable called “b_col”.
 

 3: Numpy array operations

 

Create a 1D Numpy array “d” containing the integers from 1 to 10.
Add “a” and “d” element-wise to create a new Numpy array “e”.
Multiply “b” by 2 to create a new Numpy array “b_double”.
Calculate the dot product of “b” and “b_double” to create a new Numpy array “f”.
Calculate the mean of “a”,” b”, and “b_double” to create a new Numpy array “g”.
 

4: Numpy array aggregation

 

Find the sum of every element in “a” and assign it to a variable “a_sum”.
Find the minimum element in “b” and assign it to a variable “b_min”.
Find the maximum element in “b_double” and assign it to a variable “b_double_max”.
"""

import numpy as np
a = np.random.randint(0, 100, 10)
b = np.random.randint(-10, 10, (3, 4))
b_flat = b.flatten()
a_copy = a.copy()
a_copy[0] = -1
c = a[::2]
print(a, b, b_flat, a_copy, c)



print(a[2])
print(b[-1, -1])
print(b[:2, -2:])
b_row = b[1, :]
b_col = b[:, 0]



d = np.arange(1, 11)
e = a + d
b_double = b * 2
f = np.dot(b, b_double.T)
g = np.mean([a, b, b_double])
print(e, b_double, f, g)


a_sum = np.sum(a)
b_min = np.min(b)
b_double_max = np.max(b_double)
print(a_sum, b_min, b_double_max)


"""
Task 5 : Pandas

 

Dataset : https://www.kaggle.com/datasets/rkiattisak/sports-car-prices-dataset


 

Load the dataset into a Pandas DataFrame and display the first 5 rows to get an idea of the data.
Use Pandas to clean the dataset by removing any missing or duplicate values, and converting any non-numeric data to numeric data where appropriate.
Use Pandas to explore the dataset by computing summary statistics for each column, such as mean, median, mode, standard deviation, and range.
Use Pandas to group the dataset by car make and compute the average price for each make.
Use Pandas to group the dataset by year and compute the average horsepower for each year.
Use Pandas to create a scatter plot of price versus horsepower, and add a linear regression line to the plot.
Use Pandas to create a histogram of the 0-60 MPH times in the dataset, with bins of size 0.5 seconds.
Use Pandas to filter the dataset to only include cars with a price greater than $500,000, and then sort the resulting dataset by horsepower in descending order.
Use Pandas to export the cleaned and transformed dataset to a new CSV file.
 """


import pandas as pd

df = pd.read_csv('sports_car_prices.csv')
print(df.head())
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df.dropna(inplace=True)  
print(df.describe())
avg_price_per_make = df.groupby('make')['price'].mean()
print(avg_price_per_make)
avg_hp_per_year = df.groupby('year')['horsepower'].mean()
print(avg_hp_per_year)


import matplotlib.pyplot as plt
import seaborn as sns
sns.regplot(x='horsepower', y='price', data=df)
plt.show()

df['0-60_mph_time'].plot.hist(bins=range(int(df['0-60_mph_time'].min()), int(df['0-60_mph_time'].max()) + 1, 1))
plt.show()

high_value_cars = df[df['price'] > 500000].sort_values(by='horsepower', ascending=False)
print(high_value_cars)


df.to_csv('cleaned_sports_car_prices.csv', index=False)


