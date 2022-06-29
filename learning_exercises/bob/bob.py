def response(hey_bob: str):
    alpha = False
    for word in hey_bob:
        if word.isalpha():
            alpha = True

    if len(hey_bob.strip()) == 0:
        return "Fine. Be that way!"
    elif hey_bob == hey_bob.upper() and alpha:
        if hey_bob.strip().find("?") != len(hey_bob.strip())-1:
            return "Whoa, chill out!"
        else:
            return "Calm down, I know what I'm doing!"
    else:
        if hey_bob.strip().find("?") != len(hey_bob.strip())-1:
            return "Whatever."
        else:
            return "Sure."
