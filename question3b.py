def encryption(n):
    counter = 0
    matrix = [[],[],[]]
    for i in range(0,len(n)):
        if counter == 0:
            matrix[0].append(n[i])
            counter+=1
        elif counter == 1:
            
            matrix[1].append(n[i])
            counter+=1
        else:
            matrix[2].append(n[i])
            counter = 0
    return ''.join(matrix[0])+''.join(matrix[1])+''.join(matrix[2])
print(encryption('Plain text'))