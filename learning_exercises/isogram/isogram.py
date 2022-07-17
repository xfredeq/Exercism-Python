
def is_isogram(string: str):
    string = string.lower().replace(' ', '')
    occurences = set({l: (string.count(l) if l.isalpha() else 1) for l in string}.values())
    return not string or len(occurences) == 1 and occurences.pop() == 1
