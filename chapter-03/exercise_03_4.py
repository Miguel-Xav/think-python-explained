def rectangle(char, width, height): #creating a function with the parameters char (for the character to print), width (for the number of characters in each row) and height (for the number of rows)
    for i in range(height): #creating a loop that will iterate height times
        print(char * width) #multiplying the value inside char by the width

rectangle("X", 5, 3) #calling the function with the character "X", width of 5 and height of 3, you can play changing the character, width and height to see how it works