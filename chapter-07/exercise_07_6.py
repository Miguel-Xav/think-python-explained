def uses_none(word, forbidden):
    word = word.lower() # set the word characters to lower case
    forbidden = forbidden.lower() # set the forbidden characters to lower case
    #loop
    for letter in word: # create a loop for each letter in word
        if letter in forbidden: # if the current letter is in forbidden
            return False # return False if a forbidden character is found

    return True # return True if the loop finishes without return any value
"""
The loop continues until all the characters in word is checked, if the loop do not return any value (in case of word not
having any forbidden characters), it will break end read to return True
"""

print(uses_none("banana", "xyz"))