a_leap_year = int(input('Enter the year: '))
year = a_leap_year % 4 % 100 != 0 % 400 and "No" or "Yes"
print(year)