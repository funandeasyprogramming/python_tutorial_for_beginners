#
# list_one = ["a", "b", "c", "d"]
#
# index = 0
#
# while index < len(list_one):
#     current_element = list_one[index]
#     print (current_element, index)
#     index += 1
#     if current_element == "c":
#         print ("before continue")
#         continue
#     print ("final value", current_element)
# else:
#     print ("while loop iteration ended")


# nested while loop
# list_one = ["aaa", "bbb", "ccc", "ddd"]
# index = 0
# while index < len(list_one):
#     current_element = list_one[index]
#     print ("element value", current_element)
#
#     sub_index = 0
#     while sub_index < len(current_element):
#         print ("character value", current_element[sub_index])
#         sub_index += 1
#     index += 1

# nested while loop with numbers

count = 0
while count < 5:
    print ("parent while loop", count)

    sub_count = 0
    while sub_count < count:
        print ("child while loop", sub_count)
        sub_count += 1
    count +=1

















