def rotate(text: str, key: int):
    res = ""
    for ch in text:
        if ch.isalpha():
            res += chr(ord('a') + (ord(ch) - ord('a')+key) % 26) if ch.islower() else chr(ord('A') + (ord(ch) - ord('A')+key) % 26)
        else:
            res += ch
    return res
