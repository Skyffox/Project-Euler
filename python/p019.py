# You are given the following information.
#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century
#       unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?
# Execution time: 0.236s

# Number of days in the months
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total = 0
# Starting monday in 1901, because 1900 was a leap year.
day = 366 % 7

for year in range(1901, 2001):
    for month in range(12):
        # Number of days in the current month.
        m = months[month]
        if day == 0:
            total += 1
        
        # Current year is a leap year.
        if m == 28 and year % 4 == 0:
            m += 1
        
        for d in range(m):
            if day == 6:
                day = 0
            else:
                day += 1

print ("Amount of Sundays that fell in the first month during the 20th century: " + str(total))
