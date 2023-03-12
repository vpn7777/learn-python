def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    num = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
            num += 1
        else:
            number = number * 3 + 1
            num += 1
    return num
