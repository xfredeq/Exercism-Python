def isTriangle(sides):
    for side in sides:
        if side <= 0:
            return False

    sides = sorted(sides)
    return sides[0] + sides[1] >= sides[2]


def equilateral(sides):
    return isTriangle(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    return isTriangle(sides) and (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2])


def scalene(sides):
    return isTriangle(sides) and sides[0] != sides[1] != sides[2] and sides[0] != sides[2]
