#group 1: append, extend, insert
#group 2: remove, pop, clear
#group 3: count, reverse, sort, index, copy

# help(list)

# append - appends a new elment to the end of the list./

# list_one = [1, 2, 3]
# list_one.append(4)
# print (list_one)
# list_one.append('123')
# print (list_one)

# extend - adds all elements in an iterable(tuple, dict, list, string) to the end of the list.

# list_one = [1, 2, 3]
# list_two = [4, 5, 6]
# tuple_one = (1, 2, 3)
# string_one = 'abc'
# list_one.extend(string_one)
# print (list_one)
# print (list_one + list_two)

# insert - inserts an element into the specified index within the list.

# list_one = ['a', 'b', 'c']
# # list_one.insert(1, 'd')
# # print (list_one)
# list_one.insert(0, 'aa')
# print (list_one)

#group 2: remove, pop, clear

# remove - remove an element from the list.

# list_one = ['a', 'b', 'c']
# removed_item = list_one.remove('b')
# print (removed_item)
# print (list_one)

# pop - by default, removes the last element from the list, but you can also specify the index of the element that you want to remove.
# list_one = ['a', 'b', 'c']
# removed_item = list_one.pop(0)
# print (removed_item)
# print (list_one)


# clear - clears out all the elements in the list.
# list_one = [1, 2, 3, 4, 5, 6]
# list_one.clear()
# print (list_one)
# del list_one[:]
# print (list_one)

#group 3: count, reverse, sort, index, copy

# count - counts the number of element found in the list.

# list_one = ['a', 'b', 'c', 'a']
# count = list_one.count(4)
# print (count)

# reverse - reverses all the elements in the list.
# list_one = [1, 2, 3, 1, 2, 3]
# list_one.reverse()
# print (list_one)
# print (list_one[::-1])

# sort - sorts elements in the list either ascending or descending order.
# list_one = [1, 4, 7, 5, 2, 6, 1, 9, 3]
# list_two = ['e', 'b', 'a', 'g', 'h', 'c']
#
# list_one.sort(reverse = True)
# print (list_one)
# list_two.sort(reverse = True)
# print (list_two)

# index - returns the index of the first occurrence of an element found in the list.

# list_one = ['a', 'b', 'c', 'a', 'b', 'c']
#
# index = list_one.index('a', 3, 6)
# print (index)

# copy - creates a new list with the copied value.

list_one = [1, 2, 3]
list_two = list_one.copy()

print (list_one, list_two)
list_one.append(4)
print (list_one, list_two)
print (id(list_one), id(list_two))

# list_two = list_one
#
# print (list_one, list_two)
# list_one.append(4)
# print (list_one, list_two)
# print (id(list_one), id(list_two))






















