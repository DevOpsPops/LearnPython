#Importing mathematical functions allows you to not have to write out the alegraic function but only need the input to get output
#For example we can call a mathematical function for squareroot rather than creating the underlying logic
#You will need to implort the module math to have that function available to you. Run the following:

import math

#With Import math, you now have serveral available functions to you to call from

    #Squareroot
        print(math.sqrt(25))
    
    #Floor - is used to round down to nearest whole number
        print(math.floor(2.9)) #will return 2
    
    #Ceiling - is used to round up to nearest whole number
        print(math.ceil(2.1)) #will return 3

    #Power - exponential function
        print(math.pow(3,2)) #returns 9
    
    #PI Value
        print(math.pi)

    #Epsilon
        print(math.e)

#Create an alias for an import
    #This will allow you to call 'm.f' rather than 'math.f'
        import math as m
            print(m.sqrt(25))

#If you down want to import all functions, you can take functions a la carte. To test this, close your terminal session to reapply the imports
    from math import sqrt, pow