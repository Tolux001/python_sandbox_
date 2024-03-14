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


# exe 12.2
artsShelf = ["Literature", "English", "Art"]
scienceShelf = ["Physics", "Mathematics", "Chemistry", "Biology"]

print(f"Number of books in Arts shelf is {len(artsShelf)}")
print(f"Number of books in Science shelf is {len(scienceShelf)}")
print(f"Number of books in Arts and Science shelves is {len(artsShelf) + len(scienceShelf)}")

