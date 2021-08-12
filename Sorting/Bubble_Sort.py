# Creating a bubble sort function

def bubble_sort(list1):
    # Outer loop for traverse the entire list
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1

# Take data from user as an array
array = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input(f"Enter the {i+1} elrment: "))

    array.append(ele)  # adding the element

print("The unsorted list is: ", array)

# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(array))
