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
    def init(self, name, family, genres, specie):
        self.name = name
        self.family = family
        self.genres = genres
        self.specie = specie
parrot = Animal('Emmanuel', 'Biology_children_answer_this', 'one', 'two')

print(type(parrot))