# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def create_phone_number(num_list):

    if len(num_list) > 10 or len(num_list) <10:
        return "I need an array of 10 Numbers please"
    else:
        print('They are 10')
        # phone_num = [] #"(123) 456-7890"
        for idx, num in enumerate(num_list):
            print(idx,num)
            phone_num = "(" + str(num_list[0]) + str(num_list[1]) + str(num_list[2]) + ")"
            # if idx==2: break
            phone_num = phone_num + " " + str(num_list[3]) + str(num_list[4]) + str(num_list[5])
            phone_num = phone_num + "-" + str(num_list[6]) + str(num_list[7]) + str(num_list[8])
        print(phone_num)

# print(create_phone_number(nums))

# Alternative solution 4 Pros
def create_phone(n):
    return "({}{{}}) {}{}{}-{}{}{}{}".format(*n)
