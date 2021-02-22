#Bitwise Operators
    
    #Complement (~)
        #To discover the complement you'll need to go through a series of steps, 
        #1. convert the number to binary
        #2. flip all bits to the opposite value - (aka. 1's Complement), remember this binary value, you will compare it to it's complement
        #3. If you run the "~12" cmd, you will get -13. Since you cant store negative numbers in binary
        #4. for negative number, Find (1's Complement) by pretending it is positive and writing out in binary and flipping all bits
        #5. Find (2's Complement) for the negative number by adding 1 this binary value
        #6. Compare the values from binary value from value 1 and binary value from value 2, both should be the same binary values making them complements of each other       
        #This binary value will match the binary value of the original input
        ~12 #This will return -13, See operation below:
            # 12 = 00001100 --> 11110011
            #-13 --> 13 = 00001101 --> 11110010 --> 11110011
        ~13 #This will return -14
        ~14 #This will return -15

        #in short, if given a value, its complement is "-(value+1)"

    #And (&)
        #If both are true(1) it will return true (1)
        #If both are false(0) it will return true (1)
        12&13
        #If we run "12&13" we will get the value 12
            #We got here by writing out 12 in binary and 13 in binary
            #if you compare the binary values of the two, we will write out a '1' for each match and a '0' for non matches
                #12 = 00001100
                #13 = 00001101
            #   -->   00001100 --> 12
        25&30
                #25 = 00011001
                #30 = 00011110
            #   -->   00011000 --> 24

    #Or (|)
        #If either is true (1) it will return true(1)
        #if neither are true(1) it will return false(0)
        12|13
            #if you compare the binary values of the two, we will write out a '1' for each match and a '0' for non matches   
                #12 = 00001100
                #13 = 00001101
            #   -->   00001101 --> 13
        

    #XOR (^)
        #if you have one true and one false it will return true
        #if you have 2 trues or 2 falses, you will get false
        12^13
            #if you compare the binary values of the two, we will write out a '1' for each match and a '0' for non matches   
                #12 = 00001100
                #13 = 00001101
            #   -->   00000001 --> 1

    #Left Shift (<<)
        10<<2
            #10 = 00001010
            #add two zeros on the right side and remove 2 numbers on the left 
            # --> 00101000

    #Right Shift (>>)
        10>>2
            #10 = 00001010
            #add two zeros on the left side and remove 2 numbers from the right
            # --> 00000010
