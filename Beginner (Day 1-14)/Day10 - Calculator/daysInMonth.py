#Program that returns how many days in a month depending on the year inputted
def is_leap(year):
    """Takes in a year and return whether that year is a leap year or not""" #Using docstrings
    if (year % 4 == 0) or (year % 100 != 0) and (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year,month):
    """Takes in year and month and return the number of days in the month inputted""" #Using docstrings
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month == 2:
        return month_days[month-1] + 1
    else:
        return month_days[month-1]
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)