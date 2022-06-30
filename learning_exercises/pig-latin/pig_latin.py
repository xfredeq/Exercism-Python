from random import vonmisesvariate


VOWELS = ('a', 'e', 'i', 'u', 'o', 'yt', 'xr')


def vowel_transform(text: str) -> str:
    return text + "ay"


def move_consonants(text: str) -> str:
    if text.startswith('qu'):
        return text[2:] + text[:2]
    else:
        return text[1:] + text[0]


def translate(text: str):
    result = ''
    for word in text.split():
        if word.startswith(VOWELS):
            result += vowel_transform(word)
        else:
            if len(word) == 2 and word[1] == 'y':
                result += vowel_transform(word[::-1])
            else:
                while not word.startswith(VOWELS):
                    word = move_consonants(word)

                result += vowel_transform(word)

        result += ' '

    return result.strip()
