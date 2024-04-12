# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Toluwalase'

age = 20

# Concatenating
result = 'My name is ' + name + 'and I am ' + str(age)

print(result)
# String Formatting
# Using f string

result = f'My name is {name} and I am {age} years old'

print(result)

# String Methods

a = 'hello'

a = a.capitalize()
print(a)

a = a.lower()
print(a)

a = a.upper()
print(a)

a = len(a)
print(a)

# There are other string methods also

