#!python3
"""
NOTE:
If you complete this extension, call your teacher over to have it assessed


Create a program to determine the solutions for a quadratic equation
in the format ax^2 + bx + c = 0
A key is the discriminant: b^2 - 4 * a * c
If the discriminant is negative, there are no solutions
If the discriminant is zero, there is only 1 solution
If the discriminant is positive, there are 2 solutions

If the discriminant is a perfect square, then the equation can
be factored

If the discriminant is non zero, the solutions are:
x = (-b + sqrt(b^2 - 4 * a * c)) / 2a
x = (-b - sqrt(b^2 - 4 * a * c)) / 2a

Assignment criteria:
Create a program that inputs 3 float values: a, b, c
function numSolutions(a,b,c) returns an integer with the number of solutions
function solutions(a,b,c) returns a tuple with the solutions (note that if 1 solution,
then both solutions will be the same)

If there are no solutions:
output is: "There are no real solutions"

If there is one solution:
output is "There is 1 solution, x=??"

If there are two solutions:
output is: "The solutions are x=?? and x=??"
"""

import math

perfSquare = False

def numSolutions(a,b,c):
    # inputs:
    # float a
    # float b
    # float c
    # Description:
    #
    # return 0, 1 or 2

    if (b**2 - 4 * a * c) < 0:
        return 0
    if (b**2 - 4 * a * c) == 0:
        return 1
    if (b**2 - 4 * a * c) > 0:
        return 2
    
def square(a,b,c):
    try:
        sq = math.sqrt(b**2 - 4 * a * c)
        if sq % 1 == 0:
            return True
    except:
        return False

def solutions(a,b,c):
    #inputs:
    # float a
    # float b
    # float c
    # Desription:
    #
    # return tuple of float solution1 and float solution2


    if numSolutions(a,b,c) == 0:
        return ("There are no solutions")
    
    if numSolutions(a,b,c) == 1 and square(a,b,c) == False:
        try:
            solution1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
            return solution1
        except:
            solution2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
            return solution2
        
    if numSolutions(a,b,c) == 2 and square(a,b,c) == False:
        solution1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
        solution2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
        return (solution1, solution2)
    
    if numSolutions(a,b,c) != 0 and square(a,b,c) == True:
        x = a*c
        print(x)

        if x > 0:
            li = []
            begin = -x-1
            end = x + 1
            #print(begin,end)
            for i in range(begin,end):
                #print(i)
                if i != 0:
                    n = x / i
                    #print(x,i,n)
                    if n + i == b:
                        li.insert(i, n)
                #print(li)
            solution1 = (a+li[0])/a
            if solution1 > 0:
                return (f"x + {solution1}")
            if solution1 == 0:
                return ("x")
            if solution1 < 0:
                return (f"x - {solution1}")
            solution2 = (a+li[1])/a
            if solution2 > 0:
                return (f"x + {solution2}")
            if solution2 == 0:
                return ("x")
            if solution2 < 0:
                return (f"x - {solution2}")
                
        else:
            li = []
            for i in range(x-1,-x+1):
                if i != 0:
                    n = x / i
                    if n + i == b:
                        return (i,n)
                


def title():
    # inputs none
    # return str of All the title and instructions on one line
    return "This program solves quadratic equations by the quadratic formula and if the discriminant is a perfect square, it will factor it. Input your three numbers for A, B, and C."


def main():
    # Display Title and Instructions
    print( title() )
    # Your code and function calls should go here
    a = int(input("Enter the value for A: "))
    b = int(input("Enter the value for B: "))
    c = int(input("Enter the value for C: "))
    answer = solutions(a,b,c)
    return answer

a = main()
print(a)

# PRINT OUT DATA ALONG THE SOLVING PROCESS TO CONFIRM IT, VALUES 12,54,23