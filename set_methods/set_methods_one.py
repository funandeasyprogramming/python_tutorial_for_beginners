# Union method
# set_a = {"a", "b", "c", 1, 2, 3}
# set_b = {"c", "d", "e", 3, 4, 5}
# set_c = {5, 6, 7}

# print (set_a.union(set_b))
# print (set_b.union(set_a))
# print (set_a.union(set_b, set_c))
# print (set_b.union(set_a, set_c))

# print (set_a | set_b)
# print (set_b | set_a)


# # Intersection method
# set_a = {"a", "b", "c", 1, 2, 3}
# set_b = {"c", "d", "e", 3, 4, 5}
# set_c = {1, 2, 3}

# print (set_a.intersection(set_b))
# print (set_b.intersection(set_a))
# print (set_a.intersection(set_b, set_c))

# print (set_a & set_b)
# print (set_b & set_a)

# # Intersection Update method
# set_a = {"a", "b", "c", 1, 2, 3}
# set_b = {"c", "d", "e", 3, 4, 5}
# set_c = {1, 2, 3}
#
# # common elements: 3, "c"
#
# set_b.intersection_update(set_a, set_c)
# print (set_a)
# print (set_b)
# print (set_c)


# Difference method
# set_a = {"a", "b", "c", 1, 2, 3}
# set_b = {"c", "d", "e", 3, 4, 5}
# set_c = {1, 2, 3, 4, "d"}
#
# print (set_a.difference(set_b, set_c))
# print (set_b.difference(set_a))
#
# print (set_a - set_b)
# print (set_b - set_a)


# Difference Update method
set_a = {"a", "b", "c", 1, 2, 3}
set_b = {"c", "d", "e", 3, 4, 5}
set_c = {3, 4, 5}

# set_a.difference_update(set_b)
set_b.difference_update(set_a, set_c)
print (set_a)
print (set_b)
print (set_c)






































