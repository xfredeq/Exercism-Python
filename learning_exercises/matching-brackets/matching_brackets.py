OPEN_BRACKETS = {'(': 1, '[': 2, '{': 3}

CLOSING_BRACKETS = {')': 4, ']': 5, '}': 6}


def match(id1: int, id2: int) -> bool:
    return id1 % 3 == id2 % 3


def is_paired(input_string: str) -> bool:
    stack = []
    for char in input_string:
        if char in OPEN_BRACKETS.keys():
            stack.append(char)
        elif char in CLOSING_BRACKETS.keys():
            if len(stack) == 0:
                return False
            if match(OPEN_BRACKETS[stack[-1]], CLOSING_BRACKETS[char]):
                stack.pop()
            else:
                return False

    return not len(stack)
