#Assigning a list
Nums = [4,87,43,55,22,18]
#Getting value from a list
Nums[1]
Nums[2:4]
Nums[-1]

Names = ['David', 'Rachel', 'Rene', 'David', 'Anthony']

#you can make lists of lists
ListOfLists = [Nums, Names]

#modifying lists after creation
Nums.append(45) #will add this number to the end of the list
Nums.clear # will erase the values in the list
Nums.insert(2,77) # will add the number 77 to the 3rd position in the list
Nums.remove(77) # will remove number mentioned
Nums.pop(0) #will remove first indexed number listed and provide value as output
del Nums[2:4] # will delete the range of elements
Nums.extend([44,23,55]) # will and these 3 values to the end of the list

#functions of lists
min(Nums) #takes the lowest number from the list
max(Nums) # takes the highest number from the list
sum(Nums) # adds all the numbers from the list together


#Assigning a Tuple - a tuple is unmutiable
Tup = (44,66,76,43,78)
#Retrieving a number
Tup[2]

#Assigning a Set
#Sets do not define an index for items in a set
s = {55,77,33,81,16}