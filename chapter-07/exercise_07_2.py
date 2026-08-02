def uses_any(word, forbidden):
    # making all the character of the str on the parameter of the function lower case:
    word = word.lower()
    forbidden = forbidden.lower()
    for letter in word: # create a loop for each letter in word
        if letter in forbidden: # if the current character is forbidden
            return True # return True if the word uses any forbidden character
    return False # return False if the word didn't use any forbidden character

""""
remember that if the lower() is not used, if the letter in available, required and word are not upper case or lowercase
it will cause inaccurate results! (python treats 'R' and 'r' as different characters)
"""

print(uses_any("banana", "xyz"))

