# Check The Exam Grade

num = int(input("Enter your marks: "))
if num >= 90:
	print("Your grade is = 'O'")
elif num >= 80 and num < 90:
	print("Your grade is = 'E'")
elif num >= 70 and num < 80:
	print("Your grade is = 'A'")
elif num >= 60 and num < 70:
	print("Your grade is = 'B'")
elif num >= 50 and num < 60:
	print("Your grade is = 'C'")
elif num >= 40 and num < 50:
	print("Your grade is = 'D'")
elif num >= 0 and num < 40:
	print("Your grade is = 'F'")
else:
	print("Invalid Entry")
