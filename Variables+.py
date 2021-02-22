# Variable addresses refer to a specific location in memory that the variable and value are stored in
# to retrieve the variable's adddress, use the following
# there are 3 attributes to a variable: the variable name, the box that stores the value, and the value itself
num = 5
id(num)
Name = 'David'
id(Name)

#new example
a = 10
# in python if you create a varible that is equal to another variable, it will have the same address as the referenced variable, see example:
b = a
# the address is not based on the variable name but instead, the box that stores the value, itself
id(b)
id(a)
id(10)
k=10
id(k)

#if we change the value for a to 9, it will return a different address value for a
#but b and k will still have the old address unless you update the value of b and k
a=9
k=a
b=8
#after reassigning a,b,k to new values, '10' will still exist in memory but nothing will be pointing to it
#this will go to garbage collection, meaning the memory will be available to realocated


#constant values - variables that does not change
#In Python you cannot prevent the changing of variables but you can set the intention its not to be changed
PI = 3.14
    #we can change the value of PI but why would we want to

#Determining 'Type' of a variable
type(PI)
