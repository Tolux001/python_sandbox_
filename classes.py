# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Creating class

# for js guys: you should remember
# class Animal {
#     constructor(name, legs){
#     this.name = name
#     this.legs = legs
#     }
# }
# let Parrot = new Animal("Sophia", 2)


# In python
from copyreg import constructor


class Animal:
    # constructor
    def __init__(self, name, family, genres, specie):
        self.name = name
        self.family = family
        self.genres = genres
        self.specie = specie
parrot = Animal('Emmanuel', 'Biology_children_answer_this', 'one', 'two')

print(type(parrot))

# Classes
class Self:
    def __init__(self, name, age, email, stack, github):
        self.name = name
        self.age = age
        self.email = email
        self.stack = stack
        self.github = github
    def my_specs(self):
        return f'My name is {self.name} and I am currently {self.age}. Send opportunities my way via {self.email}, currently achieving the {self.stack} stack to my platter; and yes {self.github} github account is mine'
    
Tolux = Self('Toluwalase', 22, 'toluwalasepeter001@gmail.com', 'MERN', 'tolux001')

print(Tolux.my_specs())

# Using Extends

class Universities:
    # constructor
    def __init__(self, test1, test2, test3):
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
    # Methods
    def test_score(self):
        self.test1 += self.test2
        return self.test1
    def department(self):
        return self.test3

# Extending universities
class Funaab(Universities):
    # constructor
    def __init__(self, test1, test2, test3, college):
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.college = college
    def department(self):
        return f'The {self.college} is current the best after being awarded {self.test1} medals of honor'
    
    # setting a parameter outside the constructor and inside a function
    def set_balance(self, balance):
        self.balance = balance
        return f'You currently have {self.balance} in your wallet'
    
# Accessing methods in the extended(super) class and overwriting them
test = Funaab(50, 130, 'Computer_Science', 'College of physical science')

print(test.test_score()) # Accessing a method in the parent class || Updating the value of test1
print(test.department())
print(test.set_balance(300))

# Ps: Make sure '__init__' and 'self' to call parameter is used in the constructor