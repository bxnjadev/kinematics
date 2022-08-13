import math


def equation_square(a, b, c):

    first_x = (- b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    second_x = (- b - math.sqrt(b ** 2 - (4 * a * c)) / (2 * a))

    return [first_x, second_x]
