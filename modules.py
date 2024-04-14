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

# #Import custom: Importing a file that you have 
# import validator
# from validator import validate_email
# from validator import nameValidator

# # Email_validator
# email = 'tolux001@yahoo.com'
# if validate_email(email):
#     print("Email is valid")
# else:
#     print("Email is bad")

# # Name_validator
# name1 = "Tolux001"
# name2 = "Tolux001"
# print(nameValidator(name1, name2))