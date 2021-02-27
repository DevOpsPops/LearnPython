#Determine of number is prime or not

num = 2

for i in range(2,num): #we start with 2 because prime numbers are divsible by one
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# a more efficient way of running the same thing

from math import sqrt

num = 7

for i in range(2,int(sqrt(num)+1)):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")