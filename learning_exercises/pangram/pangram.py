def is_pangram(sentence: str):
    letters = {chr(letter): 0 for letter in range(ord('a'), ord('z')+1)}
    
    for char in sentence.lower():
        if char.isalpha():
            letters[char] += 1

    return 0 not in letters.values()

