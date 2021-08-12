#Write a Python program to check whether the year is leap year or not.

year =int(input("enter a year: "))
if (year%4==0 & year%100 & year%400):
    print(f"yes, {year} is leap year")
else:
    print(f"no, {year} isn't leap year")
