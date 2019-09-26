def is_leap_year(year):
    """Returns true if the given year is a leap year."""
    if year % 400 == 0:
        return True;
    elif year % 100 == 0:
        return False;
    else:
        return year % 4 == 0


def is_valid_month(month):
    """This function returns true if a month is a valid month number. False if it's not."""
    return month >= 1 and month <= 12


def is_valid_date(year, month, day):
    """Returns true if a year is valid. Accounts for leap days."""
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    if not is_valid_month(month):
        return False
    if month == 2:
        if is_leap_year(year):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    elif month in months_with_31_days:
        return 1 <= day <= 31
    else:
        return 1 <= day <= 30


print(is_leap_year(1992), "should be True")
print(is_leap_year(2000), "should be True")
print(is_leap_year(1993), "should be False")
print(is_leap_year(1900), "should be False")

print(is_valid_month(1), "should be True")
print(is_valid_month(12), "should be True")
print(is_valid_month(0), "should be False")
print(is_valid_month(13), "should be False")

print(is_valid_date(2019, 9, 25), "should be True")
print(is_valid_date(2019, 9, 31), "should be False")
print(is_valid_date(2019, 9, 0), "should be False")
print(is_valid_date(2019, 10, 32), "should be False")
print(is_valid_date(2019, 10, 25), "should be True")
print(is_valid_date(2019, 10, 0), "should be False")
print(is_valid_date(2019, 2, 29), "should be False")
print(is_valid_date(2019, 9, 28), "should be True")
print(is_valid_date(2019, 2, 0), "should be False")
print(is_valid_date(2020, 2, 29), "should be True")
print(is_valid_date(2020, 2, 30), "should be False")