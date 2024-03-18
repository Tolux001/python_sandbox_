# PRACTICE



# Writing conditional statement

# # Accepting input integers from users
# number_supplied = eval(input("Write your number specified: "))

# # Using conditional statement
# if(number_supplied > 1000):
#     print("Number supplied is greater than 1000")
# else:
#     print("Number is within range")



# # Print the max and min numbers in a list using
# #     built in function
# #     user defined function
# numbers = [10, 5, 20, 15, 8]

# Using built-in functions
# max_num = max(numbers)
# min_num = min(numbers)

# print(f"The maximum number is {max_num}")
# print(f"The minimum number is {min_num}")



# def find_max_min(nums):
#     max_val = float("-inf")  # Initialize with negative infinity
#     min_val = float("inf")   # Initialize with positive infinity

#     for num in nums:
#         if num > max_val:
#             max_val = num
#         if num < min_val:
#             min_val = num

#     return max_val, min_val

# # Example usage
# numbers = [10, 5, 20, 15, 8]
# max_num, min_num = find_max_min(numbers)

# print(f"The maximum number is for my defined function {max_num}")
# print(f"The minimum number is for my defined function {min_num}")


# # Suppose you want to know the sum and the product of the digits in an integer
# # enter the integer: 357
# # Result: 357 digit sum is 15 and digit product is 105
# # enter the integer: 123456
# # Result: 123456 digit sum is 21 and the digit product is 720
# # write a python code that obtain the sum of and the product of the digits in a number. the first statement and the last statement of the program given to you.
# # number = input('Enter an integer: ')
# # print('\n', number, "digit sum is", digitSum, " and digit product is", digitProduct)

# # Get the input from the user
# number = input('Enter an integer: ')

# # Initialize variables for digit sum and product
# digitSum = 0
# digitProduct = 1

# # Iterate through each digit in the input number
# for digit in number:
#     # Convert the digit to an integer
#     digit_value = int(digit)
    
#     # Update the digit sum and product
#     digitSum += digit_value
#     digitProduct *= digit_value

# # Print the results
# print('\n', number, "digit sum is", digitSum, "and digit product is", digitProduct)

# use a list to solve the following problem. Read in 20 numbers. As each is read, print it only if it is not a duplicate of a number already read.


# # Initialize an empty list to store unique numbers
# unique_numbers = []

# # Read 20 numbers
# for _ in range(20):
#     try:
#         number = int(input("Enter your number: "))
#         if number not in unique_numbers:
#             unique_numbers.append(number)
#             print(number)
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")

# # Print the unique numbers
# print("Unique values entered: ", '\n', unique_numbers)



# def read_unique_numbers():
#     unique_numbers = []
#     while len(unique_numbers) < 20:
#         try:
#             number = int(input("What number do you desire (in Lucifer's voice): "))
#             if number not in unique_numbers:
#                 unique_numbers.append(number)
#                 print(number)
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")
#     return unique_numbers

# # Call the function
# unique_numbers_list = read_unique_numbers()
# print("Unique values entered: ", '\n \t', unique_numbers_list)

# number = input("what is the number you want to get it digit sum and product: ")
# digit_number_sum = 0
# digit_number_product = 1

# for value in number:
#     digits = int(value)

#     digit_number_sum += digits
#     digit_number_product *= digits
# print(digits, digit_number_sum, digit_number_product)


# n = 5

# for i in range (1,n+1):
#     i = str(i)
#     print (i*10)

# for i in range (n):
#     m = n - i
#     print ('x' * m)


# # exe 12.2
# artsShelf = ["Literature", "English", "Art"]
# scienceShelf = ["Physics", "Mathematics", "Chemistry", "Biology"]

# print(f"Number of books in Arts shelf is {len(artsShelf)}")
# print(f"Number of books in Science shelf is {len(scienceShelf)}")
# print(f"Number of books in Arts and Science shelves is {len(artsShelf) + len(scienceShelf)}")



# def change_char(string_):
#     string_ = string_.lower()
#     # Get the first character of the input string 'string_' and store it in the variable 'char'.
#     char = string_[0]
    
#     # Replace all occurrences of the character 'char' with '+' in the 'string_' string.
#     new_string = string_.replace(char, '+')
    
#     # Reconstruct the 'string_' string by placing the original 'char' as the first character,
#     # followed by the modified string starting from the second character.
#     new_string = char + new_string[1:]
    
#     # Return the modified 'string_' string.
#     return new_string

# # Example usage:
# input_string = "character"
# result = change_char(input_string)
# print("Modified string:", result)






# 1. **Bitwise AND (X & Y)**:
#    - X = 00111100
#    - Y = 00001101
#    - Result = X & Y = 00001100 (in binary) = 12 (in decimal)

# 2. **Bitwise OR (X | Y)**:
#    - X = 00111100
#    - Y = 00001101
#    - Result = X | Y = 00111101 (in binary) = 29 (in decimal)

# 3. **Bitwise XOR (X ^ Y)**:
#    - X = 00111100
#    - Y = 00001101
#    - Result = X ^ Y = 00110001 (in binary) = 49 (in decimal)


# def bitwise_operations(X, Y):
#     # Bitwise AND
#     result_and = X & Y
#     print(f"Bitwise AND: {result_and} ({bin(result_and)})")

#     # Bitwise OR
#     result_or = X | Y
#     print(f"Bitwise OR: {result_or} ({bin(result_or)})")

#     # Bitwise XOR
#     result_xor = X ^ Y
#     print(f"Bitwise XOR: {result_xor} ({bin(result_xor)})")

# # Given values
# X = 0b00111100
# Y = 0b00001101

# # Calculate bitwise operations
# bitwise_operations(X, Y)




# def linear_search(arr, target):
#     for i, num in enumerate(arr):
#         if num == target:
#             print(f"Element {target} found at index {i}.")
#             return
#     print(f"Element {target} not found in the array.")

# my_array = [10, 20, 30, 34, 40, 50, 34]
# element_to_find = 34
# linear_search(my_array, element_to_find)




# def printArray():
#     lists = []
#     num = int(input("Enter the number of items you want to store: "))
#     for i in range(0, num):
#         i = input("Input elements of the array: ")
#         lists.append(i)
#         print()
#     print(lists)
# printArray()




# def calculate_fine(days_late):
#     if days_late <= 0:
#         print("No fine. Thank you for returning the book on time!")
#     elif days_late <= 5:
#         fine = 0.50 * days_late
#         print(f"Fine amount: ₹{fine:.2f}")
#     elif days_late <= 10:
#         fine = 1.00 * days_late
#         print(f"Fine amount: ₹{fine:.2f}")
#     elif days_late <= 30:
#         fine = 5.00 * days_late
#         print(f"Fine amount: ₹{fine:.2f}")
#     else:
#         print("Your membership will be canceled due to excessive delay.")

# # Get input from the user
# try:
#     days_late = int(input("Enter the number of days the book is late: "))
#     calculate_fine(days_late)
# except ValueError:
#     print("Invalid input. Please enter a valid integer for the number of days.")




# # Python program to display all the prime numbers within an interval
# lower = 2
# upper = 10

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#     # All prime numbers are greater than 1
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)



# Certainly! Let's explore the differences between tuples and lists in Python:

# 1. **Mutability**:
#    - **Lists**: Lists are **mutable**, which means you can modify their elements (add, remove, or change) after creation.
#    - **Tuples**: Tuples are **immutable**, meaning once you create a tuple, you cannot change its elements. You can't add or remove items from a tuple.

# 2. **Syntax**:
#    - **Lists**: Lists are defined using square brackets (`[]`). For example: `my_list = [1, 2, 3]`.
#    - **Tuples**: Tuples are defined using parentheses (`()`). For example: `my_tuple = (1, 2, 3)`.

# 3. **Performance**:
#    - **Lists**: Lists are slightly slower than tuples because of their mutability. When you modify a list, Python needs to allocate new memory and copy the existing elements.
#    - **Tuples**: Tuples are faster because they are fixed-size and don't require reallocation when modified.

# 4. **Use Cases**:
#    - **Lists**: Use lists when you need a collection of items that can change (e.g., maintaining a dynamic list of user inputs, managing data that evolves over time).
#    - **Tuples**: Use tuples when you want to create an ordered collection of items that won't change (e.g., representing coordinates, database records, or function return values).

# 5. **Common Operations**:
#    - **Lists**: Lists support operations like appending, extending, slicing, and sorting.
#    - **Tuples**: Tuples support indexing, slicing, and iteration but do not have methods for modification.

# 6. **Examples**:
#    ```python
#    # Lists (Mutable)
#    my_list = [10, 20, 30]
#    my_list.append(40)  # Modify: Add an element
#    my_list[1] = 25     # Modify: Change an element

#    # Tuples (Immutable)
#    my_tuple = (10, 20, 30)
#    # my_tuple.append(40)  # Error: Tuples don't support append
#    # my_tuple[1] = 25    # Error: Tuples don't support item assignment
#    ```

# In summary, use lists when you need flexibility and mutability, and use tuples when you want immutability and performance benefits. Choose the appropriate data structure based on your specific requirements! 📊🔍




# # Predefined sets
# carnivores = {"lion", "tiger", "wolf", "cheetah"}
# herbivores = {"elephant", "giraffe", "deer", "zebra"}

# # Word to check
# word_to_check = "lion"

# # Check membership
# if word_to_check in carnivores:
#     print(f"{word_to_check} is a carnivore.")
# elif word_to_check in herbivores:
#     print(f"{word_to_check} is a herbivore.")
# else:
#     print(f"{word_to_check} is not in either set.")




# pg 97
# ^[aeiou][a-z]*[^aeiou]$



# # pg 104
# def count_words(file_path):
#     """
#     Counts and displays the total number of words in a text file.

#     Args:
#         file_path (str): Path to the text file.

#     Returns:
#         None
#     """
#     try:
#         with open(file_path, 'r') as file:
#             data = file.read()
#             words = data.split()
#             total_words = len(words)
#             print(f"Total words in '{file_path}': {total_words}")
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found. Please provide a valid file path.")

# # Example usage:
# count_words("lists.py")


# pg 96
# ^[a-zA-Z]+

import re
def JTOi(name):
    with open(name,"r") as file:
        data = file.read()
        # for line in file:
        x = re.template("J", data)

    return x
user = "text.txt"    
print(JTOi(user))

