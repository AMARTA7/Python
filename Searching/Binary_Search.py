# Binary Search Function

def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:
		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1

array = []

# number of elements as input
n = int(input("Enter number of elements you insert: "))

# iterating till the range
for i in range(0, n):
    ele = int(input(f"Enter the {i+1} elrment: "))
    array.append(ele)  # adding the element

# What number search for
x =int(input("enter the number for search: "))

# Function call
result = binary_search(array, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
