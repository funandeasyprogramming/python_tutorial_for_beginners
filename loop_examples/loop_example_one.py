# calculate and return the average of all the numbers in the list.

list_one = [1, 2, 3, 4, 5, 6]
def calculate_average_v1(a_list):
    return sum(a_list) / len(a_list)

print (calculate_average_v1(list_one))


def calculate_average_v2(a_list):
    total = 0
    for number in a_list:
        total += number
    return total / len(a_list)

print (calculate_average_v2(list_one))

list_one = [1, 2, 3, 4, 5, 6, 7]
list_two = [1, 2, 3]

def calculate_average_v3(a_list):
    total = 0
    index = 0
    while index < len(a_list):
        total += a_list[index]
        index += 1
    return total / len(a_list)

print (calculate_average_v3(list_two))


# A function that returns a string with no
# duplicate consecutive letters.

# Input: "Daaannnyyy"
# Output: "Dany"

# Input: "Pyyythhon"
# Output: "Python"

# Input: "ABBCD"
# Output: "ABCD"

string_one = "Daaannnyyy"

def remove_duplicate_consecutive_letters(a_string):

    new_variable = ""
    for index in range(len(a_string)-1):
        print (index, index+1)
        if a_string[index] != a_string[index+1]:
            print (index, index+1, "!!!!")
            print (a_string[index])
            new_variable += a_string[index]
    return new_variable + a_string[-1]

print (remove_duplicate_consecutive_letters(string_one))

























