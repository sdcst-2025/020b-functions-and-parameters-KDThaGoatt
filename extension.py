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
    
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return 0
    elif discriminant == 0:
        return 1
    else:
        return 2
    
def square(a,b,c):
    try:
        sq = math.sqrt(b**2 - 4 * a * c)
        if sq.is_integer():
            return True
        if sq.is_integer(False):
            return False
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

    num_sol = numSolutions(a,b,c)

    discriminant = b**2 - 4 * a * c

    if num_sol == 0:
        #print("POS 1")
        return ("There are no solutions")
    
    if num_sol == 1 and square(a,b,c) == False:
        try:
            solution1 = (-b + math.sqrt(discriminant)) / (2 * a)
            #print("POS 2")
            return solution1
        except:
            solution2 = (-b - math.sqrt(discriminant)) / (2 * a)
            #print("POS 3")
            return solution2
        
    if num_sol == 2 and square(a,b,c) == False:
        solution1 = (-b + math.sqrt(discriminant)) / (2 * a)
        solution2 = (-b - math.sqrt(discriminant)) / (2 * a)
        #print("POS 4")
        return (solution1, solution2)
    
    if num_sol != 0 and square(a,b,c) == True:
        x = a*c
        #print("POS 5")

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
                        #print("POS 14")
                #print(li)
                #FIND AMOUNT OF NUMBERS IN THE LIST

            if len(li) == 2:

                factors = []
                solution1 = (li[0])/a
                if solution1 > 0:
                    #print("POS 6")
                    factors.append(f"x + {solution1}")
                elif solution1 == 0:
                    #print("POS 7")
                    factors.append("x")
                else:
                    #print("POS 8")
                    solution1 = solution1 * -1
                    factors.append(f"x - {solution1}")
                solution2 = (li[1])/a
                if solution2 > 0:
                    #print("POS 9")
                    factors.append(f"x + {solution2}")
                elif solution2 == 0:
                    #print("POS 10")
                    factors.append("x")
                else:
                    #print("POS 11")
                    solution2 = solution2 * -1
                    factors.append(f"x - {solution2}")
                
                return(factors)
                
            else:
                factors = []
                solution1 = ((li[0])/a)
                if solution1 > 0:
                    #print("POS 15")
                    return(f"x + {solution1}")
                elif solution1 == 0:
                    #print("POS 16")
                    return("x")
                else:
                    #print("POS 17")
                    solution1 = solution1 * -1
                    return(f"x - {solution1}")

        else:
            #print("POS 12")
            x = a*c
            li = []
            if x > 0:
                begin = -x-1
                end = x + 1
                for i in range(begin, end):
                    #print("POS 20")
                    if i != 0:
                        #print("POS 21")
                        n = x / i
                        if n + i == b:
                            #print("POS 13")
                            return (i,n)
            else:
                begin = x-1
                end = -x + 1
                for i in range(begin, end):
                    #print("POS 22")
                    if i != 0:
                        #print("POS 23")
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

while True:
    print(main())