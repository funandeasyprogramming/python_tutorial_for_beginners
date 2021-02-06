
# def print_something(a_list):
#     try:
#         raise TypeError
#         # print ("Hello {}".format(a_list[3]))
#     # Exception handles all exceptions except base exceptions.
#     except Exception as e:
#         # print (e)
#         print (repr(e))
#         # print ("There was an error and it was handled")


# Handling exception individually
# def print_something(a_list):
#     try:
#         raise AttributeError
#         # print ("Hello {}".format(a_list[3]))
#     except IndexError as e:
#         print (repr(e))
#     except AttributeError as e:
#         print (repr(e))

# else statement with try and except.
def print_something(a_list):
    try:
        print ("Hello {}".format(a_list[0]))
    except IndexError as e:
        print (repr(e))
    except AttributeError as e:
        print (repr(e))
    else:
        print ("There was no error in the try block")
    finally:
        print ("This always gets run")



print_something(["Danny", "Eddy", "Paul"])










