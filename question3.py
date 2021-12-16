def encryption(n,k):
    #initialize 2-D array
    matrix = [[] for i in range(k)]
    
    # if k != 2  or k != 3:
    #     return 'The current accepted keys are 2 and 3'
    if k == 2:
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

    elif k == 3:
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
    else:
        # if key not equal to 2 or 3 then it prints as below
        return 'function only accepts 2 and 3 as keys'

print(encryption('Plain text',2))




def decryption(n,k):
    # check if  key equals 2
    if k ==2:
        # Initalize string q that will be used to hold the first half of the input string
        string1 = n[0:round(len(n)/2)]
        # Initalize string q that will be used to hold the first half of the input string
        string2 = n[round(len(n)/2):]
        
        # initialize an empty string varibale that would hold our final output
        string = ''
        # initilzie two varibales that will be used as counters for our indices
        s1 = 0
        s2 = 0
        #for loop that runs to the length of n
        for i in range(1,len(n)+1):
            #if the loop operation mod 2 equals zero then increment string with the s1 as index in the second string
            #increment s2 counter
            if i%2 == 0:
                string +=string2[s2]
                s2+=1
            else:
                #else incriment the output string with s2 as index in first string (string1)
                string+= string1[s1] 
                s1+=1
        # Return string
        return string
    #else if k equals 3
    elif k ==3:
        
        # check for the modulus of the length of n and that with modulus of 1 
        check = (len(n)/3)%3%1
        
        # if that output is less than 0.5 and not equal to zero then create a varibale a which is equal to length of n divided by 3 rounded plus 1
        if check <0.5 and check!=0:
            a = round(len(n)/3) + 1
        else:
            # else a will simply be rounding length of n divided by 3
            a = round(len(n)/3)
        # Initalize variable b1 which gets the extra value the length of n minus a divided by two
        b1 = round((len(n) - a)/2)
        # initiaize variable b which is a plus b1 from above
        b = round(a + b1)
        # initialize variable c which is the difference between n, a and b1
        c1 = len(n) - a - b1
        # c1 which equals b plus c1
        c = b+c1
        
        # since the key is three, we divide our string into three parts, while using the variables created above to act as indices
        string1 = n[0:a]
        string2 = n[a:b]
        string3 = n[b:]
        
        # initilaize final string output
        string = ''
        # initialize three variables that would be used as counters to increment indices in our three strings created above
        s1 = 0
        s2 = 0
        s3 = 0
        # inirialize counter variable
        counter = 0
        
        # loop from zero to length of n
        for i in range(0,len(n)):
            # if counter equals zero then we increment output string with the character found at string1 index s1 and then we incremenet s1 counter and general loop counter variable called counter
            if counter == 0:
                string +=string1[s1]
                s1+=1
                counter+=1
            # else if counter equals one then we increment output string with the character found at string2 index s2 and then we incremenet s2 counter and general loop counter variable called counter

            elif counter == 1:
                string+= string2[s2] 
                s2+=1
                counter+=1
            # else we increment output string with the character found at string3 index s3 and then we incremenet s3 counter and general loop counter variable called counter is changed to zero

            else:
                string+= string3[s3] 
                s3+=1
                counter = 0
        # retrun output string
        return string
    else:
        return 'Enter valid key'
    
print(decryption('Pantxli et',2))
