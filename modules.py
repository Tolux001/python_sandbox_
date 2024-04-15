# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules

import datetime
today = datetime.date.today()

print(today)

from datetime import date
today = date.today()

print(today)

import time
timeStamp = time.time()

print(timeStamp)

from time import time 
timeStamp = time()

print(timeStamp)

#Pip modules
from camelcase import CamelCase

c = CamelCase()
answer = c.hump("hello world")
print(answer)

#Custom Modules: Importing a python file you have already

from validator import dataTypeValidator
from validator import matching_number

#number function in validator.py
num1 = float(input('Value of first number: '))
num2 = float(input('Value of second number: '))

print(matching_number(num1, num2))

#name function in validator.py
name = int(input('Int or Float; Let see if you get it right: '))

print(dataTypeValidator(name))