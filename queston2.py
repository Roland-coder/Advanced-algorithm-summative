def grade(n):
    if n <38:
        return n
    else:
        a = n%5
        if a < 3:
            return n
        else:
            return n+(5-a)
print(grade(38))
