# tuple:
# 1. One of the data type in Python similar to list.
# 2. It is a sequence, you can store different data type
#    inside the tuple.
# 3. Uses same slicing and indexing rules from str and list.
# 4. The only difference between tuple and list is mutability.



# tuple_one = tuple()
# print (type(tuple_one))
#
# tuple_one = 2, 4.5, "Danny"
# print (type(tuple_one))

# tuple_one = (4,)
# print (type(tuple_one))

# tuple unpacking
# tuple_one = (1, "Danny", 1.2, ['a', 'b', 3.4], (4, 5, 'hi'))
#
# element_one, element_two, element_three, \
# element_four = tuple_one
#
# print (element_one)
# print (element_two)
# print (element_three)
# print (element_four)

# tuple_one = (1, "Danny", ['a', 'b', 3], (4, 5, 'hi'))
#
# print (tuple_one[0])
# print (tuple_one[-1])
# print (tuple_one[3][0])
# print (tuple_one[0: 2])
# print (tuple_one[-4: -2])




# list_one = [1, 2, 3]

# list_one[0] = 'beginning'
#
# print (list_one)
#
#
# tuple_one = (1, "Danny", ['a', 'b', 3], (4, 5, 'hi'))
#
# tuple_one[2][0] = "Beginning"
# print (tuple_one)

# tuple_one = (1, "Danny", ['a', 'b', 3], (4, 5, 'hi'))
# tuple_two = (1, 2, 3)
#
# print (tuple_one + tuple_two)
# print (tuple_two * 3)

# del tuple_one
#
# print (tuple_one)


# tuple methods - count, index

tuple_one = ('a', 'b', 'a', 'a', 1, 2, 3, 'a')

count = tuple_one.count(5)
print (count)

index = tuple_one.index('a', 4, 8)
print (index)





















