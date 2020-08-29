
# default argument
# def print_something(programming_language, first_name="Danny"):
#     print ("{0} likes to program in {1}".format(first_name, programming_language))
# print_something("JavaScript")


# positional vs keyword arguments in function call.
def print_something(first_name, last_name, programming_language):
    print ("{0} {1} likes to program in {2}".format(first_name,
                                                    last_name,
                                                    programming_language))

# print_something("Danny", last_name="Oh", programming_language="Python")

# variable arguments - args, kwargs - takes n number of arguments into a function.

def sum_numbers(*args):
    print (sum(args))

# sum_numbers(1, 2, 3, 4, 5, 6, 7, 8)

# def print_midterm_scores(**kwargs):
#     print (kwargs)
#
# # print_midterm_scores(danny="58", eddy="57", dan="24")
#
#
# # local vs global variables
# # first_name = "Danny from global"
# def print_out_first_name():
#     first_name = "Danny from local"
#     print (first_name)
#
# print (first_name)
# print_out_first_name()

# local vs global variables
# - trying to use the global variable for variable assignment
# first_name = "Danny from global"
# def print_out_first_name():
#     global first_name
#     first_name = first_name + "Danny from local"
#     print (first_name)
#
# print (first_name)
# print_out_first_name()

# example 1 - print_introduction()

# def print_introduction(first_name, last_name, hobby="programming"):
#     print("My name is {0} {1}. My hobby is {2}"
#           .format(first_name, last_name, hobby))
#
# print_introduction(input("Enter your first name "),
#                    input("Enter your last name "))

# second example - calculate the area of circle, radius from end user.

PI = 3.14
def return_area_of_circle(radius):
    return PI * (radius * radius)

print (return_area_of_circle(int(input("Enter the radius "))))


















