# print("I love Javascript!!")
# print("Yes, I am very good at it")

# # Creating variable

# # string
# name = "Tolux"
# print(name)

# #Sentence string
# label = "Hello " + name
# print(label)

# first_name = str(input("input is your first name: "))
# last_name = str(input("input is your last name: "))

# full_name = first_name + " " + last_name
# print("Hello " + full_name)

# # Using type : to know the data type used
# print(type(name))

# # int 
# age = 21
# # age = age + 1
# age += 1

# # print(age)
# # print(type(age))
# print(f'Your name is {age}')

# # float
# height = 259.39
# # print(height)
# # print(type(height))
# print(f'Your are {height}cm tall. The work of Beans isn your life')

# # Boolean
# Animal = True
# Human = False
# print(type(Animal))
# print(f'Are you human: {Human}, or are you an animal: {Animal}')

# # Using multiple assignment
# # Assigning strings to it value or to each other if they are equivalent
# name, age, number = "Tolux", 21, 2349038358375 
# print(number)
# print(age)
# print(name)

# age1 = age2 = age3 = age4 = 50
# print(age1)

# Built in functions/method
# Few Useful method for strings

# # Type casting: converting the data type of an element to another data type  
# number = 12
# control = "The crowd"

# number = str(number)
# print(control + number)

# # Using input
# person_name = input("Input your name: ")
# persons_age = int(input("How old are you?: "))

# persons_age += 1

# print(f'Hello {person_name}, you would be {persons_age} next year. You must be excited! Adulthood na scam')

# Using math function through import
# import math

# pi = 3.14
# print(math.ceil(pi))

# from math import ceil

# print(ceil(pi))

# PRACTICE

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

number = input("what is the number you want to get it digit sum and product: ")
digit_number_sum = 0
digit_number_product = 1

for value in number:
    digits = int(value)

    digit_number_sum += digits
    digit_number_product *= digits
print(digits, digit_number_sum, digit_number_product)