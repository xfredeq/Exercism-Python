def square(number: int) -> int:
    """
    :param number: int - number of field on the chessboard
    :return: int - number of grains on given square
    :raises ValueError: when number out of range[1,6]
    """

    if 0 < number <= 64:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total() -> int:
    """
    :return: int - sum of grains on all squares
    """
    return sum(square(i) for i in range(1, 65))
