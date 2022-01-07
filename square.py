# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# 
# Note: The function accepts an integer and returns an integer

num = 9119
def square_digits(num):
    ans = []
    for int(n) in str(num):
        ans.append(n**2)
    return ans
square_digits(num)
