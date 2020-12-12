# 2, 3, 5, 7, 11 ....
# 12 - divisible by 2, 3, 4, 6

def get_user_input():
    user_input = int(input("Enter an integer: "))
    return user_input

def check_prime_number():
    user_input = get_user_input()
    if user_input > 1:
        for i in range(2, user_input):
            if user_input % i == 0:
                return False
        else:
            return True
    else:
        return False

# print (check_prime_number())


# Get range of prime numbers

def get_range_prime_number():
    user_input = get_user_input()
    for index in range(user_input + 1):
        if index > 1:
            for i in range(2, index):
                if index % i == 0:
                    print ("Not prime", index)
                    break
            else:
                print ("Prime", index)
        else:
            print ("Not prime", index)

# get_range_prime_number()


# reversing all elements in the list
list_one = ["a", "b", "c", "d"]

print (list_one[::-1])

new_list = []
for i in range(len(list_one)-1, -1, -1):
    new_list.append(list_one[i])

print (new_list)


new_list = []
for i in range(len(list_one)):
    new_list.append(list_one[len(list_one)-i-1])

print (new_list)



























