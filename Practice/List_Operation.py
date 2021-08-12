# List operation made by AMARTA KUNDU:)

#List
list1=['amarta',22,'balai',43,'jamuna',99,'aronno',34,'arnob',7,9,77,30]
print(list1)

for list in list1:
	print(list)

list1.append(100)       #append
print(list1)
for list in range(245,248):
	list1.append(list)
print(list1)

list1.extend([990,999,'kundu'])        #extend
print(list1)

list1.insert(1,'KUNDU')    #insert
print(list1)

list1.remove('arnob')   #remove
print(list1)

list1.pop(7)    #pop
print(list1)

print(list1[:])   #slice
print(list1[5:-1])

print(list1[::-1])  #reverse
list1.reverse()
print(list1)

print(len(list1))     #length

print(min([100,1,9,2,19,3,4,5]))    #min/max
print(max([1,2,3,4,5]))

print(list1.count(99))    #count

list2=[100,1,9,2,19,3,4,5]   #concatenation
print(list1+list2)
print(list2+list2)

print(list2*3)    #multiply

print(list2.index(3))   #index

list2.sort()   #sort
print(list2)
