a_leap_year = int(input('Enter the year: '))
if a_leap_year % 4:
    if a_leap_year % 100:
        if a_leap_year % 400:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
else:
    print("Yes")