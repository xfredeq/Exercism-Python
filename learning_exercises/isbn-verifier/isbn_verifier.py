def is_valid(isbn: str):
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False
    
    for ch in isbn[:-1]:
        if not ch.isdecimal():
            return False
    
    if isbn[-1] != 'X' and not isbn[-1].isdecimal():
        return False

    checksum = sum((int(isbn[i]) * (10-i)) if isbn[i]!= 'X' else 10*(10-i) for i in range(10))
    return not checksum % 11


is_valid("1a2b3c")
