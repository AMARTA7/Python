# Insertion sort in Python

def insertionSort(array, n):
    for step in range(1, n):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key

# Take data from user as a array
array = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input(f"Enter the {i+1} elrment: "))

    array.append(ele)  # adding the element

insertionSort(array,n)
print('Sorted Array in Ascending Order:')
print(array)
