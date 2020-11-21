list_one = [1, 2, 3, "aaa", "bbb"]

print (list_one[0]) # 1
print (list_one[1]) # 2
print (list_one[2]) # 3
print (list_one[3]) # "aaa"
print (list_one[4]) # "bbb"


print ("==============")

# pass - synthetic sugar works as a placeholder for Python's interpreter.
for element in list_one:
    pass

# list_one = [1, 2, 3, "aaa", "bbb"]
# continue - allows us to move to next element in our iteration

# for element in list_one:
#
#     if element == "aaa":
#         continue
#
#     print (element)

# list_one = [1, 2, 3, "aaa", "bbb"]
# # break - allows us to break out from the iteration - stop the iteration
# for element in list_one:
#
#     if element == "aaa":
#         break
#
#     print (element)


list_one = [1, 2, 3, "aaa", "bbb"]
# range() - takes start, stop, and stride and provides range of index to loop through
#
# for i in range(0, len(list_one)+1):
#     print (list_one[i])

# print (list_one[0]) # 1
# # print (list_one[1]) # 2
# # print (list_one[2]) # 3
# # print (list_one[3]) # "aaa"
# # print (list_one[4]) # "bbb"
# # print (list_one[5]) # "bbb"


# else with a for loop - executes the code in else block after for loop is done.
list_one = [1, 2, 3, "aaa", "bbb"]
for i in range(0, len(list_one)):
    print (list_one[i])
else:
    print ('the looping is done')














