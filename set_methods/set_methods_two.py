# symmetric difference - gets the set of elements that are in either
# set_a or set_b but not in both, meaning not in the intersection.
# set_a = {"a", "b", "c", 1, 2, 3}
# set_b = {"c", "d", "e", 3, 4, 5}
#
# print (set_a.symmetric_difference(set_b))
# print (set_b.symmetric_difference(set_a))
#
# print (set_a ^ set_b)
# print (set_b ^ set_a)

# symmetric difference update - updates a set with the result of symmetric difference
# set_a.symmetric_difference_update(set_b)
# print (set_a)
# print (set_b)


# issuperset - checks whether a set is a super set of another set.

# set_a = {1, 2, 3, "a"}
# set_b = {1, 2, 3, "a"}
#
# print (set_a.issuperset(set_b))
# print (set_b.issuperset(set_a))


# issubset - checks whether a set is a subset of another set.

# set_a = {1, 2, 3}
# set_b = {1, 2, 3}
#
# print (set_a.issubset(set_b))
# print (set_b.issubset(set_a))


# isdisjoint - checks whether two sets have no common elements.

# set_a = {5, 2, 3}
# set_b = {5, 6, 7}
#
# print (set_a.isdisjoint(set_b))
# print (set_b.isdisjoint(set_a))


# examples with bit more realistic data
danny = {"Python", "Java", "JavaScript", "SQL", "C#"}
eddy = {"C#", "Java", "Scala", "R", "SQL", "Python"}
jennie = {"C++", "Java", "HTML", "CSS", "JavaScript"}

# what is the list of programming languages among three people?

all_programming_languages = danny.union(eddy, jennie)
# print ("all programming languages", all_programming_languages)

# what are the common programming languages being used by three individuals?
common_programming_languages = danny.intersection(eddy, jennie)
# print ("common programming languages", common_programming_languages)

danny = {"Python", "Java", "JavaScript", "SQL", "C#"}
eddy = {"C#", "Java", "Scala", "R", "SQL", "Python"}
jennie = {"C++", "Java", "HTML", "CSS", "JavaScript"}

# what are the programming languages that are specific to each individual?

programming_languages_specific_to_danny = danny.difference(eddy, jennie)
programming_languages_specific_to_eddy = eddy.difference(danny, jennie)
programming_languages_specific_to_jennie = jennie.difference(danny, eddy)

# print (programming_languages_specific_to_danny)
# print (programming_languages_specific_to_eddy)
# print (programming_languages_specific_to_jennie)

# what are the programming languages that either Eddie
# and Jennie but not in both?
danny = {"Python", "Java", "JavaScript", "SQL", "C#"}
eddy = {"C#", "Java", "Scala", "R", "SQL", "Python"}
jennie = {"C++", "Java", "HTML", "CSS", "JavaScript"}

print (eddy.symmetric_difference(jennie))























































































