#Swapping Variable Values
a = 5
b = 6

#if you try to do this, the value of a will be overwritten and both will display 6
a = b
b = a

#to fix this you would save a to a temporary variable, a will now be 6 and b will now be 5
a = 5
temp = a
a = b
b = temp

#Option 2: swapping variables without using a 3rd variable
a = a + b #11
b = a - b #5
a = a - b #6

#Option 3: using xor is a more efficient way of using less bits
a = a ^ b
b = a ^ b
a = a ^ b

#Option 4: assign the variables on one line
a,b = b,a
