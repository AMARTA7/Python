# Q1. Write a python program to calculate average of n nos within a range.

n = int(input("Enter any integer Number:"))
totalNum = n
sum = 0
while (n >= 0):
    sum += n
    n -= 1
average = sum / totalNum
print(f"sum of {totalNum} is: {sum}")
print(f"average of {totalNum} is: {average}")

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

# Q2. Print a pattern

rows =int(input("enter a int number: "))
for i in range(1, rows + 1):        #ROWS
    for j in range(1, i + 1):       #COLUMNS
        print("*",end = ' ')
    print('')
    
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

# Q3. Write a Python program to print the reverse of a number.

n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

# Q4. Write a Python program to find out the sum & average of the digits present in a number.

n = int(input("Enter any integer number:"))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print(f"Sum of first {n} numbers is: {sum}")
average = sum / n
print(f"Average of {n} numbers is: {average}")

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

# Q5. Radius aria of a circel.
def C_radius(r):
    radius =2*3.14*r
    print(f"radius is: {radius}")
def C_aria(r):
    aria =3.14*r*r
    print(f"aria is: {aria}")
num1=int(input("enter first no: "))
C_radius(num1)
C_aria(num1)

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

# Q6. Automate WhatsApp using Python

import pywhatkit as amarta
amarta.sendwhatmsg('+917595******','Hlo friend',12,42)

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
