"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""
#Me
def square_digits(num):
    str_num = str(num)
    result = ''
    for i in range(len(str_num)):
        x = int(str_num[i]) ** 2
        result += str(x)
    return int(result)

# best solution
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

# for review code


