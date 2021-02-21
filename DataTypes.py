#Data Types

    #None - not assigned or Null

    #Numeric
        #int - a whole number
            NumInt = 5
            type(NumInt)
        #float - a demcial number
        FloatInt = 2.5
        type(FloatInt)
        #complex - number + or - an imaginary number, like negative sqrts
            CompInt = 6+9j
            type(CompInt)
        #bool - Returns a true (1) or false (0) value
            boolVal = FloatInt < NumInt
            type(boolVal)

        #Converting Numeric types
        int(FloatInt)
        float(NumInt)
        complex(FloatInt,NumInt)
        int(True)
        int(False)
    
    #Sequences
        #List
            ListExample = [1,2,3,4,5]
            type(ListExample)
        #Tuple
            TupleExample = (1,2,3,4,5)
            type(TupleExample)
        #Set
            SetExample = {1,2,3,4,5}
            type(SetExample)
        #String - characters do not exist in python, only strings
            StringExample = "David"
            type(StringExample)
        #Range - an iteration between values
            Range(0,10)
            list(range(10))
            type(range(10))
            #in a range you can count by a specific amount
                list(range(2,10,2))
            
    #Mapping or Dictionary
        #assign a key for each value
        #Note: each key should not repeat
        d = {'David':'Samsung','Rachel':'Iphone','Anthony':'Iphone'}
        #print the list of keys
            d.keys()
        #print the list of values
            d.values()
        #get a specific value, we look up keys rather than index numbers
            d['David']
            #or we can use a get method
            d.get('David')