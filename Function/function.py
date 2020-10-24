
def print_something():
    print ("Hello DO Programming")

# print_something()

# help(str)

# help(round)

# print ("Hello Danny, this is your weekly stats")
# print ("You've worked 40 hours")
# print ("You've exercised 5 hours")
# print ("You've spent 6 hours eating")
# print ("You've slept 40 hours sleeping")
#
# print ("Hello John, this is your weekly stats")
# print ("You've worked 50 hours")
# print ("You've exercised 4 hours")
# print ("You've spent 10 hours eating")
# print ("You've slept 35 hours sleeping")
#
# print ("Hello Paul, this is your weekly stats")
# print ("You've worked 3 hours")
# print ("You've exercised 1.2 hours")
# print ("You've spent 4 hours eating")
# print ("You've slept 41 hours sleeping")
#
# print ("Hello Lee, this is your weekly stats")
# print ("You've worked 10 hours")
# print ("You've exercised 0 hours")
# print ("You've spent 7 hours eating")
# print ("You've slept 70 hours sleeping")
#
# print ("Hello Bryan, this is your weekly stats")
# print ("You've worked 36 hours")
# print ("You've exercised 3 hours")
# print ("You've spent 7 hours eating")
# print ("You've slept 30 hours sleeping")

def print_weekly_stats(first_name, hours_worked, hours_excercised, hours_eating, hours_sleeping):
    """
    Prints weekly stats for different people.
    :return:
    """
    print("Hello {}, this is your weekly stats".format(first_name))
    print("You've worked {} hours".format(hours_worked))
    print("You've exercised {} hours".format(hours_excercised))
    print("You've spent {} hours eating".format(hours_eating))
    print("You've slept {} hours sleeping".format(hours_sleeping))

print_weekly_stats("Danny", 40, 5, 6, 40)
print_weekly_stats("John", 50, 4, 10, 35)
print_weekly_stats("Paul", 3, 1.2, 4, 41)
print_weekly_stats("Lee", 10, 0, 7, 70)
print_weekly_stats("Bryan", 36, 3, 7, 30)
print_weekly_stats("Eddy", 32, 3, 7, 30)

# PI * r^2

# def find_area_of_circle(radius):
#     """
#     Finds the area of circle
#     :param radius:
#     :return:
#     """
#     PI = 3.142
#     result = PI * (radius * radius)
#     return result
#     print (result)
#
#
# print (find_area_of_circle(5))
#
#
#
















