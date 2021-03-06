# 1 Create a function that takes user inputs
# 2 Create a function for unit conversion
# 3 Think and implement the strategies for the actual unit conversion


# bad strategy # 1 - 100% manual implementation - not working and not complete.
# if from_unit == "CM":
#     if to_unit == "KM":
#         print(number / 100000)
#     elif to_unit == "M":
#         print(number / 100)
#     elif to_unit == "MM":
#         print(number * 10)
# elif from_unit == "M":
#     if to_unit == "KM":
#         print(number / 100000)
#     elif to_unit == "CM":
#         print(number / 100)
#     elif to_unit == "MM":
#         print(number * 10)
# elif from_unit == "KM":
#     if to_unit == "CM":
#         print(number / 100000)
#     elif to_unit == "M":
#         print(number / 100)
#     elif to_unit == "MM":
#         print(number * 10)
# elif from_unit == "MM":
#     if to_unit == "KM":
#         print(number / 100000)
#     elif to_unit == "M":
#         print(number / 100)
#     elif to_unit == "CM":
#         print(number * 10)


# bad strategy # 2 - bit better than #1
# but still involves manual calculations
# if from_unit == "KM":
#     mapper = {"M": 1000, "CM": 100000, "MM": 1000000}
#     print(number * mapper[to_unit])
# elif from_unit == "M":
#     mapper = {"KM": 0.001, "CM": 100, "MM": 1000}
#     print(number * mapper[to_unit])
# elif from_unit == "CM":
#     mapper = {"KM": 0.00001, "M": 0.01, "MM": 10}
#     print(number * mapper[to_unit])
# elif from_unit == "MM":
#     mapper = {"KM": 0.000001, "M": 0.001, "CM": 0.1}
#     print(number * mapper[to_unit])


def get_user_input():
    print("MENU 1) Unit Conversion  2) Quit")
    try:
        menu = int(input("Choose an option from the MENU: "))
        if menu == 1:
            number = float(input("Enter a number: "))
            from_unit = input("Enter the From Unit: ")
            to_unit = input("Enter the To Unit: ")
            return {"menu": menu, "number": number,
                    "from_unit": from_unit, "to_unit": to_unit}
        elif menu == 2:
            return {"menu": menu}

    except ValueError as e:
        print ("MENU and number only takes integer values")
        return get_user_input()


standard_unit_mapper = {"M": 1, "KM": 0.001,
                        "CM": 100, "MM": 1000,
                        "FT": 3.280839895,
                        "IN": 39.37007874}


def convert_unit():
    try:
        while True:
            user_input = get_user_input()

            # if not user_input:
            #     print("MENU only takes 1 or 2")
            #     return convert_unit()

            try:
                if user_input.get("menu") == 2:
                    break
            except AttributeError as e:
                print ("MENU only takes 1 or 2")
                return convert_unit()

            number = user_input.get("number")
            from_unit = user_input.get("from_unit").upper()
            to_unit = user_input.get("to_unit").upper()

            if not (from_unit in standard_unit_mapper or
                    to_unit in standard_unit_mapper):
                print("We only allow following units: {}"
                      .format(", ".join(standard_unit_mapper.keys())))

            else:
                converted_value = standard_unit_mapper[to_unit] * number / \
                                  standard_unit_mapper[from_unit]
                result = "{} {} is {} {}".format(number, from_unit, converted_value, to_unit)
                # Standard unit mapper approach.

                print(result)
    except KeyboardInterrupt:
        print ("\nSomeone manually quit the program")




convert_unit()