  # def read_file_into_list(filename):
#     content_list = []  # Initialize an empty list to store lines
#     try:
#         with open(filename, "r") as file:
#             for line in file:
#                 content_list.append(line.strip())  # Remove leading/trailing whitespace
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#         return None  # Return None to indicate an error
#     except Exception as e:
#         print(f"An error occurred while reading the file: {e}")
#         return None  # Return None for other exceptions
#     return content_list

# # Example usage:
# file_name = input("Name of file: ")  # Replace with your actual file name
# file_content = read_file_into_list(file_name)
# if file_content is not None:
#     print(file_content)

# star ="*"
# for i in range(0,9):

#     print(star * 10)

# def number_function(num):
#     for i in range(1, num + 1):
#         print(str(i) * i)
# num = input("Loops")
# num = int(num)
# number_function(num)



# def string_length(str1):
#     count = 0
#     for char in str1:
#         count += 1
#     return count
# print(string_length('www.unaab.edu.ng'))


# def number(num):
#     if(num > 1000):
#         print("Value is greater than 1000")
#     else:
#         print("Value is less than 1000")
# user_value = int(input("please input your number: "))
# number(user_value)


# def read_last_n_lines_naive(filename, N):
#     try:
#         with open(filename, "r") as file:
#             lines = file.readlines()[-N:]  # Read last N lines
#             for line in lines:
#                 print(line.strip())  # Remove leading/trailing whitespace
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#     except Exception as e:
#         print(f"An error occurred while reading the file: {e}")

# # Example usage:
# file_name = "your_file.txt"  # Replace with your actual file name
# N = 3  # Specify the number of lines to read
# read_last_n_lines_naive(file_name, N)



# def read_file_into_string(filename):
#     with open(filename, "r") as file:
#         content = file.read()  # Read the entire file content into a single string
#     return content

# # Example usage:
# file_name = "your_file.txt"  # Replace with your actual file name
# file_content = read_file_into_string(file_name)
# print(file_content)



# pg 26
# def replace_first_char(string):
#     first_char = string[0]
#     modified


# pg 28
# X = 0b00111100
# Y = 0b00001101
# result_and = X & Y
# print(f"X & Y = {result_and:08b}")
# Output: X & Y = 00000100

# result_not_X = ~X
# print(f"~X = {result_not_X:08b}")
# # Output: ~X = 11000011

# result_xor = X ^ Y
# print(f"X ^ Y = {result_xor:08b}")
# # Output: X ^ Y = 00111001

# result_left_shift = X << Y
# print(f"X << Y = {result_left_shift:08b}")
# # Output: X << Y = 11110000

# pg 31
# # Example: Using continue in a for loop
# for i in range(1, 90):
#     if i % 3 == 0:
#         continue  # Skip the current iteration if i is divisible by 3
#     print(i)

# # Output: 1 2 4 5 7 8 10

# # Example: Using continue in a while loop
# num = 0
# while num < 10:
#     num += 1
#     if num % 2 == 0:
#         continue  # Skip the current iteration if num is even
#     print(num)

# # Output: 1 3 5 7 9

# pg 33
# import array as arr

# # Create an array of 10 integers
# my_array = []
# for i in range(1, 11):
#     i = int(input("Input your array values: "))
#     my_array.append(i)
# # print(my_array)

# # Display elements with index values 2, 5, and 7
# print(f"Element at index 2: {my_array[2]}")
# print(f"Element at index 5: {my_array[5]}")
# print(f"Element at index 7: {my_array[7]}")

# pg 34
# Given array
# dept = ["csc", "sts", "mts", "chm", "phs"]

# # Sort the array in ascending order
# dept.sort()

# # Print the sorted array
# print("Sorted array in ascending order:", dept)

# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8,2,3,0,7)))




# # pg 36
# import cmath

# def solve_quadratic_equation(a, b, c):
#     # Calculate the discriminant
#     discriminant = b**2 - 4*a*c

#     # Check the value of the discriminant
#     if discriminant > 0:
#         # Real and different roots
#         root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
#         root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
#         print(f"Roots are real and different:")
#         print(f"Root 1: {root1}")
#         print(f"Root 2: {root2}")
#     elif discriminant == 0:
#         # Real and equal roots
#         root = -b / (2*a)
#         print(f"Roots are real and equal:")
#         print(f"Root: {root}")
#     else:
#         # Complex roots
#         real_part = -b / (2*a)
#         imaginary_part = cmath.sqrt(-discriminant) / (2*a)
#         root1 = complex(real_part, imaginary_part)
#         root2 = complex(real_part, -imaginary_part)
#         print(f"Roots are complex:")
#         print(f"Root 1: {root1}")
#         print(f"Root 2: {root2}")

# # Example usage
# a = int(input("what is the value of a: "))
# b = int(input("what is the value of b: "))
# c = int(input("what is the value of c: "))
# solve_quadratic_equation(a, b, c)





# pg 41
# # Sample data: Names and email addresses of lecturers
# lecturers = [
#     {"name": "John Doe", "email": "john.doe@example.com"},
#     {"name": "Alice Smith", "email": "alice.smith@example.com"},
#     {"name": "Robert Johnson", "email": "robert.johnson@example.com"},
#     {"name": "Emily Brown", "email": "emily.brown@example.com"},
#     # Add more lecturers as needed
# ]

# # Sort the lecturers by name (ascending order)
# sorted_lecturers = sorted(lecturers, key=lambda x: x["name"])

# # Display the sorted names and email addresses
# print("Lecturers in alphabetical order:")
# for lecturer in sorted_lecturers:
#     print(f"Name: {lecturer['name']}, Email: {lecturer['email']}")



# list_of_books = []
# def book_array():
#     num = int(input("How many numbers of books do you want to store: "))
#     for x in range(0, num):
#         x = str(input("Input the names of the books: "))
#         list_of_books.append(x)
#     return list_of_books
# print(book_array())


# write a python proto search for a given element in an array of INTEGER values
# write a python program to create and print an array of strings values

