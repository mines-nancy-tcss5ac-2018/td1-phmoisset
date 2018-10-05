#  Projet Euler
## Problem 22

def extract(file):
    l=[]
    for line in open(file,'r'): 
        """ extract a string from a file """
        l.append(line)
        """ erase and separate each name, except the first and the last one """
        p=l[0].split('","') 
        """ erase the " on the first name """
        p[0]=p[0].replace('"','') 
        """ erase the " on the last name """
        p[-1]=p[-1].replace('"','')
    return p

def value(name):
    """return the value of a name"""
    value = 0
    for letter in name: #run through the name to give each letter its value
        value += ord(letter)-64 #ord() gives the ascii number so I had to substract 64 to have the right number
                                #meaning 1 for A, 2 for B ...
    return value

assert(value('COLIN') == 53)



def solve(filepath):
    """ solve the 22th Euler problem """
    ans = 0
    for coef,name in enumerate(sorted(extract(filepath)),1): 
        #run through the list and give the row of each name
        #the 1 in enumerate is here to start the row at 1 and not at 0 
        #which would 'erase' the first name
        ans += value(name)*coef #the ans is the sum of all the name value * coef which is their row
    return ans

assert(solve('p022_names.txt') == 871198282)


    
