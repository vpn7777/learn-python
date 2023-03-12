def is_armstrong_number(number):
    power = len(str(number))
    return sum([int(str(number)[i]) ** power for i in range(power)]) == number
