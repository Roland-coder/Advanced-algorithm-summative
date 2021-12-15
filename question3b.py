def encryption(n):
    # initialize counter variable
    counter = 0
    
    # initialize 2-d array with three elements
    
    matrix = [[],[],[]]
    # for loop that runs to the length of the input, n
    for i in range(0,len(n)):
        
        # if counter equals zero, the value of n with index as the loop operation to the first array in the matrix
        if counter == 0:
            matrix[0].append(n[i])
            #increment counter
            counter+=1
            
            #else if counter equals 1, the value of n with index as the loop operation to the second array in the matrix
        elif counter == 1:
            
            matrix[1].append(n[i])
            #increment counter by 1
            counter+=1
        else:
            #else the value of n with index as the loop operation to the third array in the matrix
            matrix[2].append(n[i])
            #increment by 1
            counter = 0
             # # join all elements in first, second and third array into individual strings
            # return a combination of the three
    return ''.join(matrix[0])+''.join(matrix[1])+''.join(matrix[2])
print(encryption('Plain text'))
