
number_one = 5
number_two = 2

# print (number_one + number_two == 7)

# if, elif (else if), else

# if number_one + number_two == 7:
#     print ('value is 7')
# elif number_one + number_two < 7:
#     print ('value is less than 7')
# elif 6 < number_one + number_two < 10:
#     print ('value is either 7, 8, 9')
# else:
#     print ('value is greater than 9')


# if number_one + number_two == 7:
#     print ('value is 7')
# if number_one + number_two < 7:
#     print ('value is less than 7')
# if 6 < number_one + number_two < 10:
#     print ('value is either 7, 8, 9')
# if number_one + number_two > 9:
#     print ('value is greater than 9')

# calculator - 3 inputs from end users: 2 numbers and 1 operator.
def user_input():
    first_number = int(input("Enter the first number:    "))
    second_number = int(input("Enter the second number:    "))
    operator = input("Enter the operator from + - * /   ")
    return first_number, second_number, operator

def addition(first_number, second_number):
    if first_number + second_number > 100:
        print("the value is greater than 100")
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    return first_number / second_number

def exponent(first_number, second_number):
    return first_number ** second_number

def calculator():

    first_number, second_number, operator = user_input()

    if operator == '+':
        return addition(first_number, second_number)
    elif operator == '-':
        return subtraction(first_number, second_number)
    elif operator == '*':
        return multiplication(first_number, second_number)
    elif operator == '/':
        return division(first_number, second_number)
    else:
        if operator == '**':
            return exponent(first_number, second_number)
        else:
            return "Operator provided is not valid"

print (calculator())