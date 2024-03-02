# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 0

# if statements
if x < x*y:
    print(f'Regular value for {x}')


# if - Else statements
if x < x*y:
    print(f'Regular value for {x}')
else: 
    print(f'y is either less than or equal to one; The value of y is {y}')


# If - else -elif statements
if x == y:
    print("they are equal")
elif x < y:
    print(f'{x} is less than {y}')
else:
    print(f'{y} is less than {x}')


# Logical operators (and, or, not) - Used to combine conditional statements

# Nesting conditional statements: Use of and, or
if x > 2 and x < 100:
    print('Happy Ending')
else:
    print('Patch it')

if x < -2 or x <  1000:
    print("Pick me!")



# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

# To confirm if value exist in a particular environment

number = [1,2,3,4,5,6]

if x in number:
    print(x in number)

if x not in number:
    print(x not in number)
else:
    print("It their big head")

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# You can return a bool when comparing two number, string, values, keys..... using "is, is not"
a = 5
b = 10
if a is b:
    print(a is b)
else:
    print("Open your eyes Guy")
