def superdigit(n,k):
    # initializing new digit which is a product of the input digit and the number of times it is to be repeated
    loop_digit = n*k
    
    
    # While loop that runs so long as the length of the loop_digit is not equal to zero
    while len(loop_digit) != 1:
        
        # initialzing variable that would be used to hold temporal sum values for every iteration
        add = 0 
        
        #initialize for loop that runs from zero to the length of the loop)digit
        for i in range(0,len(loop_digit)):
            
            # incrementing our temporal sum variable with the value of the loop_digit with index location being the current for loop oeration and converting it to a string
            add+=int(loop_digit[i])
            #update loop_value with a string of ou temporal sum variable
        loop_digit = str(add)
      
    #return loop_digit
    return loop_digit
print(superdigit('148',3))
