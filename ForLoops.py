x = ['david',65,2.5]
print(x) # this will print the whole list 

#To print the values one by one, you will need a for loop


#example of a list print
for i in x: #i acts as a variable to store the value of each indexed item
    print(i)

#example of a string print
x = 'david'
for c in x:
    print(c)

#Printing a range
for i in range(1,10,1):
    print(i)

#Printing a range in backwards order
for i in range(10,1,-1):
    print(i)

#Printing a range in backwards order and skip printing the numbers divisible by 5
#This can be done by using an if statement
for i in range(1,21,1):
    if i%5 != 0:
        print(i)