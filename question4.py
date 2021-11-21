def superdigit(n,k):
    new_digit = n*k
    loop_digit = new_digit
    
    while len(loop_digit) != 1:
        print("Loop digit before " + loop_digit)
        add = 0
        for i in range(0,len(loop_digit)):
            add+=int(loop_digit[i])
        loop_digit = str(add)
        print("Loop digit after "+loop_digit)
    return loop_digit
print(superdigit('148',3))
