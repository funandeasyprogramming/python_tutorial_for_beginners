
# comparison operator

number_one = 4
number_two = 5

print (number_one > number_two)
print (number_one < number_two)

print (number_one >= number_two)
print (number_one <= number_two)

print (number_one == number_two)
print (number_one != number_two)

string_one = 'abcd'
string_two = 'abce'

print (string_one > string_two)
print (string_one < string_two)

print (string_one == string_two)
print (string_one != string_two)

# logical operator - to combine the boolean values
# true or false to generate an outcome between two expressions.
# there are three types of logical operators - and, or, not

print (True and True)
print (True and False)
print (False and True)
print (False and False)

print (True or True)
print (True or False)
print (False or True)
print (False or False)

# not operator
print (not True)
print (not False)

number_one, number_two, number_three = 5, 6, 1
string_one, string_two = 'abcd', 'abcd'
#     (                                         True                         ) and True
#                        False                   or             True
print ((number_one - number_two == number_three) or (string_one == string_two) and True)

# identity operator - is

string_one = 'abcd'
string_two = 'abcd'

print (id(string_one))
print (id(string_two))
print (string_one is string_two)
print (string_one == string_two)

list_one = ['a', 'b']
list_two = ['a', 'b']
print (list_one == list_two)
print (list_one is list_two)
print (id(list_one))
print (id(list_two))

# membership operator - in

string_one = 'abcd'
print ('a' in string_one)
print ('ab' in string_one)
print ('cd' not in string_one)

student_list = ['Danny', 'Steven', 'Dan', 'Ray']
print ("Paul" in student_list)

# final example - comparison, logical, identity, and membership
number_one, number_two, number_three = 2, 3, 5
name_one, name_two = 'Danny', 'Eddy'
student_list = ['Danny', 'Steven', 'Dan', 'Ray']

print (number_one + number_two == number_three and
       name_one is not name_two and
       "Danny" in student_list)




















































