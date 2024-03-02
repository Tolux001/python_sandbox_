# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create functions
def sayHello(name):
    print("My name is", name)

sayHello("Toluwalase")

#  Return Value

def getSum(num1, num2):
    total = num1 + num2
    return total

value = getSum(5, 98)
print(value)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# From running it, I think lambda is a single line function, i tried making it multiple lines but their was error in the first line
# I would do my research though
getDifference = lambda num1, num2: num1 - num2
sub_value = getDifference(100, 105)
print(sub_value)

#Getting used to writing functions
def military_uniform(rank, age, service_time):
    return f'You are a {rank} so respect people older especially when you are a {age} year old with not more than {service_time}'
military_uniform2 = lambda rank, age, service_time: f'You are a {rank} so respect people older especially when you are a {age} year old with not more than {service_time}'

print(military_uniform("Corporal", 23, 9))
print(military_uniform2("Corporal", 23, 9))

