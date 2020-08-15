# Help command displays the entire list of methods that a specific data type contains.
# help (str)

# Group 1 - capitalize, lower, islower, upper, isupper, swapcase

# capitalize() - capitalizes the first character in a given string.
capitalize_example = "danny"
# print (capitalize_example.capitalize())

# lower() - converts all upper case characters into lower case in a given string.
lower_example = "ABCDEFG"
# print (lower_example.lower())

# islower() - checks whether entire characters in a given string are lower case.
islower_example = "abcd"
# print (islower_example.islower())

# upper() - converts all lower case characters into upper case in a given string.
upper_example = "abcd eFg"
# print (upper_example.upper())

# isupper() - checks whether entire characters in a given string are upper case.
isupper_example = "CD EFG"
# print (isupper_example.isupper())

# swapcase() - swaps upper case to lower case and vice versa.
swapcase_example = "ABCD efg"
# print (swapcase_example.swapcase())

# Group 2 - format, rstrip, lstrip, strip

# format() - inserts one ore more specified values into a template string.

first_name = "Danny"
programming_language = "Python"

template_string = "Hello my name is {0}, and I love to program in {1}".format(first_name,
                                                                            programming_language)
# print (template_string)

template_string_two = "Hello my name is %s, and I love to program in %s" % (first_name,
                                                                            programming_language)
# print (template_string_two)

template_string_three = "Hello my name is " + first_name + ', and I love to program in ' + programming_language
# print (template_string_three)

# rstrip() - remove whitespaces on the right side.
rstrip_example = "abcddd "
# print (rstrip_example.rstrip('d'))

# lstrip() - remove whitespaces on the left side.
lstrip_example = " aaabcd"
# print (lstrip_example.lstrip('a'))

# strip() - removes leading and trailing spaces.
strip_example = "abcd"
# print (strip_example.strip('abd'))

# Group 3 - count, endswith, startswith, index, rindex, find, rfind, replace

# count() - counts the numbers of occurrences of the substring in a given string.
# main_string = "abcd abcd"
# sub_string = "bc"
# print (main_string.count(sub_string, 0, 4))

# endswith() - checks whether a main string endswith a substring.
# main_string = "abcd efg"
# sub_string = "d"
# print (main_string.endswith(sub_string, 0, 4))

# startswith() - checks whether a main string startswith a substring.
# main_string = "abcd efg"
# sub_string = "abcd"
# print (main_string.startswith(sub_string, 0 , 3))

# index() - finds the lowest index of a substring in a main string.
# main_string = "abcd ecfg"
# sub_string = "c"
# print (main_string.index(sub_string, 0, 4))

# rindex() - finds the highest index of a substring in a main string.
# main_string = "abcd ecfg"
# sub_string = "x"
# print (main_string.rindex(sub_string))

# find() - finds the lowest index of a substring in a main string. It returns -1 if not found.
# main_string = "abcd ecfg"
# sub_string = "x"
# print (main_string.find(sub_string))

# rfind() - finds the highest index of a substring in a main string. It returns -1 if not found.
# main_string = "abcd ecfg"
# sub_string = "x"
# print (main_string.rfind(sub_string))

# replace() - replaces the existing substring found in the main string with the new substring.
# main_string = "this is old string and old string"
# target_string = "old string"
# new_string = "new string"
# print (main_string.replace(target_string, new_string, 2))

# Group 4 - split, rsplit, join

# split() - splits a string into a list.
# split_example = "a:b:c,d,e,f"
# print (split_example.split(':', 2))

# rsplit() - split a string into a list from right only when max split is defined.
# rsplit_example = "a, b, c, d, e, f"
# print (rsplit_example.rsplit(', ', 1))
# print (rsplit_example.split(', ', 1))

# join() - joins the elements of an iterable with string separator.
join_example = ['a', 'b', 'c', 'd']
print (','.join(join_example))
