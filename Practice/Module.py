import platform
x=platform.system()
y= dir(platform)
print(x)
print(y)

---------------------------------------------

import datetime
x= datetime.datetime.now()
y=datetime.datetime(2012, 5,6)
print(y)
print(x)
z=x-y
print(z)
print(x.year)
print(x.strftime("%A"))

----------------------------------------------

x=(1,2,4,7,5,9,10,0,55)
a= max(x)
b= min(x)
print(a)
print(b)
print(abs(-45.7865))

----------------------------------------------

import math
a=math.cos(56)
print(a)
b=math.ceil(34.01)
print(b)
c=math.floor(33.90)
print(c)
d=math.pi
print(d)

--------------------------------------------------

import json
a={
    "name":"Amarta",
    "dep":"IT",
    "yer":2019,
    "roll": 4
}
b=json.dumps(a)
print(b)

--------------------------------------------------

import json
a= json.dumps(["amarta","balai","jamuna","aronno"])
print(a)

--------------------------------------------------

import json
a={
    "name":"amarta",
    "father":"balai",
    "gFriend":("A","B","R","T"),
    "mother": "jamuna",
    "brother": ["abc","def","ghi"],
    "car":[
        {"model":"BMW","color":"black"},
        {"model":"tesla","color":"white"}
    ],
    "student":True
}
b=json.dumps(a, indent=3)
print(b)

------------------------------------------------------
import json
a={
    "name":"amarta",
    "father":"balai",
    "gFriend":("A","B","R","T"),
    "mother": "jamuna",
    "brother": ["abc","def","ghi"],
    "car":[
        {"model":"BMW","color":"black"},
        {"model":"tesla","color":"white"}
    ],
    "student":True
}
b=json.dumps(a,indent=3,separators=(".","="))
print(b)

------------------------------------------------------------

import json
a={
    "name":"amarta",
    "father":"balai",
    "gFriend":("A","B","R","T"),
    "mother": "jamuna",
    "brother": ["abc","def","ghi"],
    "car":[
        {"model":"BMW","color":"black"},
        {"model":"tesla","color":"white"}
    ],
    "student":True
}
b=json.dumps(a,indent=3, separators=(".","="),sort_keys=True)
print(b)

==============================================================================

# Q1: Write a Python program to add two matrices.

X = [[1,1,1],[2,2,2],[3,3,3]]
Y = [[4,4,4],[5,5,5],[6,6,6]]
result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):   #rows
   for j in range(len(X[0])):  #columns
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)
    
===============================================================================    
    
# Q2: Write a Python program to multiply two matrices.

X = [[1,1,1],[2,2,2],[3,3,3]]
Y = [[4,4,4],[5,5,5],[6,6,6]]
result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):   #rows
   for j in range(len(X[0])):  #columns
       result[i][j] = X[i][j] * Y[i][j]
for r in result:
   print(r)  
    
==================================================================================    
    
# Q3: Write a Python program to insert elements  in a list of n nos. and find out  the average of them.

list=[]
sum=0
element=int(input("Enter how much number u want to insert: "))
for x in range(0,element):
    y= float(input(f"enter {x+1} element: "))
    list.append(y)
print(f"Ur given List is: {list}")
for z in list:
    sum=sum+z
    avg=sum/element
print(f"SUM of ur {element} no of given input is: {sum}")
print(f"Average of ur {element} no of given input is: {avg}")    

=======================================================================================

# Q4: Write a Python program to create a list and delete an item from the list.

list=[]
sum=0
element=int(input("Enter how much number u want to insert: "))
for x in range(0,element):
    y= input(f"enter {x+1} element: ")
    list.append(y)
print(f"Ur given List is: {list}")
delete=int(input(f"Enter a index number that u want to delete it should be 0 to {element-1}: "))
if delete>=element:
    print(f"Invalid Index!! it should be 0 to {element-1}!")
else:
    list.pop(delete)
    print(f"After delete of index {delete} element the list is: {list}")
    
======================================================================================    
    
# Q5: matrix
matrix1=[]
element=int(input("Enter N x N Matrix (integer only): "))
for x in range(element):
    row=[]
    for y in range(element):
        row.append(float(input(f"enter {x+1} row {y+1} element: ")))
    matrix1.append(row)
print(matrix1)

print(f"Enter {element} x {element} Matrix:")
matrix2=[]
for x in range(element):
    column=[]
    for y in range(element):
        column.append(float(input(f"enter {x+1} row {y+1} element: ")))
    matrix2.append(column)
print(matrix2)

result = [[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]]
for i in range(len(matrix1)):
   for j in range(len(matrix2[0])):
      for k in range(len(matrix1)):
         result[i][j] += matrix1[i][k] * matrix2[k][j]
print("Ans matrix is: ")
for r in result:
    print(r)    
        
==============================================================================
    
# Q6: All Stack opperation pop(), delete(), display()

list=[]
want='yes'
def push(num):
    list.append(num)

def pop():
    print("element pop is ", list.pop())

def display():
    print("list is: " ,list)

while want=='yes':
    print("give ur choice: ")
    check=int(input("1 for push, 2 for pop, 3 for display: "))
    if check==1:
        element = int(input("Enter how much number u want to insert: "))
        for x in range(element):
            y= input(f"enter {x+1} element: ")
            list.append(y)
        print(f"Present list is: {list}")

    elif check==2:
        if not list:
            print("stack underflow!!")
        else:
            size=len(list)
            delete = int(input(f"enter index from 0 to {size-1}: "))
            list.pop(delete)
        print(f"present list is: {list}")

    elif check==3:
        display()

    else:
        print("invalid details!!")

    want=input("again ? type 'yes' or 'no': ")
     
===========================================================================    
    
# Q7: Toor plan wher u want to go

list={}
condition=True
while condition:
    name=input("Enter ur name: ")
    go=input("Where u want to go: ")
    list[name]=go
    repeat=input("R u want to go another (yes/no): ")
    if repeat=="no":
            condition=False

print("------Result------")
for name, go in list.items():
    print(f"Ur name is: {name.title()}, U registered for: {go.title()}") 
    
==================================================================================
    
# wikipedia  

import wikipedia
wikipedia.set_lang("hi")
a= wikipedia.summary("India")
print(a)

-------------------------------------------------------------------------------

# File Handling

f=open("txt1.txt")
print(f.read())

print(f.readline())
print(f.readline())

f=open("txt1.txt","a")
f.write("I am Amarta Kundu")
f.close()
g=open("txt1.txt")
print(g.read())

----------------------------------
# Open a txt file

import os
#a=open("amata.txt","x")
if os.path.exists("amata.txt"):
    os.remove("amata.txt")
else:
    print("File is not found")
     
--------------------------------------------------------------------------  
    
import pandas
data={
    'car': ['MBW', 'Volvo', 'TATA', 'Land Rover', 'Toyota', 'Hundai', 'Ford'],
    'price': [20000, 5000, 3000, 8000, 8000, 6000, 4000]
}
newData=pandas.DataFrame(data)
print(newData)
print(newData.loc[[0,1,2]])
print(pandas.__version__)


list1=["A","B","C","D","E"]
nList1=pandas.Series(list1)
print(nList1)

dic1={"Name":"AMARTA","fatherName":"BALAI","motherName":"JAMUNA"}
ndic1=pandas.Series(dic1)
print(ndic1)


df=pandas.read_csv('csv_data.csv')
print(df.to_string())


fd=pandas.read_json('json_data.js')
print(fd.info())


fd=pandas.read_csv('dirtydata_csv.csv')
print(fd.to_string())
new_fd=fd.dropna()
print(new_fd.to_string())


ak=pandas.read_csv('dirtydata_csv.csv')
print(ak)
ak.dropna(inplace=True)
print(ak)

===============================================================

# matplotlib

import matplotlib.pyplot as plt
fd=pandas.read_csv('dirtydata_csv.csv')
fd.plot(kind='scatter', x='Duration', y = 'Calories')
plt.show()
