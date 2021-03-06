from secrets import randbelow


def private_key(p: int):
    return 1 + randbelow(p-1)


def public_key(p, g, private):
    return g ** private % p


def secret(p, public, private):
    return public ** private % p
