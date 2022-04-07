from operator import inv


def create_inventory(items: list):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return {item: items.count(item) for item in items}


def add_items(inventory: dict, items: list):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    for item in items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1
        else:
            inventory[item] = 0

    return inventory


def remove_item(inventory: dict, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory.keys():
        inventory.pop(item)

    return inventory


def list_inventory(inventory: dict):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [item for item in inventory.items() if item[1] > 0]

print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))