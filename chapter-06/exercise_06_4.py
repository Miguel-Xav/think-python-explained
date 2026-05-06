"""
A Ackermann's Function in Python
"""
def ackermann(m, n):
    if m == 0: # The first statement is if m = 0
        return n+1 # if m = 0 is true, return the value of n+1
    elif m > 0 and n == 0: # The second statement is if m > 0 and n == 0
        return ackermann(m-1, 1)# if m > 0 and n = 0, call the function with m-1 and n = 1
    elif m > 0 and n > 0: # now the last statement, if m > 0 and n > 0
        return ackermann(m-1, ackermann(m, n-1)) # if its true, call the function m and n-1, inside a call of m-1
    return None


print(ackermann(5, 5))
"""
Run the function with the parameters 5 for m and n will cause a recursion error
That error is Python protecting your processor from exploding (causa it cause a recursion running more than 1000 times)
If you like the idea of the Ackermann's Function i recommend see a real professors explaining really because its a complex theme 
"""