def superdigit(n,k):
    new_digit = n*k
    loop_digit = new_digit
    
    while len(loop_digit) != 1:
        
        add = 0
        for i in range(0,len(loop_digit)):
            add+=int(loop_digit[i])
        loop_digit = str(add)
        
    return loop_digit
print(superdigit('148',3))
