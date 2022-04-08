"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sub_or_superlist(list_one: list, list_two: list):
    sub = True
    if len(list_two) == len(list_one):
        return UNEQUAL
    elif len(list_two) < len(list_one):
        sub = False
        list_one, list_two = list_two, list_one

    try:
        index = list_two.index(list_one[0])
        while index + len(list_one) <= len(list_two):
            if list_one == list_two[index : index+len(list_one)]:
                return SUBLIST if sub else SUPERLIST
            index = list_two.index(list_one[0], index+1)
    except:
        pass

    return UNEQUAL


def sublist(list_one: list, list_two: list):
    if list_one == list_two:
        return EQUAL
    
    if list_one == []:
        return SUBLIST
    
    if list_two == []:
        return SUPERLIST

    return sub_or_superlist(list_one, list_two)
