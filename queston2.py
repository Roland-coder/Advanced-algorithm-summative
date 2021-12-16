def gradingStudents(n):
    
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
print(gradingStudents(38))

# Testing the function with another function that uses a list of students and the number of students in the class

def gradingStudents(n,grades):
     # if the number of students is not equal to that specifies in the list of students grade then we return a statement
     # to show that inputs do not match
    if n != len(grades):
        return 'number of students and grades do not match'
    # printing this as headers for the output, 
    print("ID OG FG")
    # for loop that runs from zero to the number of students i
    for i in range(n):
        # for each student, print their ID, former grade, pass former grade to our grade function and print to the console
        print(grades[i][0],grades[i][1],grade(grades[i][1]))
    return " "
n = 7
grades = [[0,73],[1,67],[2,38],[3,33],[4,84],[5,27],[6,57]]

print(gradingStudents(n,grades))
