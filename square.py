num = 9119
def square_digits(num):
    new = str(num)
    ans = []
    for n in new:
        print('n ', type(n))
        n = int(n)
        ans.append(n**2)
        strings = [str(integer) for integer in ans]
        a_string = "".join(strings)
        an_integer = int(a_string)
        # ans =str(ans)


    # for n in num:
    #     ans.append(n**2)
    return an_integer
print(square_digits(9119))

# Alternative Soln

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
