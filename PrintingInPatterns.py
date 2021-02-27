# print the hash pattern
 # # # #
 # # # # 
 # # # # 

#one way to do this:
print("# # # # ")
print("# # # # ")
print("# # # # ")
print("# # # # ")
print()

#print same pattern using only one hash and one print
for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()
print()

# print the hash pattern
#
# #
# # #
# # # # 

for i in range(4):
    for j in range(i+1): # we add a +1 because in a range, values start with 0
        print("# ",end="")
    print()
print()

# print the hash pattern
# # # # 
# # # 
# #
#

for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()
print()