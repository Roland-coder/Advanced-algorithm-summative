def encryption(n):
    matrix = [[],[]]
    for i in range(0,len(n)):
        print("I is" + str(i))
        if i%2 == 0:
            
            matrix[0].append(n[i])
            print("The string is " + n[i])
        else:
            
            matrix[1].append(n[i])
    return ''.join(matrix[0])+''.join(matrix[1])
print(encryption('Plain text'))
