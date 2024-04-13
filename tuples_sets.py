# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Creating tuples : Another way of creating *list* but doesn't have a lot of functions like *list* and it's unchangeable
fruits = ("Apple", "Pineapple", "Orange", "Grape")
print(fruits)

# Always remember to use comma after a single value  
fruits_str = ("Boats")
print(fruits_str, type(fruits_str))

fruits_tuples = ("Boats",)
print(fruits_tuples, type(fruits_tuples))

# A Set is a collection which is unordered and un-indexed. No duplicate members.
fruit_set = {'Apples', 'Orange', 'Mangoes'}

print(fruit_set)

findStr = 'Apples' in fruit_set
print(findStr)

findStr = fruit_set.add('Grape')
print(fruit_set)

findStr = fruit_set.remove('Orange')
print(fruit_set)

fruit_set.clear()
print(fruit_set)

del fruit_set

