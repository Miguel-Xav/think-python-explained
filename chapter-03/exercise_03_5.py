def bottle_verse(n):
    for n in range(99, 0, -1): #creating a loop that will start with 99 and will end with 1, we are using -1 to decrease the value of n in each iteration
        print (f"{n} bottles of beer on the wall") #the print (f"") is a way to format the string, we are using the value of n inside the string to print the number of bottles of beer
        print (f"{n} bottles of beer") #don't worry, the book will cover print(f"") in the future
        print ("Take one down, pass it around") 
        if n-1 == 0: #the if will check the value of n-1, if it is 0, it will print the last verse of the song
            print ("No more bottles of beer on the wall")
            print ("You drink they last one, you go to the store and buy some more")
        else: #the else will be executed if n-1 not attend the if condition
            pass #the pass command do literally nothing, we need it here because we can't have an empty else statement, but we don't want to do anything if n-1 is not 0, so we just put pass


bottle_verse(99) #caution, this will print the whole song with the 99 verses, if you are testing and not want a spam, change the value of the parameter to a smaller number
