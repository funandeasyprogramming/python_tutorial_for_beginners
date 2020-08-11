
multi_line_string_variable_one = '''
This is Danny writing
a multi-line string variable
using Python
'''

multi_line_string_variable_two = """
This is Danny writing
a multi-line string variable
using Python
"""

string_variable_one = 'This is Danny writing\n' \
                      'a multi-line string variable\n' \
                      'using Python'

print (multi_line_string_variable_one)
print (multi_line_string_variable_two)

print (string_variable_one)

first_name = "Danny"
last_name = "Oh"

print (first_name + last_name)

print (first_name * 5)

# variable[start_index:stop_index:stride]

greeting = "Welcome to DO Programming."

print (greeting[0])
print (greeting[-26])

print (greeting[-1])
print (greeting[25])

# print (greeting[26])
# print (greeting[-27])

# slicing Welcome using negative and positive indexing
print (greeting[0:7])
print (greeting[-26:-19])

# [:] = print (greeting)
print (greeting[:])

# it will slice from index of 2 until the end
print (greeting[2:])

# stride - move forward every 2 characters
print (greeting[::2])

# stride with start index
print (greeting[8::2])

# -1 as the stride = reversing a string
print (greeting[::-1])

# manual way of reversing a string
print (greeting[-1: -27: -1])

# extract out everything without first character
print (greeting[1:])

# slice Welcome using both positive and negative indexes
print (greeting[-26:7:1])

# target that we want to slice: OD ot
print (greeting[12:-19:-1])







