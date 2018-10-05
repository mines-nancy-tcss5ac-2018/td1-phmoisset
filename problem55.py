# Euler project
## Problem 55

#Lynchrel numbers

# Q: How many Lychrel numbers are there below ten-thousand?

def test_palindrome(number):
    l = len(str(number)) #define the length of the number meaning its number of digits   
    for index in range(l//2): #run through the number by each end
        if str(number)[index] != str(number)[l-index-1]: #compares the digit in a palindromic way
            return False 
    return True #if all the conditions are ok, it is a palindrome

assert(test_palindrome(12345677654321) == True) 
assert(test_palindrome(123474321) == True)
assert(test_palindrome(101) == True)


def reverse(number):
    """reverse the digits of a number"""
    reverse=str() #create an empty string
    for index in range(len(str(number))):
        reverse+=str(number)[len(str(number))-1-index] #run through the string backward
    return int(reverse)
        
assert(reverse(123456789) == 987654321)

def test_lynchrel(number):
    """determine if a number is a Lynchrel one or not"""
    for times in range(50):
        number = number + reverse(number)
        if test_palindrome(number): #if the number gives a palindrome before 50 iterations 
            return False            #it is not a lynchrel number
    return True

assert(test_lynchrel(47) == False)
assert(test_lynchrel(196) == True)

def count_lynchrel(limit): 
    """count the Lynchrel number below the limit"""
    counter = 0
    for number in range(limit):
        if test_lynchrel(number):
            counter += 1
    return counter
    

assert(count_lynchrel(10000) == 249)
    
    
    