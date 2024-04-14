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
        return f'My name is {self.name} and I am currently {self.age}. Send opportunities my way via {self.email}, currently a {self.stack}; and yes {self.github} github account is mine'
    
Tolux = Self('Toluwalase', 22, 'toluwalasepeter001@gmail.com', 'MERN', 'tolux001')

print(Tolux.my_specs())

# Using Extends

# Ps: Make sure '__init__' and 'self' to call parameter is used in the constructor