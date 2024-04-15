# Python has functions for creating, reading, updating, and deleting files.

# write mode
def file(file_name):
    myFile = open(file_name, 'w')
    myFile.write('Hello this is the file I created through the use of \'FILE\'')
    myFile.close()

file('tests.txt')

# Read mode
def file1(file_name):
    myFile = open(file_name, 'r')
    text = myFile.read()
    return text

print(file1('dictionaries.py'))

# Append Mode 
def file3(file_name):
    my_file = open(file_name, 'a')
    my_file.write(' This additional text was written using mode \'a\'')
file3('tests.txt')



'''
Read mode 'r'

Write mode 'w'

append mode 'a'

binary mode 'b'

Creation mode 'x'

Update mode '+'

.write()

.close()
'''