#  Projet Euler
## Problem 16

def solve(n):
    """Solve the 16th Euler problem. Return the sum of the digits of 2**n."""
    number = str(2**n)
    sum = 0
    letter = 'a'
    for i in number:
        letter = int(i)
        sum+=letter
    return sum

assert(solve(15)==26)
    

