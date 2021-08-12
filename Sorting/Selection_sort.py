# Selection sort in Python

def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

# Take data from user as a array
array = []
# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input(f"Enter the {i+1} elrment: "))

    array.append(ele)  # adding the element

selectionSort(array, n)
print('Sorted Array in Ascending Order:')
print(array)
