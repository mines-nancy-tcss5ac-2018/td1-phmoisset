#  Projet Euler
## Problem 16

def solve(n):
    """Solve the 16th Euler problem. Return the sum of the digits of 2**n."""
    number = str(2**n)
    sum = 0
    for digit in number: #run through the number 
        sum+=int(digit) #convert each digit of the string into an integer and sum it
    return sum

assert(solve(15)==26)
    

