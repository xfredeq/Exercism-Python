# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

NUMBERS = (ONES, TWOS, THREES, FOURS, FIVES, SIXES)

STRAIGHTS = (LITTLE_STRAIGHT, BIG_STRAIGHT)


def is_full_house(dice: list): return sorted(
    {value: dice.count(value) for value in dice}.values()) == [2, 3]


def four_of_a_kind(dice: list):
    values = {value: dice.count(value) for value in dice}
    try:
        num = [key for key, val in values.items() if val >= 4][0]
        return 4 * num
    except IndexError:
        return 0


def is_straight(dice: list, type):
    if type == BIG_STRAIGHT:
        return len(set(dice)) == 5 and 1 not in dice
    else:
        return len(set(dice)) == 5 and 6 not in dice


def score(dice: list, category: int):
    if category == CHOICE:
        return sum(dice)

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0

    if category in NUMBERS:
        return sum(category for i in dice if i == category)

    if category == FULL_HOUSE and is_full_house(dice):
        return sum(dice)

    if category == FOUR_OF_A_KIND:
        return four_of_a_kind(dice)

    if category in STRAIGHTS and is_straight(dice, category):
        return 30

    return 0
