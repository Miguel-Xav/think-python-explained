#making the print_right function
def print_right(n): 
    count = len(n) #counting the number of characters in the string n
    space = 40 - count #calculating the number of spaces needed to align the string to the right
    print (" " * space + n) #multiplying the space by the number of spaces needed and adding the string n to align it to the right

#testing the function with the given strings
print_right("Monty")
print_right("Python's")
print_right("Flying Circus")