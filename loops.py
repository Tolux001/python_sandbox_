# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ["John", "Paul", "Sara", "susan"]

# single for loop
# for person in people:
#     print(f'Print Name: {person}')

# for stated_person in people:
#     print(stated_person)

# for person in people:
#     if person == "Paul":
#         break
#     print(f'Name: {person}')

# for person in people:
#     if person == 'Paul':
#         continue
#     print(f'Name: {person}')

# Using Range
# for person in range(len(people)):
#     print(people[person]) 

# for i in range(len(people)):
#     print(people[i]) 

for i in range(0, 4):
    answer = i
    names = people[answer]
    print(names)

# Just Like in js,this concept can be used in py
# for(let i = 0; i < people.length; i++){
#     let Names = people[i];
#     console.log(Names)
# }
# While loops execute a set of statements as long as a condition is true.

# Starts by starting the no. it's starts from, then the while would hold where it would stop,the next line holds the increment. The count should be called to a variable before increment 

count = 0
while count < 11:
    answer = count
    count += 1
    print(f'count: {answer}')
    