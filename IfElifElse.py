#Testing if statements.
#using intendation tells the interpreter that print is a part of the if block or called a "Suite" in Python
if False:
    print("I'm right.")
print('bye') #print('bye') will print regardless of useing true or false since in is not apart of the indented block


#example 2  - If number is even, if number is odd

x = 8
r = x % 2

if r==0:
    print("number provided is even")

if r==1:
    print("number provided is odd")

print('bye')

#to improve the performance of the code:
x = 8
r = x % 2

if r==0:
    print("number provided is even")

else:
    print("number provided is odd")

print('bye')

#Nested If, Nested Else
x = 7
r = x % 2

if r==0:
    print("number provided is even")
    if x > 5:
        print("X is greater than 5")
    else:
        print("X is less than 5")
else:
    print("number provided is odd")

#Elif example and else
x = 1

if x==1:
    print("One")
elif x==2:
    print("Two")
elif x==3:
    print("Three")
elif x==4:
    print("Four")
else:
    print('wrong input')