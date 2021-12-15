def grade(n):
    
    # if n is less than 38 then return n 
    if n <38:
        return n
    else:
        # else if n is not less than 38, we initialize new_variable a which equals the mod of n and 5
        a = n%5
        # if a is less than 3 return n
        if a < 3:
            return n
        else:
            #else return the sum of n and the difference between 5 and a
            return n+(5-a)
print(grade(38))
