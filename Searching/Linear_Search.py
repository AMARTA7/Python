def linearsearch(array, x):
   for i in range(n):
      if array[i] == x:
         return i
   return -1

array = []
# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input(f"Enter the {i+1} elrment: "))
    array.append(ele)

x =int(input("enter the number for search: "))

result = linearsearch(array, x)
print("Element is present at index", str(result))
# print("element found at index "+str(linearsearch(array,x)))
