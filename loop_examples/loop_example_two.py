# Data type conversion:
# 1. List of tuples -> List of dictionaries
# 2. List of dictionaries -> List of tuples

input_list = [("name", "Danny"), ("name", "Dan"),
              ("name", "Eddy"), ("name", "Michelle")]

output_list = [{'name': 'Danny'}, {'name': 'Dan'},
               {'name': 'Eddy'}, {'name': 'Michelle'}]

result_list = list()

for tuple_element in input_list:
    result_dict = {tuple_element[0]: tuple_element[1]}
    result_list.append(result_dict)

# print (result_list)

result_list = list()
for dict_element in output_list:
    # result_tuple = ("name", dict_element.get("name"))
    # result_list.append(result_tuple)
    for key, value in dict_element.items():
        result_tuple = (key, value)
        result_list.append(result_tuple)


# print (result_list)

# 1. Add a new element into programmer's dictionary
# called operating system. And each programmer
# will have different list of operating systems.

# 2. Merge programming_languages, frameworks,
# and operating_system into one complete list
# called technical_stacks.

# 3. Destructure the information that we
# have, to create an introduction paragraph
# for each programmer.

programmers = [
    {
        "programmer_id": 1,
        "name": "Danny",
        "programming_languages": ["Python", "JavaScript", "SQL", "Java"],
        "frameworks": ["Flask", "Django", "Spring"]
    },
    {
        "programmer_id": 2,
        "name": "Eddy",
        "programming_languages": ["C#", "C++", "Mongo", "Java"],
        "frameworks": ["ASP", "Blazor", "Spring"]
    },
    {
        "programmer_id": 3,
        "name": "Steve",
        "programming_languages": ["Postgres", "JavaScript"],
        "frameworks": ["Next", "Express"]
    }
]


# 1. Add a new element into programmer's dictionary
# called operating system. And each programmer
# will have different list of operating systems.

os_mapper = {1: ["Windows", "Mac"], 2: ["Unix", "Mac"], 3: ["Linux", "Windows"]}

for programmer_dict in programmers:
    #1 - add operating system with values for each programmer
    programmer_id = programmer_dict.get("programmer_id")
    programmer_os = os_mapper.get(programmer_id)
    programmer_dict.update({"operating_system": programmer_os})

    #2 - merge all three lists into one, and delete unused lists
    technical_stacks = programmer_dict.get("programming_languages") + \
                       programmer_dict.get("frameworks") + \
                       programmer_os
    programmer_dict["technical_stacks"] = technical_stacks

    del programmer_dict["frameworks"]
    del programmer_dict["programming_languages"]
    del programmer_dict["operating_system"]

    # 3 - create a paragraph for programmer's introduction
    # ", ".join(programmer_dict.get("technical_stacks"))
    new_string = ""
    for technical_stack in programmer_dict.get("technical_stacks"):
        new_string += technical_stack
        new_string += ", "


    introduction = "Hello! My name is {}. My technical " \
                   "stacks include followings: {}"\
        .format(programmer_dict.get("name"),
                new_string[:-2])

    print (introduction)












