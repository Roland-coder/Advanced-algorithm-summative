def encryption(n):
    matrix = [[],[]]
    for i in range(0,len(n)):
        if i%2 == 0:
            
            matrix[0].append(n[i])
            
        else:
            
            matrix[1].append(n[i])
    return ''.join(matrix[0])+''.join(matrix[1])
print(encryption('Plain text'))
