def leap_year(year: int):
    """Determines whether the given year is leap year

    Args:
        year (int): given year

    Returns:
        bool: True if given year is leap year, False otherwise
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
