def is_triangle(func):
    def inner(s):
        return all([s[0] > 0, s[1] > 0, s[2] > 0,
                    sum(s) / 2 > max(s), func(s)])
    return inner


@is_triangle
def equilateral(sides):
    return is_triangle(sides) and sides[0] == sides[1] == sides[2]


@is_triangle
def isosceles(sides):
    return is_triangle(sides) and any([sides[0] == sides[1],
                                      sides[0] == sides[2],
                                      sides[1] == sides[2]])


@is_triangle
def scalene(sides):
    return all([is_triangle(sides),
               not equilateral(sides), not isosceles(sides)])
