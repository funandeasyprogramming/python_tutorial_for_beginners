# set data type
# unordered collection data type
# does not allow duplicate elements
# mutable and iterable

# set_one = {1, 2, 3, "four", 3, (5, "five"), (5, "five")}
# print (set_one)

# set_one = set([1, 2, 3, 4, 5])
# print (set_one)
#
# set_one = set({"1": 1, "2": 2, "2": 2})
# print (set_one)

# Adding elements to set

# add - will allow us to add a single element into the set.

# set_one = {1, "2", 3, "four"}
#
# set_one.add("five")
# print (set_one)
#
# set_one.add(("six", 6))
# print (set_one)
#
# set_one.add([1, 2])
# print (set_one)

# update - allows us to add multiple elements at the same time into set.

# set_one = {"a", 2, "c", 3}
#
# set_one.update([1, 2, 3])
# print (set_one)
#
# set_one.update({1: "1", 2:"2", 5: "5"})
# print (set_one)


# methods to remove items from set - discard, remove, pop, clear



# set_one.discard(5)
# print (set_one)

# set_one.remove(5)
# print (set_one)

# pop - removes a random element from the set.

set_one = {"a", 1, "b", 2, (1, 2)}

# removed_item = set_one.pop()
# print (removed_item)
#
# print (set_one)

# set_one.clear()
# print (set_one)

# frozenset
# similar to set - the only difference is that frozenset is immutable.

f_set_one = frozenset([1, 2, 3, "a", "b", (1, 2, 3), "b"])
print (type(f_set_one))
print (f_set_one)















































