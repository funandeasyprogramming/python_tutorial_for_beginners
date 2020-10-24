# dict_one = {"first_name": "Danny", "last_name": "Oh"}

# get() method - retrieves the value of an element given a key.
# print (dict_one.get("nick_name", "This is the default value"))
# print (dict_one["nick_name"])

# keys() method - retrieves all keys in dictionary
# print (dict_one.keys())

# values() method - retrieves all values in dictionary
# print (dict_one.values())

# fromkeys() method - creates a new dictionary given a sequence of items.

# keys = {"a", "b", "c"}
# values = [1, 2, 3]
#
#
# print (dict.fromkeys(keys, values))
# values.append(4)
# print (dict.fromkeys(keys, values))

# items() method - list out all the keys and values

# dict_one = {"first_name": "Danny", "last_name": "Oh"}
#
# print (dict_one.items())

# setdefault() method - gets the value based on keys if key exists
# otherwise inserts.

# dict_one = {"first_name": "Danny", "last_name": "Oh"}
# print (dict_one.setdefault("nick_name", "Dan"))
# print (dict_one)


# copy() method - returns the shallow copy of the dictionary
# dict_one = {"first_name": "Danny", "last_name": "Oh"}
# new_dict_one = dict_one.copy()
#
# print (dict_one)
# print (new_dict_one)
#
# print (new_dict_one.clear())
#
# print (dict_one)
# print (new_dict_one)
#
# print (id(dict_one))
# print (id(new_dict_one))


# update() method - 1) updates the existing value if key exists
#                   2) inserts new element if key does not exists

# dict_one = {"first_name": "Danny", "last_name": "Oh"}

# dict_one["first_name"] = "New Danny"
# dict_one["nick_name"] = "Dan"
# print (dict_one)

# dict_one.update({"first_name": "New Danny", "nick_name": "Dan"})

# dict_one.update([("first_name", "New Danny"), ("nick_name", "Dan")])
# print (dict_one)

# dict_one.update([["first_name", "New Danny"], ["nick_name", "Dan"]])
# print (dict_one)

# dict_one.update(first_name="New Danny", nick_name="Dan")
# print (dict_one)


# clear() method - clears out all the elements in the dictionary

# dict_one = {"first_name": "Danny", "last_name": "Oh"}

# print (dict_one.clear())
# print (dict_one)



# pop() method - takes key as the arguments and removes that item
# also returns the value of an items that is currently being removed.
# dict_one = {"first_name": "Danny", "last_name": "Oh"}

# removed_item = dict_one.pop("first_name")
# print (removed_item)
# print (dict_one)
#
# removed_item = dict_one.pop("nick_name", "This is the default value")
# print (removed_item)
# print (dict_one)




# popitem() method - does not take any argument, but removes the last
# inserted element by default, returns the tuple that contains
# key and value pair of an items that is being removed.

dict_one = {"first_name": "Danny", "last_name": "Oh"}
removed_item = dict_one.popitem()

print (removed_item)
print (dict_one)


















































