# Individual Control Center
# 1) Get user inputs among: 1) View 2) Insert 3) Update 4) Delete 5) Quit
# 2) Based on the selection, get more user inputs.
# 3) Perform various dictionary operations based on the selected option.

individual_database = {}


def user_prompt():
    user_input = int(input("Welcome to the individual control center \n"
                           "Please select an option from: \n"
                           "1) View 2) Insert 3) Update 4) Delete 5) Quit      "))
    return user_input


def individual_control_center():
    user_input = user_prompt()

    # View
    if user_input == 1:
        print("Currently there are {} individual(s) "
              "in individual database".format(len(individual_database)))
        print(individual_database)
        individual_control_center()

    # Insert
    elif user_input == 2:
        user_input_first_name = input("Enter the first name: ")
        user_input_last_name = input("Enter the last name: ")
        user_input_nick_name = input("Enter the nick name: ")

        individual_database[user_input_first_name] = \
            {"first_name": user_input_first_name,
             "last_name": user_input_last_name,
             "nick_name": user_input_nick_name}

        print ("A new individual was inserted into the individual database")
        individual_control_center()

    # Update
    elif user_input == 3:
        user_input_first_name = input("Enter the first name: ")
        if user_input_first_name in individual_database:
            # 1. get the target key and value from end user.
            # 2. retrieve value of individual (another dictionary) using the first name as the key.
            # 3. use target key and value to perform update.

            target_key = input("Enter the key:  ")
            target_value = input("Enter the value:  ")

            target_person = individual_database[user_input_first_name]
            target_person[target_key] = target_value

            if target_key == 'first_name':
                individual_database.pop(user_input_first_name)
                individual_database[target_value] = target_person
        else:
            print ("individual does not exist")

        individual_control_center()

    # Delete
    elif user_input == 4:
        user_input_first_name = input("Enter the first name: ")
        if user_input_first_name in individual_database:
            individual_database.pop(user_input_first_name)
        else:
            print("individual does not exist")
        individual_control_center()
    elif user_input == 5:
        print ("The program was terminated")

    else:
        print ("The input that you've provided is not valid")

individual_control_center()


# Limitations and things to improve

# 1. Using the first name as the key
# 1.a. Doesn't allow us to insert duplicate individual
# 1.b. Updating the first name requires deletion then re-insertion.

# 2. Using dictionary as individual database
# 2.a. If we use list, we can more easily manage multiple individuals.
# individual_database =
# [
#   {
#   "first_name": "Mitchell",
#   "last_name": "Hill",
#   "nick_name": "Mitch"
#   },
#   {
#   "first_name": "Christopher",
#   "last_name": "Jones",
#   "nick_name": "Chris"
#   }
# ]

# 3. Generally it is not recommended to use a variable to store persistent data.
# 3.a. Use proper database or caching system to properly interact
#      with the data from your program.

# 4. Using while loop instead of recursion may simplify the code a bit.
















