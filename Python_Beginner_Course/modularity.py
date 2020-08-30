# coding: utf-8

# Modules

import math

print(math.sqrt(81))


def squaredNumber(number):
    return math.sqrt(number)


print(squaredNumber(81))


def even_or_odd(number):
    if number % 2 == 0:
        print(str(number) + ' is a even number.')
        return True
    else:
        print(str(number) + ' is a odd number.')
        return False


number_list = [12, 34, 1, 53, 12]

for number in number_list:
    even_or_odd(number)
