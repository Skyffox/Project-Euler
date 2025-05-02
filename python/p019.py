# pylint: disable=line-too-long
"""
Problem 19: Counting Sundays

Problem description:
You are given the following information:
1 Jan 1900 was a Monday.
Thirty days has September, April, June and November. All the rest have thirty-one,
Saving February alone, which has twenty-eight, rain or shine. And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Answer: 171
"""

from utils import profiler


def is_leap_year(year: int) -> bool:
    """
    Returns True if the given year is a leap year, False otherwise.

    A leap year is divisible by 4, but if it is divisible by 100, it must also be divisible by 400.
    This function checks whether the given year satisfies the conditions for being a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, otherwise False.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False


@profiler
def compute() -> int:
    """
    Compute how many Sundays fell on the first day of the month in the timeframe from 1901 to 2000.

    This function counts how many times the first day of a month was a Sunday between the years 1901 and 2000.
    The function keeps track of the day of the week for the first day of each month, adjusting for leap years
    in February. It assumes that January 1st, 1901, was a Monday.

    Returns:
        int: The number of Sundays that fell on the first day of the month between 1901 and 2000.
    """
    # Number of days in each month (non-leap year)
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total_sundays = 0
    current_day_of_week = 366 % 7  # Starting Monday in 1901 because 1900 was a leap year.

    # Iterate through the years from 1901 to 2000
    for year in range(1901, 2001):
        for month in range(12):
            # If the first day of the month is a Sunday, increment the counter
            if current_day_of_week == 0:
                total_sundays += 1

            # Update the day of the week for the first day of the next month
            # Adjust February for leap years
            days_in_month = months[month]
            if month == 1 and is_leap_year(year):  # February
                days_in_month += 1

            # The first day of the next month is determined by adding days_in_month to current_day_of_week
            current_day_of_week = (current_day_of_week + days_in_month) % 7

    return total_sundays


if __name__ == "__main__":
    print(f"Problem 19: {compute()}")
