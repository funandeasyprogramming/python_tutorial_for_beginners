# while False:
#     print ("Hello Do Programming")
#
#
# count = 0
# while count < 5:
#     print ("Hello DO Programming")
#     count = count + 1
#     # count += 1

# count = 5
# # while count <= 5 and count > 0:
# #     print ("Hello DO Programming")
# #     count = count - 1
# #     # count -= 1

# Iterating a list using while loop

list_one = ["a", "b", "c", "d"]

index = 0
while index < len(list_one):
    print (list_one[index])
    index += 1


# Iterating a dictionary using while loop
dict_one = {"key1": "value1", "key2": "value2", "key3": "value3"}

dict_one_iterator_obj = iter(dict_one.items())

while True:
    try:
        dict_one_item = next(dict_one_iterator_obj)
        print (*dict_one_item)
    except StopIteration:
        print ('stop iteration error was handled')
        break

for k, v in dict_one.items():
    print (k, v)


















