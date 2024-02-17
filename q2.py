#File: q2.py
#Author: Leah Philip
#Date: 02/16/2024
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program determines if the year inputted by user is a leap year.
year = int(input('Enter a year:'))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year.".format(year))
else:
    print("{0} is not a leap year.".format(year))
