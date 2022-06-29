def is_armstrong_number(number: int):
    return number == sum(int(d)**len(str(number)) for d in str(number))
