

# Unit Conversion Program from the last video.
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
        print ("MENU or number only takes integer.")
        return get_user_input()


standard_unit_mapper = {"M": 1, "KM": 0.001,
                        "CM": 100, "MM": 1000,
                        "FT": 3.280839895,
                        "IN": 39.37007874}


def convert_unit():
    try:
        while True:
            user_input = get_user_input()

            if not user_input:
                print ("The menu only takes 1 or 2")
                return convert_unit()

            if user_input.get("menu") == 2:
                break

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
    except KeyboardInterrupt as e:
        print ("\n Someone quit the program manually")


convert_unit()
