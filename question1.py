def firstnsum(n):
    #initialize counter variable
  
    x = 0
    
    # loop through from 1 to n+1 since n is supposed to be inclusive in our sum
    for i in range(1,n+1):
        # increment counter variable by loop operation number
        x+=i
    
    # Retrun the value of x
    return x
print(firstnsum(100000))

