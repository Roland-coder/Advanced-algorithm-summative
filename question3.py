def encryption(n):
    #initialize 2-D array
    matrix = [[],[]]
    
    # for loop that runs from zero to the length of n
    for i in range(0,len(n)):
        # If the current loop operation mod 2 equals zero then append the value of n with index as the loop operation to the first array in the matrix
        if i%2 == 0:
            
            matrix[0].append(n[i])
            
        else:
            # else append the value of n with index as the loop operation to the second array in the matrix
            matrix[1].append(n[i])
            
            # # join all elements in first and second array into individual strings
            # return a combination of the two
    return ''.join(matrix[0])+''.join(matrix[1])
print(encryption('Plain text'))
