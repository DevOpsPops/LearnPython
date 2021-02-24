#initialization
i = 0
#condition
while i < 5:
    print ("Hello")
#Increment/Decrement
    i = i + 1 




#decending count

#initialization
i = 5
#condition
while i > 0:
    print ("Hello", i)
#Increment/Decrement
    i = i - 1 



#while loop in a while loop
#initialization
i = 5

#condition
while i > 0:
    j = 5
    print ("Hello: ", end="") # makes it so a new line is not started
    #condition within the condition
    while j > 0:
        print("echo ", end="") # makes it so that a new line is not started
        #Increment/Decrement
        j = j - 1
#Increment/Decrement
    i = i - 1 
    print() #prints a blank line