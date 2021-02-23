#Using input allows a user to specify a value to through a commandlin
#Using input() will always give the string type,

X = input("input value for X: ")
Y = input("input value for Y: ")
Z = X + Y
print (Z) 

#If you want to use number values as input, use integer()

X = int(input("input value for X: "))
Y = int(input("input value for Y: "))
Z = X + Y
print (Z)

#If you want to use a single character as input:
ch = input("enter a char: ")[0]
print(ch)

#if you want to pass value at the same time of execution of the file
#you can use 'argv'
#you will need to import sys

#import sys
#X = sys.argv[1]
#Y = sys.argv[2]
#Z = X + Y
#print(Z)