def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total


print("Result Sum test: ", 1*2*3*4)
print(multiply(1,2,3,4))


def odd_or_even(number):
    multiply_of_2 = number % 2 == 0
    if multiply_of_2:
        return f'{number} is oven'
    return f'{number} is odd'

print(odd_or_even(12))



