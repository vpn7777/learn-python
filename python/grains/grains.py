def square(number):
    if 0 < number < 65:
        return 1 << (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    return (1 << 64) - 1
