def triangle(char, n): #defining the function triangle with two parameters, char (for the character to print) and n (for the number of rows)
    for i in range(n): #creating a loop that will iterate n times
        print(char * (i+1)) #printing the character char multiplied by the current iteration number + 1 (remember that python counts from 0, so we need to add 1 to have the correct number of characters printed)

triangle("L", 5) #calling the function with the character "L" and 5 rows, you can play changing the character and the number of rows to see how it works


#bonus!!!
#an function that prints a triangle aligned in the center
def triangle_center(char, n): #same basis as the previous function
    for i in range(n): #same loop as before
        space = n - i - 1 #now we are subtracting for each time the loops repeats the number of spaces needed to align the triangle to the center, we start with n spaces and for each iteration we subtract 1 space
        print(" " * space + (char * (i)) + char+(char*i)) # same as before the exercise 2, but now we add char+(char*i) to make the other side (the triangle go 1,3,5...)


triangle_center("L", 5)

#I have created this just as a challenge for myself. I think it is a good way to fix the things that we have learned in the previous exercises and also to practice with loops and string manipulation.
#I hope you find more useful bonuses as the book continues