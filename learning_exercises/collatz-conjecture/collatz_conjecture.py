def steps(number: int):
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    s = 0
    while number != 1:
        s += 1
        number = number/2 if not number % 2 else 3*number + 1

    return s
