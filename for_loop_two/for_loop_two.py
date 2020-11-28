# list for loop
# list_one = [1, 2, 3, "aaa", "bbb"]
#
# for element in list_one:
#     print (element)
#
# for index in range(len(list_one)):
#     print (list_one[index])

# tuple for loop
# tuple_one = (1, 2, 3, "aaa", "bbb")
#
# for element in tuple_one:
#     print (element)
#
# for index in range(len(tuple_one)):
#     print (tuple_one[index])

# string for loop
# string_one = "DO Programming"
#
# for character in string_one:
#     print (character)
#
# for index in range(len(string_one)):
#     print (string_one[index])


# dict for loop



# for element in dict_one:
#     print (element)
#
# # wrong
# for index in range(len(dict_one)):
#     print (dict_one[index])

# items - allows us to extract out key and value together.

# dict_one = {"name": "Danny", "programming_language": "Python",
#             "channel_name": "DO Programming"}
#
# for key, value in dict_one.items():
#     print (key, value)
#
# for key in dict_one:
#     print (key, dict_one[key])
#
# # keys - allows us to extract all the keys within dict_one
#
# for key in dict_one.keys():
#     print (key)
#
# for key in dict_one:
#     print (key)
#
# # values - allows us to extract all the values within the dict_one
#
# for value in dict_one.values():
#     print (value)
#
# for key in dict_one:
#     print (dict_one[key])


# set for loop
# set_one = {"111", "111", "a", "b", "c", 4, 5, 6}
#
# for element in set_one:
#     print (element)

# 1 - convert set to list
# 2 - loop through the list

# list_one = list(set_one)
#
# for index in range(len(list_one)):
#     print (list_one[index])

# enumerate: allows us to iterate through with
# the index and element together
list_one = [1, 2, 3, "aaa", "bbb"]
dict_one = {"name": "Danny", "programming_language": "Python",
            "channel_name": "DO Programming"}

for count, element in enumerate(dict_one, 1):
    print (count, element)

# print ("============")
# for index in range(len(list_one)):
#     print (index, list_one[index])





















