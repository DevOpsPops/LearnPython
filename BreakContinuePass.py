#Break conditions
#in this scenario we are simulating a candy machine where a user can request a max of up to 5 candy.

av = 5 #this represents the available inventory of the machine

x = int(input("How many candies do you want? "))

i = 1 
while i <= x:

    if i > av:
        print("Out of Stock")
        break #allows you to break the loop and move on to next block of code

    print ("Candy")
    i+=1

print("bye")

#Continue example
#Using continue will not jump out of the loop, it will just skip this iteration
#print numbers from 1 to 100 but dont print the values divisible by 3 or 5
r = range(1,100)

for i in r:
    if i%3 == 0:
        continue
 
    elif i%5 == 0:
        continue
    print(i)    
print("Done")

#another way to do the same thing
for i in r:
    if i%3 == 0 or i%5 == 0:
        continue
    print(i)
print("Done")


#Pass example
#Pass is used a place holder or to nullify a condtion

for i in r:
    if (1%2!=0):
        pass
    else:
        print(i)