# an array works like a list but all values in an array have to be of the same type

#In order to use an array, you will need to import a module
import array as arr

#you will need to specify what types will be in the array
# each time has a code

# TypeCode  |   C Type      |   Python Type |   Min.size in bites
#    'b'      signed char      int                1
#    'B'      unsigned char    int                1
#    'u'      Py_UNICODE       Unicode char       2
#    'h'      signed short     int                2
#    'H'      unsigned short   int                2
#    'i'      signed int       int                2
#    'I'      unsigned int     int                2
#    'l'      signed long      int                4
#    'L'      unsigned long    int                4
#    'f'      float            float              4
#    'd'      double           float              8

vals = arr.array('i',[5,9,8,4,2])
print(vals) # but this wont print the values cleanly

#instead use
print(vals.buffer_info()) # this will return your address and size of the array

vals.reverse # reverses the order of the array

print(vals[0]) #print the first value in the array
print()

#if you know the length and want to print all the values, you will need to use a loop

for i in range(5):
    print(vals[i])

#if you dont know the length
for i in range(len(vals)):
    print(vals[i])


#if you want to create another based on the values from the last array but dont know them

newArr = array(vals.typecode,(a for a in vals))