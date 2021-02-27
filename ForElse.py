#for else examples

nums = [12,15,18,21,26]

#if this list has a number divisible by 5, print it, and stop the loop

for i in nums:
    if i % 5 == 0:
        print(i)
        break

#if the example above were to have no number divisible by 5, it would not return a print statement
#Using else can be used as a catch
#We can use else to print a not found

nums = [12,2,18,21,26]

for i in nums:
    if i % 5 == 0:
        print(i)
        break
else:
    print("Not Found") #if we didnt indent print under else, print would be returned regardless if a match was found
