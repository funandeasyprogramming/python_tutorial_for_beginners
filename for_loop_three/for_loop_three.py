# list_one = ["Danny", "Eddy", "Michelle"]
#
# for name in list_one:
#     print (name)
#     for character in name:
#         if character == 'a':
#             break
#         print (character)

# nested for loop using the range() and index.

# for i in range(4):
#     print ("Outer loop {}".format(i))
#     for j in range(i):
#         print ("Inner loop {}".format(j))


# nested for loops for multiple data types.

individual_list = [
    {"personal_info": {"name": "Danny",
                       "nick_name": "Dan"},
     "programming_language": ["Python", "JavaScript"]},

    {"personal_info": {"name": "Patrick",
                       "nick_name": "Pat"},
     "programming_language": ["C#", "SQL"]},

    {"personal_info": {"name": "Mitchell",
                       "nick_name": "Mitch"},
     "programming_language": ["HTML", "CSS", "JavaScript"]}
]

for individual_counter, individual in enumerate(individual_list):
    print ("Individual# {}".format(individual_counter + 1))
    for ind_key, ind_value in individual.items():
        if ind_key == 'programming_language':
            for counter, language in enumerate(ind_value):
                print ("Language# {} - {}".format(counter + 1, language))


















