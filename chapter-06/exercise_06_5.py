"""
In this function, it will be used Euclid's Algorithm to calculate the Greatest Common Divisor of two determined numbers
"""
def gcd(a, b):
    if b == 0: # Create a statement that if b = 0, attribute the value of a to the function
        return a
    return gcd(b, a % b) # if not, the b move to the place of a. While, a is divided by b and attribute the remainder of the division to b
#It will return (and invert) until b = 0
print(gcd(8,12)) # it will return the gcd regardless of the order
#If you don't understand very well, check a professor video explaining the Euclid`s Algorithm