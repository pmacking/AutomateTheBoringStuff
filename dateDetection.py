import re, calendar

# dateDetection regex can:
#   detect dates in DD/MM/YYYY format
#   doesn't have to detect correct days for each month or leap years
#   store strings into variables named 'month', 'day', and 'year'
# additional code that can detect if string is a valid date:
#   April, June, September & November have 30 days, February has 28 days, the rest of the monthds have 31.
#   February has 29 days in leap years:
#       Leap years are every year evenly divisible by 4
#       except for years evenly divisible by 100
#       unless years is also divisible by 400
# Assumptions:
#   days = 01 to 31 (two digits)
#   months = 01 to 12 (two digits)
#   years = 1000-2999

dateTest= '28/02/2019'
thirtyOneDayMonths=[1,3,5,7,8,11,12]
thirtyDayMonths=[4,6,9,10]

# Regex to detect date format of text
dateDetection = re.compile(r'''
    ^(\d{2}) # two digit day format with () to isolate group for detection, using ^$ so input string format is checked
    \/      # forward slash
    (\d{2}) # two digit month format with () to isolate group for detection
    \/      #forward slash
    (\d{4})$ # four digit year format with () to isolate group for detection
    ''', re.VERBOSE)

# Multiple assignment regex match, strip leading 0s, and make int
day, month, year = dateDetection.search(dateTest).groups()
day=int(day.lstrip('0'))
month=int(month.lstrip('0'))
year=int(year)

# Check that day, month, year are within acceptable ranges
while True:
    if day < 1 or day > 31:
        print ('Not a valid day 1-31: '+ str(day))
    elif month < 1 or month > 12:
        print ('Not a valid month 1-12: '+ str(month))
    elif year < 1000 or year > 2999:
        print ('Not a valid year 1000-2999: ' + str(year))
    else:
        # valid date checker based on month
        if month in thirtyDayMonths:
            if day == 31:
                print ('Not a valid date, too many days ' + (str(day)) + 'in month: ' + str(month))
        elif month == 2:
            if calendar.isleap(year) and day >= 30:
                    print('Not a valid date, too many days ' + (str(day)) + ' in month: ' + str(month))
                    print ('leap year! neato')
            elif not calendar.isleap(year) and day >= 29:
                    print('Not a valid date, too many days ' + (str(day)) + ' in month: ' + str(month))
    break