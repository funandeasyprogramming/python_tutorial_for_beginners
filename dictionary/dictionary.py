# dict_one = {"name": "Danny"}
# print (type(dict_one))
# print (dict_one)
#
# dict_one = dict()
# print (type(dict_one))

# key - value pair
# dict_one = {"name": "Danny", "namex": "Danny"}
# print (dict_one)

# key

# 1. key should be unique.
# 2. only immutable data type can be used as the key

# immutable data type - str, int, float, boolean, tuple
# mutable data type - list, dict

# dict_one = {"name": "Danny"}
# print (dict_one)
#
# dict_one = {("name", "name"): "Danny"}
# print (dict_one)
#
# dict_one = {0: "Danny"}
# print (dict_one)
#
# dict_one = {["name", "name"]: "Danny"}
# print (dict_one)

# value
dict_one["person"]['hobby'] = "Programming"
dict_one = {"person": {"first_name": "Danny", "last_name": "Oh", }}
# dict_one = {"name": "Danny", "another_name": "Danny"}
# print (dict_one)
#
# dict_one = {"name": ["Danny", "Paul", "Eddy"]}
# print (dict_one)
#
# dict_one = {"name": ("Danny", "Paul", "Eddy")}
# print (dict_one)
#
# dict_one = {"name": {"first_name": "Danny", "last_name": "Oh"}}
# print (dict_one)

# Accessing value of an element using key.
# dict_one = {
#     "individuals":
#         [{"first_name": "Danny", "last_name": "Oh"},
#          {"first_name": "Mitchell", "last_name": "Hill"}],
#     "video": "python tutorial"}

# print (dict_one["individual"])
# print (dict_one["video"])
# print (dict_one["individuals"][0]["last_name"])
#
# print (dict_one.get("individual", "key does not exist"))
# print (dict_one.get("video"))
# print (dict_one["individuals"][0].get('last_name'))

# dict_one = {
#     "individuals":
#         [{"first_name": "Danny", "last_name": "Oh"},
#          {"first_name": "Mitchell", "last_name": "Hill"}],
#     "video": "python tutorial"}

# Adding a new element into dictionary
# dict_one["individuals"][0]["hobby"] = "programming"
# print (dict_one)


# dict_one["new_video"] = "javascript tutorial"
# print (dict_one)


# Updating the value of an existing element using the key.
dict_one = {
    "individuals":
        [{"first_name": "Danny", "last_name": "Oh"},
         {"first_name": "Mitchell", "last_name": "Hill"}],
    "video": "python tutorial"}

# dict_one["individuals"][0]["last_namex"] = "New Last Name"
# print (dict_one)

# dict_one["individuals"] = []
# dict_one["video"] = "javascript tutorial"
# print (dict_one)

# Deleting one or more elements in the dictionary.
dict_one = {
    "individuals":
        [{"first_name": "Danny", "last_name": "Oh"},
         {"first_name": "Mitchell", "last_name": "Hill"}],
    "video": "python tutorial"}

# 1 - pop()
# dict_one["individuals"][0].pop("last_name")
# print (dict_one)
# removed_item = dict_one.pop("video")
# print ("This item is removed", removed_item)
# print (dict_one)

# 2 - popitem()
dict_one = {
    "individuals":
        [{"first_name": "Danny", "last_name": "Oh"},
         {"first_name": "Mitchell", "last_name": "Hill"}],
    "video": "python tutorial"}

# removed_item = dict_one.popitem()
# print ("This item is removed", removed_item)
# print (dict_one)

# 3 - clear()
# dict_one = {
#     "individuals":
#         [{"first_name": "Danny", "last_name": "Oh"},
#          {"first_name": "Mitchell", "last_name": "Hill"}],
#     "video": "python tutorial"}
# dict_one["individuals"][0].clear()
# print (dict_one)

# dict_one.clear()
# print (dict_one)
# Other operations - len(), membership operator (in)
dict_one = {
    "individuals":
        [{"first_name": "Danny", "last_name": "Oh"},
         {"first_name": "Mitchell", "last_name": "Hill"}],
    "video": "python tutorial"}

# print (len(dict_one["individuals"][0]))


print ("individuals" in dict_one)


dict_one = {"name": "Danny"}

dict_one = dict()




































