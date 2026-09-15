"""
Counting the Pallor!
A function to count the number of times pale, and it's variations, exist in The Count of Monte Cristo
"""

def pallor_counter(file_read):
    reader = open(file_read)
    target_words = ["palle", "pales", "paled", "paleness", "pallor"] # create a list of the words you wanna find
    counter = 0 # counter of the occurs of the target words in the .txt file
    for i in reader: # loop for each line of the file
        for word in target_words: # see if the line of the book contain a target_words
            if word in i: # if it has
                counter += 1 # sum 1 to the counter, and repeat the loop until the final of the book
    reader.close() # close the reader for save memory
    return counter # return the counter as value of the function

print(pallor_counter("pg1184.txt")) # return 36
