#Ways to create an Array:
    #array() - in an array all the elements should be of the same type
from numpy import *

arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype)

        #if a float is listed within the array, an implicate conversion will occur, changing ints to floats       

arr = array([1,2,3,4,5.0])
print(arr)
print(arr.dtype)
        
        #You can explicly convert by:

arr = array([1,2,3,4,5],float)
print(arr)
print(arr.dtype)

    #linspace() - takes three parameters (start,stop,step)
        #The step is not the number the counter jumps by, but instead breaks the range into that many parts
        #The array wil be come float if steps do not land on an integer

arr = linspace(0,16,10)
print(arr)
print(arr.dtype)

    #arange() - "a range", provide first element, last element, and step

arr = arange(0,16,2)
print(arr)
print(arr.dtype)

    #logspace() - used for logarithms

arr = logspace(1,40,5)
print(arr)
print(arr.dtype)

        #if you want to print an item in the array with out 'e'

print('%.2f' %arr[0]) 

    #zeros() - creates an array with all the numbers as zeros

arr = zeros(5)

print(arr)
print(arr.dtype)
    
    #ones() - creates an array with all the numbers as ones

arr = ones(5)
print(arr)
print(arr.dtype)
    
    #ones()