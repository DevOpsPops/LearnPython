#get the values from the user and search for a value, get the index value

from array import *

arr = array('i',[]) #an empty array

n = int(input("Enter the length of the Array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)

# have a user search for a value in the array
val = int(input("Enter the value for search: "))

k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k+=1

#Here is a fuction that does the same thing
print(arr.index(val))